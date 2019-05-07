---
title: Module Details (noctcp)
---

## The "noctcp" Module

### Description

This module adds channel mode `C` (noctcp) which allows channels to block messages which contain CTCPs.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="noctcp">
```

This module requires no other configuration.

### Channel Modes

Name   | Character | Type   | Parameter Syntax | Description
------ | --------- | ------ | ---------------- | -----------
noctcp | C         | Switch | *None*           | Enables blocking messages that contain CTCPs.

### Exemptions

Name   | Description
------ | -----------
noctcp | Allows exempted users to send messages that contain CTCPs.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
C         | Acting | `C:<mask>` | Bans &lt;mask&gt; from sending messages that contain CTCPs.

#### Example Usage

Bans users matching `*!*@example.com` from sending messages that contain CTCPs:

```plaintext
/MODE #channel +b C:*!*@example.com
```

### Special Notes

Actions (i.e. /ME) use a CTCP internally but are not blocked by this module.
