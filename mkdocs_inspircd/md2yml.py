"""Converts existing .md files to the new .yml.

Usage: python3 -m mkdocs_inspircd.md2yml <filename>"""

import re
import sys

import yaml

# Parse the document structure:
RE = r"""^---
title: "Module Details: (?P<name1>\S*) \(v3\)"
---

## The "(?P<name2>\S*)" Module
(?P<introduction>.*?
)?
### Description

(?P<description>.*?)

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="(?P<name3>\S*)">
```

(?P<configuration>.*?)
(
### Commands
(?P<commands>.*?)
)?(
### Client Capabilities
(?P<caps>.*?)
)?(
### Channel Modes
(?P<chmodes>.*?)
)?(
### User Modes
(?P<umodes>.*?)
)?(
### Exemptions
(?P<exemptions>.*?)
)?(
### Extended Bans
(?P<extbans>.*?)
)?(
### Server Notice Masks
(?P<snomasks>.*?)
)?(
### Statistics
(?P<stats>.*?)
)?(
### Special Notes
(?P<special_notes>.*?)
)?$"""

# Parse a single config tag:
CONFIG_RE = r"""#### `(?P<name><\S*>)`

(?P<description>.*?)

(?P<attributes>Name.*?
----.*?)

(?P<details>.*?)##### Example Usage

(?P<example>.*?)
(?=#)"""

# Parse channel modes and extbans:
MODES_RE = r"""(?P<description>.*?

)?(?P<chars>(Name|Character).*?
----.*?)(

#### Example Usage
(?P<example>.*))?$"""

COMMANDS_RE = r"""(?P<commands>.*?)(

(?P<details>.*?

)?#### Example Usage
(?P<example>.*))?$"""


class md_block:
    """formats a block of markdown as a |- yaml block."""
    def __init__(self, *lines):
        self.data = "\n".join(lines)


def md_block_representer(dumper, data: md_block):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data.data, style="|")


def dict_representer(dumper, data: dict):
    """Formats a dict by preserving the original order (py >= 3.7 only!)"""
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


class Dumper(yaml.Dumper):
    pass


Dumper.add_representer(md_block, md_block_representer)
Dumper.add_representer(dict, dict_representer)


def removeprefix(text, prefix):
    """Like Python 3.9's str.removeprefix"""
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def parse_table(s):
    rows = s.strip().split("\n")
    rows = [[cell.strip() for cell in row.split(" | ")] for row in rows]
    (headers, ruler, *rows) = rows
    return [dict(zip(headers, row)) for row in rows]


def main(filename):
    with open(filename) as fd:
        content = fd.read()

    match = re.match(RE, content, re.DOTALL)
    groups = match.groupdict()
    if not (groups["name1"] == groups["name2"] == groups["name3"]):
        print("Mismatched names.")
        exit(1)


    output = {
        "name": groups["name1"],
    }

    if groups["introduction"]:
        output["introduction"] = groups["introduction"].strip()

    output["description"] = md_block(groups["description"])

    parse_configuration(groups, output)
    parse_chmodes(groups, output)
    parse_umodes(groups, output)
    parse_commands(groups, output)
    parse_caps(groups, output)
    parse_exemptions(groups, output)
    parse_extbans(groups, output)
    parse_snomasks(groups, output)
    parse_stats(groups, output)
    parse_special_notes(groups, output)

    print(yaml.dump(output, Dumper=Dumper))

def parse_configuration(groups, output):
    configuration = groups["configuration"]
    if configuration.strip() != "This module requires no other configuration.":
        output["configuration"] = [
            {
                "name": m.group("name"),
                "description": md_block(m.group("description")),
                "attributes": [
                    {
                        "name": row["Name"],
                        "type": row["Type"],
                        "required": "Required!" in row["Description"],
                        "default": "None" if row["Default Value"] == "*None*" else row["Default Value"],
                        "description": md_block(removeprefix(row["Description"], "**Required!** ")),
                    }
                    for row in parse_table(m.group("attributes"))
                ],
                "details": md_block(m.group("details")),
                "example": md_block(m.group("example").strip()),
            }
            for m in re.finditer(CONFIG_RE, configuration + "\n#", re.DOTALL)
        ]

