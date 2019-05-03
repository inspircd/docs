---
title: Module Details (commonchans)
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

Name            | Character | Type   | Parameter Syntax | Description
--------------- | --------- | ------ | ---------------- | -----------
deaf_commonchan | c         | Switch | *None*           | Requires other users to have a common channel before they can message this user.
