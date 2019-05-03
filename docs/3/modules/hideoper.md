---
title: Module Details (hideoper)
---

## The "hideoper" Module

### Description

This module adds user mode `H` (hideoper) which hides the server operator status of a user from unprivileged users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="hideoper">
```

This module requires no other configuration.

### User Modes

Name     | Character | Type   | Parameter Syntax | Description
-------- | --------- | ------ | ---------------- | -----------
hideoper | h         | Switch | *None*           | Hides the user's server operator status from unprivileged users.
