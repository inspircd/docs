---
title: Module Details (stripcolor)
---

## The "stripcolor" Module

### Description

This module adds channel mode `S` (stripcolor) which allows channels to strip IRC formatting codes from messages.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_stripcolor.so">
```

This module requires no other configuration.

### Channel Modes

Name       | Character | Type   | Parameter Syntax | Description
---------- | --------- | ------ | ---------------- | -----------
stripcolor | S         | Switch | *None*           | Enables stripping of IRC formatting codes from channel messages.

### User Modes

Name         | Character | Type   | Parameter Syntax | Description
------------ | --------- | ------ | ---------------- | -----------
u_stripcolor | S         | Switch | *None*           | Enables stripping of IRC formatting codes from private messages.

### Exemptions

Name       | Description
---------- | -----------
stripcolor | Allows exempted users to send messages that contain IRC formatting codes.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
S         | Acting | `S:<mask>` | Strips IRC formatting codes from messages sent by users matching &lt;mask&gt;.

#### Example Usage

Strips IRC formatting codes from users matching `*!*@example.com`:

```plaintext
/MODE #channel +b S:*!*@example.com
```
