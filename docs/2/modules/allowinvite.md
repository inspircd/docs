---
title: "Module Details: allowinvite (v2)"
---

{! 2/_support.md !}

## The "allowinvite" Module

### Description

This module adds channel mode `A` (allowinvite) which allows unprivileged users to use the `/INVITE` command and extended ban `A` which bans specific masks from using the `/INVITE` command.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_allowinvite.so">
```

This module requires no other configuration.

### Channel Modes

Name        | Character | Type   | Parameter Syntax | Description
----------- | --------- | ------ | ---------------- | -----------
allowinvite | A         | Switch | *None*           | Allows unprivileged users to use the `/INVITE` command.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
A         | Acting | `A:<mask>` | Bans &lt;mask&gt; from using the `/INVITE` command.

#### Example Usage

Bans users matching `*!*@example.com` from using the `/INVITE` command:

```plaintext
/MODE #channel +b A:*!*@example.com
```
