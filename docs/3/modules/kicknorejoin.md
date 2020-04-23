---
title: Module Details: kicknorejoin (v3)
---

## The "kicknorejoin" Module

### Description

This module adds channel mode `J` (kicknorejoin) which prevents users from rejoining after being kicked from a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="kicknorejoin">
```

### Channel Modes

Name         | Character | Type      | Parameter Syntax | Usable By         | Description
------------ | --------- | --------- | ---------------- | ----------------- | -----------
kicknorejoin | J         | Parameter | `<seconds>`      | Channel operators | Prevents who have been kicked from rejoining until &lt;seconds&gt; seconds have passed.

#### Example Usage

Prevents kicked users from rejoining for 30 seconds:

```plaintext
/MODE #channel +J 30
```
