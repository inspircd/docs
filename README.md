## About

InspIRCd is a modular C++ Internet Relay Chat (IRC) server for UNIX-like and Windows systems.

This repository contains the sources for the documentation available at [docs.inspircd.org](https://docs.inspircd.org).

## Development

The documentation is built with [MkDocs](https://www.mkdocs.org). You can install this along with all of the other dependencies using [pip](https://pip.pypa.io/en/stable/) using the following command:

```sh
pip3 install -r requirements.txt
```

Depending on your system you may need to run this as root for a system-wide install.

Once the dependencies are installed you can run the site using the following command:

```sh
mkdocs serve
```
