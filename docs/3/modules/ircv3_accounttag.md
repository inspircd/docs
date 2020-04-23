---
title: "Module Details: ircv3_accounttag (v3)"
---

## The "ircv3_accounttag" Module

### Description

This module provides the IRCv3 `account-tag` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3_accounttag">
```

This module requires no other configuration.

### Client Capabilities

Name                                                                   | Description
---------------------------------------------------------------------- | -----------
[account-tag](https://ircv3.net/specs/extensions/account-tag-3.2.html) | Adds an `account` tag with the services account of the sender to all messages.
