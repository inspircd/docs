---
title: Module Details (uninvite)
---

{! 2/_support.md !}

## The "uninvite" Module

### Description

This module adds the `/UNINVITE` command which allows users who have invited another user to a channel to withdraw their invite.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_uninvite.so">
```

This module requires no other configuration.

### Commands

Name     | Parameter Count | Syntax             | Description
-------- | --------------- | ------------------ | -----------
UNINVITE | 1               | `<nick> <channel>` | Withdraws the invite for &lt;nick&gt; to join &lt;channel&gt;

#### Example Usage

Withdraws the invite for Adam to join #secret:

```plaintext
/UNINVITE Adam #secret
```
