---
title: "Module Details: cap (v3)"
---

## The "cap" Module

### Description

This module implements support for [the IRCv3 Client Capability Negotiation extension](https://ircv3.net/specs/core/capability-negotiation.html).

This is used by clients to allow the use of modern IRC features without breaking compatibility with older clients.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="cap">
```

This module requires no other configuration.

### Commands

Name | Parameter Count | Syntax                                                                        | Description
---- | --------------- | ----------------------------------------------------------------------------- | -----------
CAP  | 1-2             | `CLEAR`<br>`END`<br>`LIST`<br>`LS [<version>]`<br>`REQ :[-]<cap>[ [-]<cap>]+` | Allows clients to enable capabilities, disable capabilities, and view the capabilities they have enabled.

<!-- CAP is not documented here because it is not intended to be executed by users -->

### Client Capabilities

Name                | Description
------------------- | -----------
inspircd.org/poison | Rejects any attempt to request it to avoid clients requesting all available capabilities rather than the ones they support.

### Special Notes

The `/CAP` command should generally not be executed by users. It is intended to be an entirely internal feature which is executed automatically by clients. Adding and removing capabilities manually may break your client.
