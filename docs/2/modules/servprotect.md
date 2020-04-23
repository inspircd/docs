---
title: "Module Details: servprotect (v2)"
---

{! 2/_support.md !}

## The "servprotect" Module

### Description

This module adds user mode `k` (servprotect) which protects services pseudoclients from being kicked, being killed, or having their channel prefix modes changed.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_servprotect.so">
```

This module requires no other configuration.

### User Modes

Name        | Character | Type   | Parameter Syntax | Description
----------- | --------- | ------ | ---------------- | -----------
servprotect | k         | Switch | *None*           | Protects services pseudoclients against kicks, kills, and channel prefix mode changes.

### Special Notes

This user mode **can not** be set on normal users. It is intended specifically for services pseudoclients.
