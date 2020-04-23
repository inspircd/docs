---
title: Module Details: sanick (v3)
---

## The "sanick" Module

### Description

This module adds the `/SANICK` command which allows server operators to change the nickname of a user.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sanick">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax                  | Description
------ | --------------- | ----------------------- | -----------
SANICK | 2               | `<old-nick> <new-nick>` | Changes the nickname of &lt;old-nick&gt; to &lt;new-nick&gt;.

#### Example Usage

Changes the nickname of Sadie to Sadie2:

```plaintext
/SANICK Sadie Sadie2
```
