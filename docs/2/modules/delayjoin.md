---
title: Module Details: delayjoin (v2)
---

{! 2/_support.md !}

## The "delayjoin" Module

### Description

This module adds channel mode `D` (delayjoin) which hides JOIN messages from users until they speak.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_delayjoin.so">
```

This module requires no other configuration.

### Channel Modes

Name      | Character | Type   | Parameter Syntax | Description
--------- | --------- | ------ | ---------------- | -----------
delayjoin | D         | Switch | *None*           | Prevents users from receiving JOIN messages until the joining user speaks.
