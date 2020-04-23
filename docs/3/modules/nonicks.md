---
title: "Module Details: nonicks (v3)"
---

## The "nonicks" Module

### Description

This module adds channel mode `N` (nonick) which prevents users from changing their nickname whilst in the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="nonicks">
```

This module requires no other configuration.

### Channel Modes

Name   | Character | Type   | Parameter Syntax | Usable By         | Description
------ | --------- | ------ | ---------------- | ----------------- | -----------
nonick | N         | Switch | *None*           | Channel operators | Prevents users from changing their nickname whilst in the channel.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
N         | Acting | `N:<mask>` | Bans privileged users matching &lt;mask&gt; from changing their nickname whilst in the channel.

#### Example Usage

Bans privileged users matching `*!*@example.com` from changing their nickname whilst in the channel.

```plaintext
/MODE #channel +b N:*!*@example.com
```
