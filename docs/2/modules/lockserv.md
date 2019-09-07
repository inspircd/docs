---
title: Module Details (lockserv)
---

{! 2/_support.md !}

## The "lockserv" Module

### Description

This module adds the `/LOCKSERV` and `/UNLOCKSERV` commands which allows server operators to control whether users can connect to the local server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_lockserv.so">
```

This module requires no other configuration.

### Commands

Name       | Parameter Count | Syntax | Description
---------- | --------------- | ------ | -----------
LOCKSERV   | 0               | *None* | Disables access to the local server.
UNLOCKSERV | 0               | *None* | Enables access to the local server.

## Special Notes

If you accidentally disconnect whilst a server is locked you can disable the lock by rehashing the server.
