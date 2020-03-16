---
title: Module Details (servprotect)
---

## The "servprotect" Module

### Description

This module adds user mode `k` (servprotect) which protects services pseudoclients from being kicked, being killed, or having their user modes changed.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="servprotect">
```

This module requires no other configuration.

### User Modes

Name        | Character | Type   | Parameter Syntax | Usable By | Description
----------- | --------- | ------ | ---------------- | --------- | -----------
servprotect | k         | Switch | *None*           | Servers   | Protects services pseudoclients against kicks, kills, and user mode changes.

### Special Notes

This user mode **can not** be set on normal users. It is intended specifically for services pseudoclients.
