---
title: "Module Details: disable (v3)"
---

## The "disable" Module

### Description

This module allows commands, channel modes, and user modes to be disabled.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="disable">
```

#### `<class>`

This module extends the core `<class:privs>` key with the following values:

Name                          | Description
----------------------------- | -----------
servers/use-disabled-commands | Allows server operators to use disabled commands.
servers/use-disabled-modes    | Allows server operators to use disabled modes.

#### Example Usage

Allows server operators with the class named BasicOper to use disabled commands and modes.

```xml
<class name="BasicOper"
       ...
       privs="... servers/use-disabled-commands servers/use-disabled-modes ...">
```

### `<disabled>`

The `<disabled>` tag defines commands and modes which normal users can not change. This tag can only be defined once.

Name            | Type    | Default Value | Description
--------------- | ------- | ------------- | -----------
fakenonexistent | Boolean | No            | Whether to pretend that a disabled command/mode does not exist.
notifyopers     | Boolean | No            | Whether to send a notice to snomask `a` when a user is prevented from using a disabled command or mode.
commands        | Text    | *None*        | A space-delimited list of commands to disable.
chanmodes       | Text    | *None*        | A list of channel modes to disable.
usermodes       | Text    | *None*        | A list of user modes to disable.

##### Example Usage

```xml
<disabled fakenonexistent="no"
          notifyopers="no"
          commands="MODE TOPIC"
          chanmodes="kp"
          usermodes="iw">
```
