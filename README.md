## About

InspIRCd is a modular C++ Internet Relay Chat (IRC) server for UNIX-like and Windows systems.

This repository contains the sources for the documentation available at [docs.inspircd.org](https://docs.inspircd.org).

## Development

The documentation is built with [MkDocs](https://www.mkdocs.org). You can install this along with all of the other dependencies using [pip](https://pip.pypa.io/en/stable/) using the following command:

```sh
pip3 install -r requirements.txt .
```

Depending on your system you may need to run this as root for a system-wide install.

Once the dependencies are installed you can run the site using the following command:

```sh
mkdocs serve
```

## Documentation Structure

### Content

Most of it is in `docs/3/`, which is the documentation of the current major release. The core documentation directly in it, and module documentation in in a subfolder.
Each module is documented by a YAML file, that is formatted by the MkDocs extension using `mkdocs_inspircd/templates/module.md.j2`.
The data is also interpreted by the documentation to generate tables in the core documentation (eg. to provide a list of all commands of all modules).

`docs/4/` contains preparatory work for the next major release.

### MkDocs extension

`mkdocs_inspircd/` contains an extension for MkDocs, that does two things things:

#### Rendering module documentation

All module pages are very similar in structure, so we decided to generate them from data files instead of repeating the markdown code.
This avoids inconsistencies, and easier changes in the structure; and to access module information programmatically.

To do this, the MkDocs extension implements [the `on_files` hook](https://www.mkdocs.org/dev-guide/plugins/#on_files), so MkDocs detects `.yml` files as source files (as if they were `.md`).

It also implements [the `on_page_read_source` hook](https://www.mkdocs.org/dev-guide/plugins/#on_page_read_source) to convert the YAML content to Markdown on the fly, because MkDocs tries to parse it.
This is done simply by rending `mkdocs_inspircd/templates/module.md.j2` with the YAML content as context.

#### Jinja templating for Markdown

Some pages, like `docs/3/channel-modes.md`, use dynamic data to populate tables (eg. the table of all plugins' channel modes) without duplicating data from plugins.
This is done by the [the `on_page_markdown` hook](https://www.mkdocs.org/dev-guide/plugins/#on_page_markdown), which is executed just before MkDocs parses renders Markdown.
This hook interprets Markdown documents as if they were Jinja templates, and passes them module data in the context; which produces the final Markdown document.

### License

This documentation is licensed under the same license as InspIRCd (GPLv2).
