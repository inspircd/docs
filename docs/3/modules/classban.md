---
title: Module Details (classban)
---

## The "classban" Module

### Description

This module adds the `n` extended ban which check whether users are in a connect class matching the specified glob pattern.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="classban">
```

This module requires no other configuration.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
n         | Matching | `n:<pattern>` | Checks whether users are in a connect class &lt;pattern&gt;.

#### Example Usage

Bans users in the "webchat" connect class from joining the channel:

```plaintext
/MODE #channel +b n:webchat
```
