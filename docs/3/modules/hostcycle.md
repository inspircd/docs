---
title: Module Details (hostcycle)
---

## The "hostcycle" Module

### Description

This module sends a fake disconnection and reconnection when a user's username (ident) or hostname changes to allow clients to update their internal caches.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="hostcycle">
```

This module requires no other configuration.
