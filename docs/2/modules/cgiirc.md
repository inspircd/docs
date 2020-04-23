---
title: "Module Details: cgiirc (v2)"
---

{! 2/_support.md !}

## The "cgiirc" Module

### Description

This module adds the ability for IRC gateways to forward the real IP address of users connecting through them.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_cgiirc.so">
```

#### `<cgiirc>`

The `<cgiirc>` tag defines settings about how the cgiirc module should behave. This tag can only be defined once.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
opernotice | Boolean | Yes           | Whether to send a notice to snomask `a` (local) and snomask `A` (remote) when a users IP address changes.

##### Example Usage

```xml
<cgiirc opernotice="yes">
```

#### `<cgihost>`

The `<cgihost>` tag defines a specific IRC gateway. This tag can be defined as many times as required.

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
mask     | Text | *None*        | **Required!** The IP address or hostname of the gateway.
type     | Text | *None*        | **Required!** The type of authentication that the gateway uses.
password | Text | *None*        | **Required for the webirc type!** The password that the WebIRC gateway will authenticate with.

The type field should be set to one of the following values:

Value      | Description
---------- | -----------
ident      | The IP address of the user will be sent in the username (ident) field in hexadecimal (IPv4 only).
pass       | *Deprecated!* The IP address of the user will be sent with the `/PASS` command field in hexadecimal (IPv4 only).
identfirst | *Deprecated!* The ident method will be tried and if that does not work the pass method will be tried.
passfirst  | *Deprecated!* The pass method will be tried and if that does not work the ident method will be tried.
webirc     | The IP address of the user will be sent using the `/WEBIRC` command (recommended).

##### Example Usage

Tells the cgiirc module that the "irc.example.com" gateway will encode the IPv4 address of users into their username (ident).

```xml
<cgihost type="ident"
         mask="irc.example.com">
```

Tells the cgiirc module that gateways in the "192.2/24" CIDR range will send the IPv4 address of users with the `/PASS` command.

```xml
<cgihost type="pass"
         mask="192.2/24">
```

Tells the cgiirc module that gateways with an IP matching "198.51.100.*" will send the IP address of users with the `/WEBIRC` command.

```xml
<cgihost type="webirc"
         mask="198.51.100.*"
         password="secret">
```

### Commands

Name   | Parameter Count | Syntax                                      | Description
------ | --------------- | ------------------------------------------- | -----------
WEBIRC | 4               | `<password> <gateway> <hostname> <address>` | Allows gateways to specify the hostname and IP address of users.

More information about the `/WEBIRC` command is available on [the IRCv3 website](https://ircv3.net/specs/extensions/webirc.html).

<!-- WEBIRC is not documented here because it is not intended to be executed by users -->

### Special Notes

The `/WEBIRC` command should generally not be executed by users. It is intended to be an entirely internal feature which is executed automatically by gateways.
