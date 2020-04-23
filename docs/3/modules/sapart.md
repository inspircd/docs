---
title: Module Details: sapart (v3)
---

## The "sapart" Module

### Description

This module adds the `/SAPART` command which allows server operators to force part users from one or more channels without having any privileges in these channels.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sapart">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax                                     | Description
------ | --------------- | ------------------------------------------ | -----------
SAPART | 2-3             | `<nick> <channel>[,<channel>]+ [<reason>]` | Force parts &lt;nick&gt; from &lt;channel&gt; optionally with the reason specified in &lt;reason&gt;.

#### Example Usage

Force parts emily from #channel:

```plaintext
/SAPART #channel emily :Your behaviour is inappropriate
```
