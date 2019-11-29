---
title: Module Details (setname)
---

## The "setname" Module

### Description

This module adds the `/SETNAME` command which allows users to change their real name (gecos).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="setname">
```

#### `<setname>`

The `<setname>` tag defines settings about how the setname module should behave. This tag can only be defined once.

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
notifyopers | Boolean | Yes           | Whether to notify server operators when a user changes their real name.
operonly    | Boolean | No            | Whether the `/SETNAME` command can only be used by server operators.

#### Example Usage

```xml
<setname notifyopers="yes"
         operonly="no">
```

### Commands

Name    | Parameter Count | Syntax       | Description
------- | --------------- | ------------ | -----------
SETNAME | 1               | `<realname>` | Changes the real name (gecos) of the user to &lt;realname&gt;.

#### Example Usage

Changes the real name (gecos) of the user to "Wibble Wobble":

```plaintext
/SETNAME :Wibble Wobble
```
