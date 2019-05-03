---
title: Module Details (ircv3_servertime)
---

## The "ircv3_servertime" Module

### Description

This module provides the IRCv3 `server-time` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3_servertime">
```

This module requires no other configuration.

### Client Capabilities

Name                                                                   | Description
---------------------------------------------------------------------- | -----------
[server-time](https://ircv3.net/specs/extensions/server-time-3.2.html) | Adds an `time` tag with the time the message was sent to all messages.
