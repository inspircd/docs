---
title: Module Details (sajoin)
---

## The "sajoin" Module

### Description

This module adds the `/SAJOIN` command which allows server operators to force users to join one or more channnels.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_sajoin.so">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax             | Description
------ | --------------- | ------------------ | -----------
SAJOIN | 2               | `<nick> <channel>` | Forces &lt;nick&gt; to join &gt;channel&gt;.

#### Example Usage

Forces Sadie to join #channel:

```plaintext
/SAJOIN Sadie #channel
```
