---
title: Module Details (sslmodes)
---

{! 2/_support.md !}

## The "sslmodes" Module

### Description

This module adds channel mode `z` (sslonly) which prevents users who are not connecting using SSL from joining the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_sslmodes.so">
```

This module requires no other configuration.

### Channel Modes

Name    | Character | Type   | Parameter Syntax | Description
------- | --------- | ------ | ---------------- | -----------
sslonly | z         | Switch | *None*           | Prevents users who are not connected using SSL from joining the channel.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
z         | Matching | `z:<pattern>` | Checks whether users have an SSL client certificate with a fingerprint matching &lt;pattern&gt;.

#### Example Usage

Bans users with an SSL client certificate fingerprint of 5d7499e1a3537687a2e875fed60b171508a4d1384351e276c4f961ab80729249:

```plaintext
/MODE #channel +b z:5d7499e1a3537687a2e875fed60b171508a4d1384351e276c4f961ab80729249
```
