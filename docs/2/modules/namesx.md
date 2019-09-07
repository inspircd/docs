---
title: Module Details (namesx)
---

{! 2/_support.md !}

## The "namesx" Module

### Description

This module provides the IRCv3 `multi-prefix` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_namesx.so">
```

This module requires no other configuration.

### Client Capabilities

Name                                                                     | Description
------------------------------------------------------------------------ | -----------
[multi-prefix](https://ircv3.net/specs/extensions/multi-prefix-3.1.html) | Causes responses to the `/NAMES` and `/WHO` commands to contain all prefix modes set on users.

### Special Notes

The behaviour of this module can also be enabled using the legacy `/PROTOCTL NAMESX` command. This only exists for compatibility with older clients and will be removed in a future release.
