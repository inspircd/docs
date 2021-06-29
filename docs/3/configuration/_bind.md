<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<bind>`

The `<bind>` tag defines an endpoint to listen for connections on. This tag can be defined as many times as required.

Name        | Type     | Default Value | Description
----------- | -------- | ------------- | -----------
address     | Text     | *None*        | *TCP/IP listeners only!* If defined then the IP address to bind to instead of listening on all available interfaces.
port        | Number   | *None*        | **Required for TCP/IP listeners!** The TCP port to listen for connections on.
defer       | Duration | 0             | *TCP/IP listeners only!* The number of seconds to defer a connection for whilst waiting for it to send data (not supported on Windows).
hook        | Text     | *None*        | If defined then the name of a module that provides middleware for this listener.
free        | Boolean  | No            | *TCP/IP listeners only!* Whether to allow binding on TCP/IP endpoints which may not be usable yet (not supported on Windows).
path        | Text     | *None*        | **Required for UNIX listeners!** The UNIX socket endpoint to listen for connections on (not supported on Windows).
permissions | Number   | *None*        | *UNIX listeners only!* The permissions to use for the UNIX socket (only supported on Linux).
replace     | Boolean  | No            | *UNIX listeners only!* Whether to replace the UNIX socket file if it already exists (not supported on Windows).
type        | Text     | clients       | The type of connection to be allowed on this endpoint.

If defined the hook field should be set to one of the following values:

Value     | Module                            | Description
--------- | --------------------------------- | -----------
haproxy   | [haproxy](/3/modules/haproxy)     | Listens for connections that use the HAProxy Proxy protocol.
websocket | [websocket](/3/modules/websocket) | Listens for connections that use WebSocket framing.

The type field should be set to one of the following values:

Value        | Module                                  | Description
------------ | --------------------------------------- | -----------
clients      | *None*                                  | Listens for IRC client connections.
flashpolicyd | [flashpolicyd](/3/modules/flashpolicyd) | Listens for Adobe Flash policy connections.
httpd        | [httpd](/3/modules/httpd)               | Listens for HTTP connections.
servers      | [spanningtree](/3/modules/spanningtree) | Listens for IRC server connections.

#### Example Usage

Listens for IRC client connections on 192.0.2.1:6667:

```xml
<bind address="192.0.2.1"
      port="6667"
      type="clients"
      defer="0s"
      free="no">
```

Listens for IRC server connections on *:7000:

```xml
<bind port="7000"
      type="servers"
      defer="5s"
      free="no">
```

Listens for IRC client connections on `/run/inspircd.sock`

```xml
<bind path="/run/inspircd.sock"
      type="clients"
      permissions="750"
      replace="yes">
```
