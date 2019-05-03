---
title: Module Details (deaf)
---

## The "deaf" Module

### Description

This module adds user mode `d` (deaf) which prevents users from receiving channel messages.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="deaf">
```

#### `<deaf>`

The `<deaf>` tag defines settings about how the deaf module should behave. This tag can only be defined once.

Name             | Type    | Default Value | Description
---------------- | ------- | ------------- | -----------
bypasschars      | Text    | *None*        | A list of characters that a message to a normal user can begin with that exempt it from the deaf mode.
bypasscharsuline | Text    | *None*        | A list of characters that a message to a ulined user can begin with that exempt it from the deaf mode.
enableprivdeaf   | Boolean | No            | Whether user mode `D` (privdeaf) is enabled
privdeafuline    | Boolean | Yes           | Whether users on U-lined servers are exempt from user mode `D` (privdeaf).

##### Example Usage

```xml
<deaf bypasschars="!."
      bypasscharsuline="!."
      enableprivdeaf="yes"
      privdeafuline="yes">
```

### User Modes

Name     | Character | Type   | Parameter Syntax | Description
-------- | --------- | ------ | ---------------- | -----------
deaf     | d         | Switch | *None*           | Prevents the user from receiving channel messages.
privdeaf | D         | Switch | *None*           | Prevents the user from receiving private messages.

### Special Notes

If you want to link against InspIRCd v2 servers you must not enable user mode `D` (privdeaf).
