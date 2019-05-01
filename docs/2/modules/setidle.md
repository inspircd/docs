---
title: Module Details (setidle)
---

## The "setidle" Module

### Description

This module adds the `/SETIDLE` command which allows server operators to change their idle time.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_setidle.so">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax       | Description
------- | --------------- | ------------ | -----------
SETIDLE | 1               | `<duration>` | Changes the idle time of the user to &lt;duration&gt;.

#### Example Usage

Changes the idle time of the user to five minutes:

```plaintext
/SETIDLE 5m
```
