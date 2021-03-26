---
title: "Module Details: sslrehashsignal (v3)"
---

## The "sslrehashsignal" Module

!!! note ""
    This module depends on UNIX-specific features and must be manually enabled at compile time.

    If you are building on a UNIX platform you can enable this module using the following command:

    <pre><code>./configure --enable-extras sslrehashsignal</code></pre>

### Description

This module allows the `SIGUSR1` signal to be sent to the server to reload TLS (SSL) certificates.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sslrehashsignal">
```

This module requires no other configuration.

### Signals

Name    | Description
------- | -----------
SIGUSR1 | Reloads the server's TLS (SSL) certificates.
