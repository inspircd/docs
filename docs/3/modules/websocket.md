---
title: Module Details (websocket)
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

This module extends the core `<bind>` tags with the following hook types:

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

Name       | Type     | Default Value | Description
---------- | -------- | ------------- | -----------
sendastext | Text     | Yes           | Whether to send messages to WebSocket clients using text frames instead of binary frames. This requires all text to be transcoded to UTF-8. 

##### Example Usage

```xml
<websocket sendastest="yes">
```

#### `<wsorigin>`

The `<wsorigin>` tag defines an WebSocket origin that is allowed to connect to the server. This tag can be defined as many times as required.

Name  | Type | Default Value | Description
----- | ---- | ------------- | -----------
allow | Text | *None*        | **Required!** A glob pattern for an URL of a web page that is allowed to connect.

##### Example Usage

Allows access to the server from all subdomains of example.com:

```xml
<wsorigin allow="https://*.example.com/">
```
