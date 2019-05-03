---
title: Module Details (sasl)
---

## The "sasl" Module

### Description

This module provides the IRCv3 `sasl` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sasl">
```

#### `<sasl>`

The `<sasl>` tag defines settings about how the sasl module should behave. This tag can only be defined once.

Name   | Type    | Default Value | Description
------ | ------- | ------------- | -----------
target | Text    | *None*        | **Required!** A glob pattern for the server to route SASL requests to. This should usually be set to the name of your services server.

#### Example Usage

```xml
<sasl target="services.example.com">
```

### Commands

Name         | Parameter Count | Syntax                             | Description
------------ | --------------- | ---------------------------------- | -----------
AUTHENTICATE | 1               | `*`<br>`<mechanism>`<br>`<base64>` | Allows clients to authenticate against a services account.

<!-- AUTHENTICATE is not documented here because it is not intended to be executed by users -->

### Client Capabilities

Name                                                     | Description
-------------------------------------------------------- | -----------
[sasl](https://ircv3.net/specs/extensions/sasl-3.1.html) | Enables support for SASL authentication.

### Special Notes

The `/AUTHENTICATE` command should generally not be executed by users. It is intended to be an entirely internal feature which is executed automatically by clients.