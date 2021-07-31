"""Standalone script to test the output the plugin would give from
a yaml file

Usage: python3 -m mkdocs_inspircd.yml2md <filename>"""

import os.path
import sys

import jinja2

from . import yml2md

def main(filename):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
        undefined=jinja2.StrictUndefined,  # error when using undefined variables
    )
    module_template = env.get_template("module.md.j2")

    print(yml2md(filename, module_template))

if __name__ == "__main__":
    (_, filename) = sys.argv
    main(filename)
