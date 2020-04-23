---
title: "Module Details: uhnames (v3)"
---

## The "uhnames" Module

### Description

This module provides the IRCv3 `userhost-in-names` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="uhnames">
```

This module requires no other configuration.

### Client Capabilities

Name                                                                               | Description
---------------------------------------------------------------------------------- | -----------
[userhost-in-names](https://ircv3.net/specs/extensions/userhost-in-names-3.2.html) | Causes responses to the `/NAMES` command to contain the full nick!user@host mask of returned users.

### Special Notes

The behaviour of this module can also be enabled using the legacy `/PROTOCTL UHNAMES` command. This only exists for compatibility with older clients and will be removed in a future release.
