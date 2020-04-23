---
title: Module Details: helpop (v2)
---

{! 2/_support.md !}

## The "helpop" Module

### Description

This module adds the `/HELPOP` command which allows users to view help on various topics and user mode `h` (helpop) which marks a server operator as being available for help.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_helpop.so">
```

#### `<helpop>`

The `<helpop>` tag defines a help topic. This tag can be defined as many times as required.

Name  | Type | Default Value                 | Description
----- | ---- | ----------------------------- | -----------
key   | Text | *None*                        | The name of this help topic.
value | Text | *None*                        | The contents of this help topic. This can be split over multiple lines if needed.

##### Example Usage

```xml
<helpop key="test"
        value="This is a test!">
```

### Commands

Name   | Parameter Count | Syntax      | Description
------ | --------------- | ----------- | -----------
HELPOP | 0-1             | `[<topic>]` | Looks up help on a particular topic.

#### Example Usage

Responds with the help introduction page:

```plaintext
/HELPOP
```

Responds with a list of all potential help topics:

```plaintext
/HELPOP index
```

Responds with the contents of the "example" help topic:

```plaintext
/HELPOP example
```

### User Modes

Name   | Character | Type   | Parameter Syntax | Description
------ | --------- | ------ | ---------------- | -----------
helpop | h         | Switch | *None*           | Marks the user as being available for help.

### Special Notes

You may find it useful to use one of the predefined help files which ship with InspIRCd.

For basic help add the following tag to your configuration:

```xml
<include file="conf/examples/helpop.conf.example">
```

For full help add the following tag to your configuration:

```xml
<include file="conf/examples/helpop-full.conf.example">
```
