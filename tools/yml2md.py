#!/usr/bin/env python3

import pathlib

import jinja2
import yaml

ROOT = pathlib.Path(__file__).parent.parent

ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(ROOT / "tools"),
    undefined=jinja2.StrictUndefined,  # error when using undefined variables
)

MODULE_TEMPLATE = ENV.get_template("module.md.j2")

for source_filename in (ROOT / "docs" / "3" / "modules").glob("*.yml"):
    with open(source_filename) as fd:
        data = yaml.safe_load(fd)

    target_filename = source_filename.with_suffix(".md")

    try:
        output = MODULE_TEMPLATE.render(data)
    except:
        print(f"Error while rendering {source_filename.name}:")
        raise
    with open(target_filename, "w") as fd:
        fd.write(output)
