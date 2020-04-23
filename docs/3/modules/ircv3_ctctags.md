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

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax     | Description
------ | --------------- | ---------- | -----------
TAGMSG | 1               | `<target>` | Sends a message containing only tags to the specified target.

<!-- TAGMSG is not documented here because it is not intended to be executed by users -->

### Client Capabilities

Name                                                                 | Description
-------------------------------------------------------------------- | -----------
[message-tags](https://ircv3.net/specs/extensions/message-tags.html) | Enables support for sending and receiving `TAGMSG` messages.
