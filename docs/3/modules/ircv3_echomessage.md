---
title: Module Details: ircv3_echomessage (v3)
---

## The "ircv3_echomessage" Module

### Description

This module provides the IRCv3 `echo-message` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3_echomessage">
```

This module requires no other configuration.

### Client Capabilities

Name                                                               | Description
------------------------------------------------------------------ | -----------
[echo-message](https://ircv3.net/specs/core/echo-message-3.2.html) | Echoes `NOTICE`, `PRIVMSG`, and `TAGMSG` messages back to the sender.
