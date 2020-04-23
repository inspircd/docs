---
title: "Module Details: haproxy (v3)"
---

## The "haproxy" Module

### Description

This module allows IRC connections to be made using reverse proxies that implement the HAProxy PROXY protocol.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="haproxy">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following hook types:

Name    | Description
------- | -----------
haproxy | Listens for haproxy connections.

##### Example Usage

Listens for plaintext haproxy connections on the 0.0.0.0:8080 endpoint:

```xml
<bind address="0.0.0.0"
      port="8080"
      ...
      hook="haproxy">
```

## Special Notes

If you are using this module you must terminate TLS (SSL) connections at your reverse proxy.
