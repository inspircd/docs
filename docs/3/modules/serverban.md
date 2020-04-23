---
title: "Module Details: serverban (v3)"
---

## The "serverban" Module

### Description

This module adds the `s` extended ban which check whether users are on a server matching the specified glob pattern.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="serverban">
```

This module requires no other configuration.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
s         | Matching | `s:<pattern>` | Checks whether users are on a server matching &lt;pattern&gt;.

#### Example Usage

Bans users on irc2.example.com from joining the channel:

```plaintext
/MODE #channel +b s:irc2.example.com
```
