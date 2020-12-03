---
title: "Module Details: ircv3_ctctags (v3)"
---

## The "ircv3_ctctags" Module

### Description

This module provides the IRCv3 `message-tags` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3_ctctags">
```

#### `<ctctags>`

The `<ctctags>` tag defines settings about how the ircv3_ctctags module should behave. This tag can only be defined once.

Name                | Type    | Default Value | Description
------------------- | ------- | ------------- | -----------
allowclientonlytags | Boolean | Yes           | [**New in v3.7.0!**](/3/change-log/#inspircd-370) Whether to allow clients to send client-to-client tags.

##### Example Usage

```xml
<ctctags allowclientonlytags="yes">
```

### Commands

Name   | Parameter Count | Syntax     | Description
------ | --------------- | ---------- | -----------
TAGMSG | 1               | `<target>` | Sends a message containing only tags to the specified target.

<!-- TAGMSG is not documented here because it is not intended to be executed by users -->

### Client Capabilities

Name                                                                 | Description
-------------------------------------------------------------------- | -----------
[message-tags](https://ircv3.net/specs/extensions/message-tags.html) | Enables support for sending and receiving `TAGMSG` messages.
