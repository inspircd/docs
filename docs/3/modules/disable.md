---
title: Module Details (disable)
---

## The "disable" Module

### Description

This module allows commands, channel modes, and user modes to be disabled.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="disable">
```

This module requires no other configuration.

### `<disabled>`

The `<disabled>` tag defines commands and modes which normal users can not change. This tag can only be defined once.

Name            | Type    | Default Value | Description
--------------- | ------- | ------------- | -----------
fakenonexistent | Boolean | No            | Whether to pretend that a disabled command/mode does not exist.
commands        | Text    | *None*        | A space-delimited list of commands to disable.
chanmodes       | Text    | *None*        | A list of channel modes to disable.
usermodes       | Text    | *None*        | A list of user modes to disable.

##### Example Usage

```xml
<disabled fakenonexistent="no"
          commands="MODE TOPIC"
          chanmodes="kp"
          usermodes="iw">
```
