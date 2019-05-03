---
title: Module Details (sakick)
---

## The "sakick" Module

### Description

This module adds the `/SAKICK` command which allows server operators to kick users from a channel without having any privileges in the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sakick">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax                        | Description
------ | --------------- | ----------------------------- | -----------
SAKICK | 2-3             | `<channel> <nick> [<reason>]` | Kicks &lt;nick&gt; from &gt;channel&gt; optionally with the reason specified in &lt;reason&gt;.

#### Example Usage

Kicks emily from #channel:

```plaintext
/SAKICK #channel emily :Your behaviour is inappropriate
```
