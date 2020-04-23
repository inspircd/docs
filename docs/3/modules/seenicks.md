---
title: "Module Details: seenicks (v3)"
---

## The "seenicks" Module

### Description

This module sends a notice to snomasks `n` (local) and `N` (remote) when a user changes their nickname.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="seenicks">
```

This module requires no other configuration.

### Server Notice Masks

Character | Description
--------- | -----------
n         | Notifications about nicknames being changed on the local server.
N         | Notifications about nicknames being changed on a remote server.
