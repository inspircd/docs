---
title: Module Details (ojoin)
---

## The "ojoin" Module

### Description

This module adds the `/OJOIN` command which allows server operators to join a channel and receive the server operator-only `Y` (official-join) channel prefix mode.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_ojoin.so">
```

#### `<ojoin>`

The `<ojoin>` tag defines settings about how the ojoin module should behave. This tag can only be defined once.

Name   | Type    | Default Value | Description
------ | ------- | ------------- | -----------
notice | Boolean | Yes           | Whether to inform channel members that a server operator is joining on official network business.
op     | Boolean | Yes           | Whether to also give joining server operators the `o` (op) channel prefix mode.
prefix | Text    | *None*        | If defined then the prefix character to use for the `Y` (official-join) channel prefix mode.

##### Example Usage

```xml
<ojoin notice="yes"
       op="yes"
       prefix="!">
```

### Commands

Name  | Parameter Count | Syntax      | Description
----- | --------------- | ----------- | -----------
OJOIN | 1               | `<channel>` | Joins &lt;channel&gt; with the server operator-only `Y` (official-join) channel prefix mode.

#### Example Usage

Joins #example with the server operator-only `Y` (official-join) channel prefix mode:

```plaintext
/JOIN #example
```

### Channel Modes

Name          | Character | Type      | Parameter Syntax | Description
------------- | --------- | --------- | ---------------- | -----------
official-join | Y         | Prefix    | `<nick>`         | Grants channel official-join status to &lt;nick&gt;.

### Special Notes

The `Y` (official-join) channel prefix mode can not be directly set by users. To enable this channel prefix mode log into a server operator account and use the `/OJOIN` command.

If you want the `Y` (official-join) channel prefix mode to be active at all times consider using [the operprefix module](/2/modules/operprefix) instead.
