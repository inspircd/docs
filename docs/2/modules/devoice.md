---
title: Module Details (devoice)
---

{! 2/_support.md !}

## The "devoice" Module

### Description

This module adds the `/DEVOICE` command which allows users with channel prefix mode `v` (voice) to remove it from themselves.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_devoice.so">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax      | Description
------- | --------------- | ----------- | -----------
DEVOICE | 1               | `<channel>` | Removes channel prefix mode `v` (voice) from the user in &lt;channel&gt;.

#### Example Usage

```plaintext
/DEVOICE #channel
```
