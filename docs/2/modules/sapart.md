---
title: "Module Details: sapart (v2)"
---

{! 2/_support.md !}

## The "sapart" Module

### Description

This module adds the `/SAPART` command which allows server operators to force part users from a channel without having any privileges in the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_sapart.so">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax                        | Description
------ | --------------- | ----------------------------- | -----------
SAPART | 2-3             | `<nick> <channel> [<reason>]` | Force parts &lt;nick&gt; from &lt;channel&gt; optionally with the reason specified in &lt;reason&gt;.

#### Example Usage

Force parts emily from #channel:

```plaintext
/SAPART #channel emily :Your behaviour is inappropriate
```
