---
title: Module Details (delayjoin)
---

## The "delayjoin" Module

### Description

This module adds channel mode `D` (delayjoin) which hides JOIN messages from users until they speak.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="delayjoin">
```

This module requires no other configuration.

### Channel Modes

Name      | Character | Type   | Parameter Syntax | Usable By         | Description
--------- | --------- | ------ | ---------------- | ----------------- | -----------
delayjoin | D         | Switch | *None*           | Channel operators | Prevents users from receiving JOIN messages until the joining user speaks.
