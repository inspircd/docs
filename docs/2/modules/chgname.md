---
title: "Module Details: chgname (v2)"
---

{! 2/_support.md !}

## The "chgname" Module

### Description

This module adds the `/CHGNAME` command which allows server operators to change the real name (gecos) of a user.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_chgname.so">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax                  | Description
------- | --------------- | ----------------------- | -----------
CHGNAME | 2               | `<nickname> <realname>` | Changes the real name (gecos) of &lt;nickname&gt; to &lt;realname&gt;.

#### Example Usage

Changes the real name (gecos) of Sadie to "Wibble Wobble":

```plaintext
/CHGNAME Sadie :Wibble Wobble
```
