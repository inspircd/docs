---
title: "Module Details: spanningtree (v3)"
---

## The "spanningtree" Module

### Description

This module allows linking multiple servers together as part of one network.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="spanningtree">
```

#### `<autoconnect>`

The `<autoconnect>` tag defines one or more servers to attempt to connect to. This tag can be defined as many times as required.

Name   | Type     | Default Value | Description
------ | -------- | ------------- | -----------
period | Duration | *None*        | The time period to wait between server connection attempts.
server | Text     | *None*        | A space-delimited list of servers to attempt to connect to.

##### Example Usage

Automatically connects to hub1.example.com after 120 seconds, failing over to hub2.example.com and then hub3.example.com if connecting to the previous server fails:

```xml
<autoconnect period="2m"
             server="hub1.example.com hub2.example.com hub3.example.com">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following listener types:

Name    | Description
------- | -----------
servers | Listens for server connections.

##### Example Usage

Listens for TLS encrypted server connections on the *:7002 endpoint with an SSL profile named "Servers":

```xml
<bind address="*"
      port="7003"
      ...
      ssl="Servers"
      type="servers">
```

Listens for unencrypted server connections on the 127.0.0.1:7000 endpoint:

```xml
<bind address="127.0.0.1"
      port="7000"
      ...
      type="servers">
```

#### `<link>`

The `<link>` tag defines a server to link with. This tag can be defined as many times as required.

Name        | Type     | Default Value | Description
----------- | -------- | ------------- | -----------
allowmask   | Text     | *None*        | **Required!** One or more CIDR ranges or glob patterns that the remote server can connect from.
bind        | Text     | *None*        | The IP address to bind to when connecting to the remote server.
fingerprint | Text     | *None*        | If defined then the TLS (SSL) client fingerprint of the remote server.
hidden      | Boolean  | No            | Whether the server IP address is hidden from server operators.
ipaddr      | Text     | *None*        | **Required!** The IP address or hostname of the remote server.
name        | Text     | *None*        | **Required!** The hostname of the IRC server.
port        | Number   | *None*        | If defined then the TCP port to connect to this server on.
recvpass    | Text     | *None*        | **Required!** The password that the remote server will use to log into the local server.
sendpass    | Text     | *None*        | **Required!** The password that the local server will use to log into the remote server.
ssl         | Text     | *None*        | If defined then the name of a TLS (SSL) profile to use for encrypting the connection with this server.
statshidden | Boolean  | No            | Whether the server IP address is hidden in the `/STATS` output.
timeout     | Duration | 30s           | The number of seconds to wait before declaring a server connection as having failed.

##### Example Usage

Automatically connects to hub1.example.com after 120 seconds, failing over to hub2.example.com and then hub3.example.com if connecting to the previous server fails:

```xml
<link allowmask="192.0.2.0/24 198.51.100.*"
      bind="203.0.113.2"
      fingerprint="1fba42fde3c4e76b7cca45764faf5cc1a7c903a77e0f2bc978d990280b15906f"
      hidden="no"
      ipaddr="server-1a4.example.net"
      name="hub.example.com"
      port="7000"
      recvpass="incoming!password"
      sendpass="outgoing!password"
      ssl="Servers"
      timeout="15s">
```

#### `<options>`

This module extends the core `<options>` tag with the following fields:

Name           | Type     | Default Value | Description
-------------- | -------- | ------------- | -----------
allowmismatch  | Boolean  | No            | Whether optionally common modules can be loaded on one server but not the other.
announcets     | Boolean  | No            | Whether to announce changes in channel creation time.
pingwarning    | Duration | 15s           | The number of seconds to wait before warning server operators that a server has not responded to a ping.
serverpingfreq | Duration | 1m            | The number of seconds to wait between pinging servers.

##### Example Usage

```xml
<options ...
         allowmismatch="no"
         announcets="no"
         pingwarning="15"
         serverpingfreq="120">
```

#### `<performance>`

This module extends the core `<performance>` tag with the following fields:

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
quietbursts | Boolean | No            | Whether to inform server operators of users who connect during a network merge.

##### Example Usage

```xml
<performance ...
             quietbursts="yes">
```

#### `<security>`

This module extends the core `<security>` tag with the following fields:

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
flatlinks   | Boolean | No            | Whether to flatten the output of `/LINKS` to avoid leaking network architecture.
hidesplits  | Boolean | No            | Whether to show `*.net *.split` instead of the server names when a netsplit happens
hideulines  | Boolean | No            | Whether to hide U-lined servers from the output of `/LINKS` and `/MAP`.

##### Example Usage

```xml
<security ...
          flatlinks="no"
          hidesplits="no"
          hideulines="no">
```

#### `<uline>`

The `<uline>` tag defines one or more services servers. This tag can be defined as many times as required.

Name   | Type    | Default Value | Description
------ | ------- | ------------- | -----------
server | Text    | *None*        | The name of a services server. You must NOT specify a server that normal users can connect to here.
silent | Boolean | No            | Whether server operators should be informed of users on this server connecting and disconnecting.

##### Example Usage

Marks services.example.com as a silent services server:

```xml
<uline server="services.example.com"
       silent="yes">
```

### Commands

Name     | Parameter Count | Syntax                                      | Description
-------- | --------------- | ------------------------------------------- | -----------
CONNECT  | 1               | `<server>`                                  | Attempts to connect the local server to &lt;server&gt;.
LINKS    | 0               | *None*                                      | Lists all servers connected to the current one.
MAP      | 0               | *None*                                      | Shows a textual map of the network architecture.
RCONNECT | 2               | `<remote-server-mask> <target-server-mask>` | Attempts to connect &lt;remote-server-mask&gt; to &lt;target-server-mask&gt;
RSQUIT   | 2               | `<server-mask> [<reason>]`                  | Attempts to disconnect &lt;server-mask&gt; from the network with &lt;reason&gt;.
SQUIT    | 2               | `<server-mask> [<reason>]`                  | Attempts to disconnect &lt;server-mask&gt; from the local server with &lt;reason&gt;.

#### Example Usage

Connects the local server to hub.example.com:

```plaintext
/CONNECT hub.example.com
```

Connects the remote server eu-hub.example.com to us-hub.example.com:

```plaintext
/RCONNECT eu-hub.example.com us-hub.example.com
```

Disconnects the remote server eu-hub.example.com with no reason:

```plaintext
/RSQUIT eu-hub.example.com
```

Disconnects the remote server us-hub.example.com with the reason "Updating InspIRCd":

```plaintext
/RSQUIT us-hub.example.com :Updating InspIRCd
```

Disconnects the local server eu-hub.example.com with no reason:

```plaintext
/SQUIT eu-hub.example.com
```

Disconnects the local server us-hub.example.com with the reason "Updating InspIRCd":

```plaintext
/SQUIT us-hub.example.com :Updating InspIRCd
```

### Server Notice Masks

Character | Description
--------- | -----------
l         | Messages relating to server linking on the local server.
L         | Messages relating to server linking on a remote server.

### Statistics

Character | Description
--------- | -----------
c         | Lists servers which the server may connect to or allow connections from.
n         | Lists servers which the server may connect to or allow connections from.

### Special Notes

Linking non-local servers without TLS (SSL) is a serious privacy risk and will be removed in the next major version of InspIRCd.
