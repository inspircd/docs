---
title: Module Details (saquit)
---

## The "saquit" Module

### Description

This module adds the `/SAQUIT` command which allows server operators to disconnect users from the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_saquit.so">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax            | Description
------ | --------------- | ----------------- | -----------
SAQUIT | 2               | `<nick> <reason>` | Disconnects &lt;nick&gt; from the server with the reason specified in &lt;reason&gt;.

#### Example Usage

Disconnects emily from the server:

```plaintext
/SAQUIT emily :Quitting
```
