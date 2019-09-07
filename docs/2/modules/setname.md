---
title: Module Details (setname)
---

{! 2/_support.md !}

## The "setname" Module

### Description

This module adds the `/SETNAME` command which allows users to change their real name (gecos).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_setname.so">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax       | Description
------- | --------------- | ------------ | -----------
SETNAME | 1               | `<realname>` | Changes the real name (gecos) of the user to &lt;realname&gt;.

#### Example Usage

Changes the real name (gecos) of the user to "Wibble Wobble":

```plaintext
/SETNAME :Wibble Wobble
```
