---
title: Module Details (chancreate)
---

## The "chancreate" Module

### Description

This module sends a notice to snomasks `j` (local) and `J` (remote) when a channel is created.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="chancreate">
```

This module requires no other configuration.

### Server Notice Masks

Character | Description
--------- | -----------
j         | Notifications about channels being created on the local server.
J         | Notifications about channels being created on a remote server.
