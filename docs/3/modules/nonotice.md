---
title: Module Details (nonotice)
---

## The "nonotice" Module

### Description

This module adds channel mode `T` (nonotice) which allows channels to block messages sent with the `/NOTICE` command.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="nonotice">
```

This module requires no other configuration.

### Channel Modes

Name     | Character | Type   | Parameter Syntax | Description
-------- | --------- | ------ | ---------------- | -----------
nonotice | T         | Switch | *None*           | Enables blocking messages sent with the `/NOTICE` command.

### Exemptions

Name     | Description
-------- | -----------
nonotice | Allows exempted users to send messages with the `/NOTICE` command.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
T         | Acting | `T:<mask>` | Bans &lt;mask&gt; from sending messages with the `/NOTICE` command.

#### Example Usage

Bans users matching `*!*@example.com` from sending messages with the `/NOTICE` command:

```plaintext
/MODE #channel +b T:*!*@example.com
```
