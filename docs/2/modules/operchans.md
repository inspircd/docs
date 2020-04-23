---
title: Module Details: operchans (v2)
---

{! 2/_support.md !}

## The "operchans" Module

### Description

This module adds channel mode `O` (operonly) which prevents non-server operators from joining the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_operchans.so">
```

This module requires no other configuration.

### Channel Modes

Name     | Character | Type   | Parameter Syntax | Description
-------- | --------- | ------ | ---------------- | -----------
operonly | O         | Switch | *None*           | Prevents non-server operators from joining the channel.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
O         | Matching | `O:<pattern>` | Checks whether users are logged into a server operator account matching &lt;pattern&gt;.

#### Example Usage

Bans users logged into server operator accounts matching `Evil*` from joining the channel:

```plaintext
/MODE #channel +b O:Evil*
```
