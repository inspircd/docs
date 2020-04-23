---
title: "Module Details: ircv3_chghost (v3)"
---

## The "ircv3_chghost" Module

### Description

This module provides the IRCv3 `chghost` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3_chghost">
```

This module requires no other configuration.

### Client Capabilities

Name                                                           | Description
-------------------------------------------------------------- | -----------
[chghost](https://ircv3.net/specs/extensions/chghost-3.2.html) | Notifies users when the username (ident) or hostname of a user they share a channel with changes.
