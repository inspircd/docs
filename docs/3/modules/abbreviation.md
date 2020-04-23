---
title: "Module Details: abbreviation (v3)"
---

## The "abbreviation" Module

### Description

This module allows commands to be abbreviated by appending a full stop. For example, executing `/PRIV. #test Hello!` would expand to `/PRIVMSG #test Hello!`.

If more than one command matches the specified abbreviation the server will respond with a list of commands that the abbreviation could possibly match.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="abbreviation">
```

This module requires no other configuration.

### Special Notes

This module will not allow you to abbreviate aliases added by [the alias module](/3/modules/alias) as aliases are not real commands. If you wish to shorten an alias you should add a short form version of that alias.
