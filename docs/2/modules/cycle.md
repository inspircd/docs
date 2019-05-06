---
title: Module Details (cycle)
---

## The "cycle" Module

### Description

This module allows channel members to part and rejoin a channel without needing to worry about channel modes such as +i (inviteonly) which might prevent rejoining.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_cycle.so">
```

This module requires no other configuration.

### Commands

Name  | Parameter Count | Syntax                 | Description
----- | --------------- | ---------------------- | -----------
CYCLE | 1-2             | `<channel> [<reason>]` | Parts and rejoins the specified channel.

#### Example Usage

Parts and rejoins the #example channel:

```plaintext
/CYCLE #example
```

Parts and rejoins the #example channel with "Be right back!" as the reason:

```plaintext
/CYCLE #example :Be right back!
```
