---
title: Module Details (botmode)
---

{! 2/_support.md !}

## The "botmode" Module

### Description

This module adds user mode `B` (bot) which marks users with it set as bots in their `/WHOIS` response.

Depending on your module-specific configuration this can also prevents a bot from using non-bot aliases (requires [the alias module](/2/modules/alias)) and from receiving channel history on join (requires [the chanhistory module](/2/modules/chanhistory)).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_botmode.so">
```

This module requires no other configuration.

### User Modes

Name | Character | Type   | Parameter Syntax | Description
---- | --------- | ------ | ---------------- | -----------
bot  | B         | Switch | *None*           | Marks the user as a bot.
