---
title: Module Details: commonchans (v3)
---

## The "commonchans" Module

### Description

This module adds user mode `c` (deaf_commonchan) which requires users to have a common channel before they can privately message each other.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="commonchans">
```

This module requires no other configuration.

### User Modes

Name            | Character | Type   | Parameter Syntax | Usable By | Description
--------------- | --------- | ------ | ---------------- | --------- | -----------
deaf_commonchan | c         | Switch | *None*           | Anyone    | Requires other users to have a common channel before they can message this user.
