---
title: "Module Details: channelban (v2)"
---

{! 2/_support.md !}

## The "channelban" Module

### Description

This module adds the `j` extended ban which checks whether users are in a channel matching the specified glob pattern.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_channelban.so">
```

This module requires no other configuration.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
j         | Matching | `j:<pattern>` | Checks whether users are in a channel matching &lt;pattern&gt;.

#### Example Usage

Bans users in #evil from joining the channel:

```plaintext
/MODE #channel +b j:#evil
```

Bans users that have channel operator status in #evil from joining the channel:

```plaintext
/MODE #channel +b j:@#evil
```
