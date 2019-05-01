---
title: Module Details (servprotect)
---

## The "servprotect" Module

### Description

This module adds user mode `k` (servprotect) which protects services pseudoclients from being kicked, being killed, or having their user modes changed.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_servprotect.so">
```

This module requires no other configuration.

### User Modes

Name        | Character | Type   | Parameter Syntax | Description
----------- | --------- | ------ | ---------------- | -----------
servprotect | k         | Switch | *None*           | Protects services pseudoclients against kicks, kills, and user mode changes.

### Special Notes

This channel mode **can not** be set on normal users. It is intended specifically for services pseudoclients.
