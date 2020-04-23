---
title: "Module Details: svshold (v3)"
---

## The "svshold" Module

### Description

This module adds the `/SVSHOLD` command which allows services to reserve nicknames. This is identical to a Q-line other than it can only be modified by a network service.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="svshold">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax                               | Description
------- | --------------- | ------------------------------------ | -----------
SVSHOLD | 1-3             | `<nickname> [<duration> [<reason>]]` | Allows services to add and remove nickname reservations.

<!-- SVSHOLD is not documented here because it is not intended to be executed by users -->

### Statistics

Character | Description
--------- | -----------
S         | Lists all nickname reservations.

### Special Notes

SVSHOLDs are expired lazily when a lookup happens for performance reasons. This means that expiry messages may display later than expected.
