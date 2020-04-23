---
title: Module Details: hidechans (v2)
---

{! 2/_support.md !}

## The "hidechans" Module

### Description

This module adds user mode `I` (hidechans) which hides the channels users with it set are in from their `/WHOIS` response.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_hidechans.so">
```

#### `<hidechans>`

The `<hidechans>` tag defines settings about how the hidechans module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
affectsopers | Boolean | No            | Whether server operators are affected by the user mode.

##### Example Usage

```xml
<hidechans affectsopers="no">
```

### User Modes

Name      | Character | Type   | Parameter Syntax | Description
--------- | --------- | ------ | ---------------- | -----------
hidechans | I         | Switch | *None*           | Hides the channels the user is in from their `/WHOIS` response.
