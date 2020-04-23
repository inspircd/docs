---
title: "Module Details: blockcolor (v2)"
---

{! 2/_support.md !}

## The "blockcolor" Module

### Description

This module adds channel mode `c` (blockcolor) which allows channels to block messages which contain IRC formatting codes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_blockcolor.so">
```

This module requires no other configuration.

### Channel Modes

Name       | Character | Type   | Parameter Syntax | Description
---------- | --------- | ------ | ---------------- | -----------
blockcolor | c         | Switch | *None*           | Enables blocking messages that contain IRC formatting codes.

### Exemptions

Name       | Description
---------- | -----------
blockcolor | Allows exempted users to send messages that contain IRC formatting codes.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
c         | Acting | `c:<mask>` | Bans &lt;mask&gt; from sending messages that contain IRC formatting codes.

#### Example Usage

Bans users matching `*!*@example.com` from sending messages that contain IRC formatting codes:

```plaintext
/MODE #channel +b c:*!*@example.com
```

