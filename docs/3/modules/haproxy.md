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

This module extends [the core `<bind>` tags](/3/configuration#bind) with the following hook types:

Name    | Description
------- | -----------
haproxy | Listens for haproxy connections.

##### Example Usage

Listens for plaintext haproxy connections on the /run/inspircd/haproxy.sock UNIX socket endpoint:

```xml
<bind path="/run/inspircd/haproxy.sock"
      ...
      hook="haproxy">
```

Listens for plaintext haproxy connections on the 127.0.0.1:29583 endpoint:

```xml
<bind address="127.0.0.1"
      port="29583"
      ...
      hook="haproxy">
```

## Special Notes

If you are using this module you must terminate TLS (SSL) connections at your reverse proxy.
