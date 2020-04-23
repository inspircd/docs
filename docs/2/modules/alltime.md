---
title: "Module Details: alltime (v2)"
---

{! 2/_support.md !}

## The "alltime" Module

### Description

This module adds the `/ALLTIME` command which allows server operators to see the current UTC time on all of the servers on the network.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_alltime.so">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax | Description
------- | --------------- | ------ | -----------
ALLTIME | 0               | *None* | Causes all servers on the network to respond with the current UTC time on the server.
