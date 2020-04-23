---
title: Module Details: chgident (v3)
---

## The "chgident" Module

### Description

This module adds the `/CHGIDENT` command which allows server operators to change the username (ident) of a user.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="chgident">
```

This module requires no other configuration.

### Commands

Name     | Parameter Count | Syntax                  | Description
-------- | --------------- | ----------------------- | -----------
CHGIDENT | 2               | `<nickname> <username>` | Changes the username (ident) of &lt;nickname&gt; to &lt;username&gt;.

#### Example Usage

Changes the username (ident) of Sadie to wibble:

```plaintext
/CHGIDENT Sadie wibble
```
