<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<bind>`

The `<bind>` tag defines an endpoint to listen for connections on. This tag can be defined as many times as required.

Name    | Type   | Default Value | Description
------- | ------ | ------------- | -----------
address | Text   | *None*        | If defined then the IP address to bind to instead of listening on all available interfaces.
port    | Number | *None*        | **Required!** The TCP port to listen for connections on.
type    | Text   | clients       | The type of connection to be allowed on this endpoint.

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
      type="clients">
```

Listens for IRC server connections on *:7000:

```xml
<bind port="7000"
      type="servers">
```
