"""
Preprocesses data files docs/*/modules/*.yml into markdown, so they can
be built by MkDocs like regular pages.
"""

import collections
import fnmatch
import functools
import glob
import pathlib

import mkdocs.exceptions
import mkdocs.plugins
import mkdocs.structure.files
import jinja2
import mergedeep;
import yaml

PACKAGE_DIR = pathlib.Path(__file__).parent.resolve()
TEMPLATES_DIR = PACKAGE_DIR / "templates"


@functools.lru_cache(10240)
def load_yaml(filename):
    with filename.open() as fd:
        result = yaml.safe_load(fd)
        if result is not None and 'INHERIT' in result:
            relpath = result.pop('INHERIT')
            abspath = filename.parent / relpath
            if not abspath.exists():
                raise mkdocs.exceptions.ConfigurationError(f"Inherited data file '{relpath}' does not exist at '{abspath}'.")
            parent = load_yaml(abspath)
            result = mergedeep.merge(parent, result)
        return result

def yml2md(filename, template):
    return template.render(load_yaml(filename))


class ExtendedFile(mkdocs.structure.files.File):
    """Like the original File class, but can also be a .yml module
    description."""

    def __init__(self, file, dest_dir, use_directory_urls):
        self.__dict__.update(file.__dict__)  # copy all attributes

        # Copy-pasted from mkdocs.structure.files.File's init;
        # but we need to run them again now that .yml are recognized
        # as documentation pages.
        self.dest_path = self._get_dest_path(use_directory_urls)
        self.abs_dest_path = pathlib.Path(dest_dir) / self.dest_path
        self.url = self._get_url(use_directory_urls)

    def is_documentation_page(self):
        return super().is_documentation_page() or self.is_inspircd_module_yaml() or self.is_inspircd_servermsg_yaml()

    def is_inspircd_module_yaml(self):
        return fnmatch.fnmatch(self.src_path, "*/modules/*.yml")

    def is_inspircd_servermsg_yaml(self):
        return fnmatch.fnmatch(self.src_path, "server/messages/*.yml")

class InspircdPlugin(mkdocs.plugins.BasePlugin):
    def __init__(self):
        super().__init__()
        self._modules = None
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader([TEMPLATES_DIR]),
        )
        self.module_template = self.env.get_template("module.md.j2")
        self.servermsg_template = self.env.get_template("servermsg.md.j2")

    def on_files(self, files, config):
        """Converts all original mkdocs.structure.files.File files to this
        plugin's ExtendedFile class, which behaves the same but accepts .yml
        files as input."""
        return mkdocs.structure.files.Files(
            [
                ExtendedFile(file, config["site_dir"], config["use_directory_urls"])
                for file in files
            ]
        )

    def on_page_read_source(self, page, config):
        """Replaces MkDocs's open() to read source files by reading the file
        directly and pre-rendering it to Markdown."""
        if page.file.is_inspircd_module_yaml():
            return yml2md(
                pathlib.Path(page.file.abs_src_path), template=self.module_template
            )
        elif page.file.is_inspircd_servermsg_yaml():
            return yml2md(
                pathlib.Path(page.file.abs_src_path), template=self.servermsg_template
            )

    def modules(self, config, version):
        if version is None:
            return []
        if self._modules is None:
            self._modules = []
            for module_file in pathlib.Path(config["docs_dir"]).glob(version + "/modules/*.yml"):
                self._modules.append(load_yaml(module_file))
        return self._modules

    def chmodes(self, config, version):
        modules = self.modules(config, version)
        return [
            {**mode, "module": module["name"]}
            for module in modules
            if "chmodes" in module
            for mode in module["chmodes"]["chars"]
        ]

    def umodes(self, config, version):
        modules = self.modules(config, version)
        return [
            {**mode, "module": module["name"]}
            for module in modules
            if "umodes" in module
            for mode in module["umodes"]["chars"]
        ]

    def extbans(self, config, type, version):
        modules = self.modules(config, version)
        return [
            {**extban, "module": module["name"]}
            for module in modules
            if "extbans" in module
            for extban in module["extbans"]["chars"]
            if extban["type"] == type
        ]

    def snomasks(self, config, version):
        modules = self.modules(config, version)
        return [
            {**snomask, "module": module["name"]}
            for module in modules
            if "snomasks" in module
            for snomask in module["snomasks"]
        ]

    def extra_tag_fields(self, config, version):
        extra_tag_fields = collections.defaultdict(
            lambda: collections.defaultdict(list)
        )

        for module in self.modules(config, version):
            for module_tag in module.get("configuration", []):
                if module_tag.get("extends", False):
                    # Some modules describe two tags at the same time
                    if isinstance(module_tag["name"], str):
                        tag_names = [module_tag["name"]]
                    else:
                        tag_names = module_tag["name"]

                    for name in tag_names:
                        for field in module_tag.get("attributes", []):
                            tagname = field["name"]
                            if isinstance(tagname, dict):
                                tagname = next(iter(tagname))
                            extra_tag_fields[name][tagname].append(
                                {
                                    "module": module["name"],
                                    **field,
                                }
                            )
        return extra_tag_fields

    def core_config_tags(self, config, version):
        if version is None:
            return []
        paths = pathlib.Path(config["docs_dir"]).glob(version + "/configuration/_*.yml")
        paths = sorted(paths)  # sorts by config name
        return [load_yaml(path) for path in paths]

    def core_commands(self, config, version):
        if version is None:
            return []
        paths = pathlib.Path(config["docs_dir"]).glob(version + "/commands/_*.yml")
        paths = sorted(paths)  # sorts by command name
        return [load_yaml(path) for path in paths]

    def server_messages(self, config):
        paths = pathlib.Path(config["docs_dir"]).glob("server/messages/*.yml")
        paths = sorted(paths)  # sorts by message name
        return [load_yaml(path) for path in paths]

    def page_version(self, url):
        segments = url.split("/")
        if segments[0].isdigit():
            return segments[0]

    def on_page_markdown(self, markdown, page, config, files):
        """Runs Jinja on an input markdown file, to produce another markdown file."""
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader([TEMPLATES_DIR, config["docs_dir"]]),
        )
        version = self.page_version(page.url)
        context = {
            "module_chmodes": self.chmodes(config, version),
            "module_umodes": self.umodes(config, version),
            "acting_module_extbans": self.extbans(config, "Acting", version),
            "matching_module_extbans": self.extbans(config, "Matching", version),
            "module_snomasks": self.snomasks(config, version),
            "extra_tag_fields": self.extra_tag_fields(config, version),
            "core_config_tags": self.core_config_tags(config, version),
            "core_commands": self.core_commands(config, version),
            "server_messages": self.server_messages(config),
            "version": version,
        }
        template = env.from_string(markdown)
        return template.render(context)