def parse_chmodes(groups, output):
    chmodes = groups["chmodes"]
    if chmodes:
        m = re.match(MODES_RE, chmodes.strip(), re.DOTALL)
        output["chmodes"] = {
            "description": m.group("description"),
            "chars": [
                {
                    "name": row["Name"],
                    "char": row["Character"],
                    "type": row["Type"],
                    "syntax": "None" if row["Parameter Syntax"] == "*None*" else row["Parameter Syntax"],
                    "usable_by": row["Usable By"],
                    "description": md_block(row["Description"]),
                }
                for row in parse_table(m.group("chars"))
            ],
            "example": md_block((m.group("example") or "").strip()),
        }

def parse_umodes(groups, output):
    umodes = groups["umodes"]
    if umodes:
        # copy-pasted from the chmodes above
        m = re.match(MODES_RE, umodes.strip(), re.DOTALL)
        output["umodes"] = {
            "description": m.group("description"),
            "chars": [
                {
                    "name": row["Name"],
                    "char": row["Character"],
                    "type": row["Type"],
                    "syntax": "None" if row["Parameter Syntax"] == "*None*" else row["Parameter Syntax"],
                    "usable_by": row["Usable By"],
                    "description": md_block(row["Description"]),
                }
                for row in parse_table(m.group("chars"))
            ],
            "example": md_block((m.group("example") or "").strip()),
        }

def parse_commands(groups, output):
    if groups["commands"]:
        commands = []
        commands = groups["commands"]
        m = re.match(COMMANDS_RE, commands, re.DOTALL)
        output["commands"] = [
            {
                "name": row["Name"],
                "param_count": row["Parameter Count"],
                "syntax": "None" if row["Syntax"] == "*None*" else row["Syntax"],
                "description": md_block(row["Description"]),
            }
            for row in parse_table(m.group("commands"))
        ]
        if m.group("details"):
            output["command_details"] = md_block((m.group("details") or "").strip())
        if m.group("example"):
            output["example_commands"] = md_block((m.group("example") or "").strip())

def parse_caps(groups, output):
    if groups["caps"]:
        commands = []
        output["client_caps"] = [
            {
                "name": row["Name"],
                "description": md_block(row["Description"]),
            }
            for row in parse_table(groups["caps"])
        ]

def parse_stats(groups, output):
    if groups["stats"]:
        output["stats"] = [
            {
                "char": row["Character"],
                "description": row["Description"],
            }
            for row in parse_table(groups["stats"])
        ]

def parse_snomasks(groups, output):
    if groups["snomasks"]:
        output["snomasks"] = [
            {
                "char": row["Character"],
                "description": row["Description"],
            }
            for row in parse_table(groups["snomasks"])
        ]

def parse_exemptions(groups, output):
    if groups["exemptions"]:
        output["exemptions"] = [
            {
                "name": row["Name"],
                "description": row["Description"],
            }
            for row in parse_table(groups["exemptions"])
        ]

def parse_extbans(groups, output):
    if groups["extbans"]:
        m = re.match(MODES_RE, groups["extbans"].strip(), re.DOTALL)
        output["extbans"] = {
            "description": m.group("description"),
            "chars": [
                {
                    "char": row["Character"],
                    "type": row["Type"],
                    "syntax": row["Ban Syntax"],
                    "description": row["Description"],
                }
                for row in parse_table(m.group("chars"))
            ],
            "example": md_block((m.group("example") or "").strip()),
        }

def parse_special_notes(groups, output):
    if groups["special_notes"]:
        output["special_notes"] = md_block(groups["special_notes"].strip())


if __name__ == "__main__":
    (_, filename) = sys.argv
    main(filename)
