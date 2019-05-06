---
title: Module Details (deaf)
---

## The "deaf" Module

### Description

This module adds user mode `d` (deaf) which prevents users from receiving channel messages.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_deaf.so">
```

#### `<deaf>`

The `<deaf>` tag defines settings about how the deaf module should behave. This tag can only be defined once.

Name             | Type | Default Value | Description
---------------- | ---- | ------------- | -----------
bypasschars      | Text | *None*        | A list of characters that a message to a normal user can begin with that exempt it from the deaf mode.
bypasscharsuline | Text | *None*        | A list of characters that a message to a U-lined user can begin with that exempt it from the deaf mode.

##### Example Usage

```xml
<deaf bypasschars="!."
      bypasscharsuline="!.">
```

### User Modes

Name | Character | Type   | Parameter Syntax | Description
---- | --------- | ------ | ---------------- | -----------
deaf | d         | Switch | *None*           | Prevents the user from receiving channel messages.
