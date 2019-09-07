---
title: Module Details (nopartmsg)
---

{! 2/_support.md !}

## The "nopartmsg" Module

### Description

This module adds the `p` extended ban which blocks the part message of matching users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_nopartmsg.so">
```

This module requires no other configuration.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
p         | Acting | `p:<mask>` | Bans &lt;mask&gt; from sending a `/PART` message.

#### Example Usage

Bans users matching `*!*@example.com` from sending a `/PART` message:

```plaintext
/MODE #channel +b p:*!*@example.com
```
