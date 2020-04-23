---
title: Module Details: botmode (v3)
---

## The "botmode" Module

### Description

This module adds user mode `B` (bot) which marks users with it set as bots in their `/WHOIS` response.

Depending on your module-specific configuration this can also prevents a bot from using non-bot aliases (requires [the alias module](/3/modules/alias)) and from receiving channel history on join (requires [the chanhistory module](/3/modules/chanhistory)).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="botmode">
```

This module requires no other configuration.

### User Modes

Name | Character | Type   | Parameter Syntax | Usable By | Description
---- | --------- | ------ | ---------------- | --------- | -----------
bot  | B         | Switch | *None*           | Anyone    | Marks the user as a bot.
