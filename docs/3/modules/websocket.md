---
title: "Module Details: websocket (v3)"
---

## The "websocket" Module

### Description

This module allows WebSocket clients to connect to the IRC server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="websocket">
```

#### `<bind>`

This module extends [the core `<bind>` tags](/3/configuration#bind) with the following hook types:

Name      | Description
--------- | -----------
websocket | Listens for WebSocket connections.

##### Example Usage

Listens for plaintext WebSocket connections on the 0.0.0.0:8080 endpoint:

```xml
<bind address="0.0.0.0"
      port="8080"
      ...
      hook="websocket">
```

#### `<websocket>`

The `<websocket>` tag defines settings about how the websocket module should behave. This tag can only be defined once.

Name        | Type     | Default Value | Description
----------- | -------- | ------------- | -----------
proxyranges | Text     | *None*        | [**New in v3.5.0!**](/3/change-log/#inspircd-350) A space-delimited list of glob or CIDR matches to trust the X-Real-IP or X-Forwarded-For headers from.
sendastext  | Text     | Yes           | Whether to send messages to WebSocket clients using text frames instead of binary frames. This requires all text to be transcoded to UTF-8.

##### Example Usage

```xml
<websocket proxyranges="192.0.2.0/24 198.51.100.*"
           sendastext="yes">
```

#### `<wsorigin>`

The `<wsorigin>` tag defines an WebSocket origin that is allowed to connect to the server. This tag can be defined as many times as required.

Name  | Type | Default Value | Description
----- | ---- | ------------- | -----------
allow | Text | *None*        | **Required!** A glob pattern for an URL of a web page that is allowed to connect.

##### Example Usage

Allows access to the server from all subdomains of example.com:

```xml
<wsorigin allow="https://*.example.com">
```

### Special Notes

The following HTTP errors are sent by this module:

 - HTTP 400 &mdash; Your WebSocket implementation has not sent the required `Origin` header.
 - HTTP 403 &mdash; You are attempting to connect from a non-whitelisted origin.
 - HTTP 501 &mdash; Your WebSocket implementation has not sent the required `Sec-WebSocket-Key` header.
 - HTTP 503 &mdash; You do not have [the sha1 module](/3/modules/sha1) loaded.

If you add an encrypted WebSocket listener you should create a custom SSL profile that has `requestclientcert="no"` set. This is required to allow connections to your server using Google Chrome.

Some reverse proxy providers (e.g. Cloudflare) drop idle WebSocket connections which can cause problems with this module. It is recommended that you avoid these providers.
