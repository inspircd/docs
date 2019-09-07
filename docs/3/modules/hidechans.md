---
title: Module Details (hidechans)
---

## The "hidechans" Module

### Description

This module adds user mode `I` (hidechans) which hides the channels users with it set are in from their `/WHOIS` response.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="hidechans">
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

Name      | Character | Type   | Parameter Syntax | Usable By | Description
--------- | --------- | ------ | ---------------- | --------- | -----------
hidechans | I         | Switch | *None*           | Anyone    | Hides the channels the user is in from their `/WHOIS` response.
