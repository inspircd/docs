---
title: Module Details (sslrehashsignal)
---

## The "sslrehashsignal" Module

### Description

This module allows the `SIGUSR1` signal to be sent to the server to reload SSL certificates.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sslrehashsignal">
```

This module requires no other configuration.

### Signals

Name    | Description
------- | -----------
SIGUSR1 | Reloads the server's SSL certificates.
