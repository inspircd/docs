---
title: Module Details: timedbans (v3)
---

## The "timedbans" Module

### Description

This module adds the `/TBAN` command which allows channel operators to add bans which will be expired after the specified period.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="timedbans">
```

This module requires no other configuration.

### Commands

Name | Parameter Count | Syntax                           | Description
---- | --------------- | -------------------------------- | -----------
TBAN | 3               | `<channel> <duration> <banmask>` | Bans &lt;banmask&lt; from &lt;channel&gt; for &lt;duration&gt;.

#### Example Usage

Bans `*!*@example.com` from #channel for one hour:

```plaintext
/TBAN #channel 1h *!*@example.com
```
