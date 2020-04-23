---
title: "Module Details: setident (v2)"
---

{! 2/_support.md !}

## The "setident" Module

### Description

This module adds the `/SETIDENT` command which allows server operators to change their username (ident).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_setident.so">
```

This module requires no other configuration.

### Commands

Name     | Parameter Count | Syntax       | Description
-------- | --------------- | ------------ | -----------
SETIDENT | 1               | `<username>` | Changes the username (ident) of the user to &lt;username&gt;.

#### Example Usage

Changes the username (ident) of the user to wibble:

```plaintext
/SETIDENT wibble
```
