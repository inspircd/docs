---
title: "Module Details: close (v2)"
---

{! 2/_support.md !}

## The "close" Module

!!! warning ""
    This module has been moved to [inspircd-contrib](/2/module-manager) in the next major version of InspIRCd.

### Description

This module adds the `/CLOSE` command which allows server operators to disconnect all users who have not fully connected to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_close.so">
```

This module requires no other configuration.

### Commands

Name  | Parameter Count | Syntax | Description
----- | --------------- | ------ | -----------
CLOSE | 0               | *None* | Disconnects all users who have not fully connected to the server.
