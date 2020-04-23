---
title: Module Details: operprefix (v2)
---

{! 2/_support.md !}

## The "operprefix" Module

### Description

This module adds the server operator-only `y` (operprefix) channel prefix mode.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_operprefix.so">
```

#### `<operprefix>`

The `<operprefix>` tag defines settings about how the operprefix module should behave. This tag can only be defined once.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
prefix | Text | !             | The prefix character to use for the `y` (operprefix) channel prefix mode.

##### Example Usage

```xml
<operprefix prefix="!">
```

### Channel Modes

Name       | Character | Type      | Parameter Syntax | Description
---------- | --------- | --------- | ---------------- | -----------
operprefix | y         | Prefix    | `<nick>`         | Grants channel operprefix status to &lt;nick&gt;.

### Special Notes

The `y` (operprefix) channel prefix mode can not be directly set by users. To enable this channel prefix mode log into a server operator account.

If you don't want the `y` (operprefix) channel prefix mode to be active at all times consider using [the ojoin module](/2/modules/ojoin) instead.
