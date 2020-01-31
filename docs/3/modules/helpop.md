---
title: Module Details (helpop)
---

## The "helpop" Module

### Description

This module adds the `/HELPOP` command which allows users to view help on various topics and user mode `h` (helpop) which marks a server operator as being available for help.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="helpop">
```

#### `<helpmsg>`

The `<helpmsg>` tag defines responses to the /HELPOP command. This tag can only be defined once.

Name   | Type | Default Value                                                      | Description
------ | ---- | ------------------------------------------------------------------ | -----------
nohelp | Text | There is no help for the topic you searched for. Please try again. | The message to respond with when a help topic does not exist.

##### Example Usage

```xml
<helpmsg nohelp="There is no help for the topic you searched for. Please try again.">
```

#### `<helpop>`

The `<helpop>` tag defines a help topic. This tag can be defined as many times as required.

Name  | Type | Default Value                 | Description
----- | ---- | ----------------------------- | -----------
key   | Text | *None*                        | The name of this help topic.
title | Text | *None*                        | [**New in v3.5.0!**](/3/change-log/#inspircd-350) The header for the help topic.
value | Text | *None*                        | The contents of this help topic. This can be split over multiple lines if needed.

##### Example Usage

```xml
<helpop key="test"
        title="Testing?"
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

Name   | Character | Type   | Parameter Syntax | Usable By        | Description
------ | --------- | ------ | ---------------- | ---------------- | -----------
helpop | h         | Switch | *None*           | Server operators | Marks the user as being available for help.

### Special Notes

You may find it useful to use the predefined help file which ships with InspIRCd.

To use this add the following tag to your configuration:

```xml
<include file="examples/helpop.conf.example">
```
