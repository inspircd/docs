---
title: Module Details (cgiirc)
---

## The "cgiirc" Module

### Description

This module adds the ability for IRC gateways to forward the real IP address of users connecting through them.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="cgiirc">
```

#### `<cgiirc>`

The `<cgiirc>` tag defines settings about how the cgiirc module should behave. This tag can only be defined once.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
opernotice | Boolean | Yes           | Whether to send a notice to snomask `w` (local) and snomask `W` (remote) when a gateway tries to change an IP address.

##### Example Usage

```xml
<cgiirc opernotice="yes">
```

#### `<cgihost>`

The `<cgihost>` tag defines a specific IRC gateway. This tag can be defined as many times as required.

Name        | Type | Default Value | Description
----------- | ---- | ------------- | -----------
fingerprint | Text | *None*        | **Required for the webirc type if password is not set!** The SSL client certificate fingerprint that the WebIRC gateway will authenticate with.
mask        | Text | *None*        | **Required!** The IP address or hostname of the gateway.
newident    | Text | gateway       | If the ident type is used then the value to replace usernames (idents) that contain hexadecimal-encoded IPv4 addresses.
type        | Text | *None*        | **Required!** The type of authentication that the gateway uses.
password    | Text | *None*        | **Required for the webirc type if fingerprint is not set!** The password that the WebIRC gateway will authenticate with.
hash        | Text | *None*        | If the webirc type is used the algorithm that the password is hashed with.

The type field should be set to one of the following values:

Value      | Description
---------- | -----------
ident      | The IP address of the user will be sent in the username (ident) field in hexadecimal (IPv4 only).
webirc     | The IP address of the user will be sent using the `/WEBIRC` command (recommended).

##### Example Usage

Tells the cgiirc module that the \*.ident.gateway.example.com gateway will encode the IPv4 address of users into their username (ident).

```xml
<cgihost type="ident"
         mask="*.ident.gateway.example.com"
         newident="wobble">
```

Tells the cgiirc module that gateways with an IP matching 192.0.2.0/24 will send the IP address of users with the `/WEBIRC` command using SSL client certificate fingerprint authentication:

```xml
<cgihost type="webirc"
         fingerprint="bd90547b59c1942b85f382bc059318f4c6ca54c5"
         mask="192.0.2.0/24">
```

Tells the cgiirc module that gateways with a hostname matching \*.webirc.gateway.example.com will send the IP address of users with the `/WEBIRC` command using password authentication:

```xml
<cgihost type="webirc"
         password="$2a$10$WEUpX9GweJiEF1WxBDSkeODBstIBMlVPweQTG9cKM8/Vd58BeM5cW"
         hash="bcrypt"
         mask="*.webirc.gateway.example.com">
```

### Commands

Name   | Parameter Count  | Syntax                                                | Description
------ | ---------------- | ----------------------------------------------------- | -----------
WEBIRC | 4-5              | `<password> <gateway> <hostname> <address> [<flags>]` | Allows gateways to specify the hostname and IP address of users.

More information about the `/WEBIRC` command is available on [the IRCv3 website](https://ircv3.net/specs/extensions/webirc.html).

<!-- WEBIRC is not documented here because it is not intended to be executed by users -->

### Server Notice Masks

Character | Description
--------- | -----------
w         | Notifications about gateways changing IP addresses on the local server.
W         | Notifications about gateways changing IP addresses on a remote server.

### Special Notes

The `/WEBIRC` command should generally not be executed by users. It is intended to be an entirely internal feature which is executed automatically by gateways.
