---
title: "Module Details: gecosban (v2)"
---

{! 2/_support.md !}

## The "gecosban" Module

### Description

This module adds the `r:` extended ban which checks whether users have a real name (gecos) matching the specified glob pattern.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_gecosban.so">
```

This module requires no other configuration.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
r         | Matching | `r:<pattern>` | Checks whether users have a a real name (gecos) matching &lt;pattern&gt;.

#### Example Usage

Bans users with a real name (gecos) matching `*example*` from joining the channel:

```plaintext
/MODE #channel +b r:*example*
```
