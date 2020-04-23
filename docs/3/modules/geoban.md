---
title: Module Details: geoban (v3)
---

## The "geoban" Module

### Description

This module adds extended ban `G` which matches against two letter country codes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="geoban">
```

This module requires no other configuration.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
G         | Matching | `G:<pattern>` | Matches against the two letter country code for the country that users are connecting from.

#### Example Usage

Bans users connecting from the United States of America:

```plaintext
/MODE #channel +b G:US
```
