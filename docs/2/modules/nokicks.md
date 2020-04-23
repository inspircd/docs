---
title: Module Details: nokicks (v2)
---

{! 2/_support.md !}

## The "nokicks" Module

### Description

This module adds channel mode `Q` (nokick) which prevents privileged users from using the `/KICK` command.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_nokicks.so">
```

This module requires no other configuration.

### Channel Modes

Name   | Character | Type   | Parameter Syntax | Description
------ | --------- | ------ | ---------------- | -----------
nokick | Q         | Switch | *None*           | Prevents privileged users from using the `/KICK` command.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
Q         | Acting | `Q:<mask>` | Bans privileged users matching &lt;mask&gt; from using the `/KICK` command.

#### Example Usage

Bans privileged users matching `*!*@example.com` from using the `/KICK` command:

```plaintext
/MODE #channel +b Q:*!*@example.com
```

### Special Notes

You should consider using [the mlock module](/2/modules/mlock) and the mode locking feature of your IRC services to prevent privileged users from evading this mode by unsetting it.
