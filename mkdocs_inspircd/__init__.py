"""
Preprocesses data files docs/*/modules/*.yml into markdown, so they can
be built by MkDocs like regular pages.
"""

import fnmatch
import pathlib
import os.path

import mkdocs.plugins
import mkdocs.structure.files
import jinja2
import yaml


def yml2md(filename, template):
    with open(filename) as fd:
        data = yaml.safe_load(fd)
    return template.render(data)


class ExtendedFile(mkdocs.structure.files.File):
    """Like the original File class, but can also be a .yml module
    description."""

    def __init__(self, file, dest_dir, use_directory_urls):
        self.__dict__.update(file.__dict__)  # copy all attributes

        # Copy-pasted from mkdocs.structure.files.File's init;
        # but we need to run them again now that .yml are recognized
        # as documentation pages.
        self.dest_path = self._get_dest_path(use_directory_urls)
        self.abs_dest_path = os.path.normpath(os.path.join(dest_dir, self.dest_path))
        self.url = self._get_url(use_directory_urls)

    def is_documentation_page(self):
        return super().is_documentation_page() or self.is_inspircd_module_yaml()

    def is_inspircd_module_yaml(self):
        return fnmatch.fnmatch(self.src_path, "*/modules/*.yml")


class InspircdPlugin(mkdocs.plugins.BasePlugin):
    def __init__(self):
        super().__init__()
        self.env = jinja2.Environment(
            loader=jinja2.PackageLoader(__name__),
        )
        self.module_template = self.env.get_template("module.md.j2")

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
            return yml2md(page.file.abs_src_path, template=self.module_template)
