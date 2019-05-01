---
title: Module Details (nicklock)
---

## The "nicklock" Module

### Description

This module adds the `/NICKLOCK` command which allows server operators to change a user's nickname and prevent them from changing it again until they disconnect.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_nicklock.so">
```

This module requires no other configuration.

### Commands

Name       | Parameter Count | Syntax                  | Description
---------- | --------------- | ----------------------- | -----------
NICKLOCK   | 2               | `<old-nick> <new-nick>` | Changes the nickname of `<old-nick>` to `<new-nick>` and prevents them from changing their nickname.
NICKUNLOCK | 1               | `<locked-nick>`         | Allows `<locked-nick>` to change their nickname.

#### Example Usage

Changes the nickname of Sadie to Sadie2 and prevents them from changing their nickname:

```plaintext
/NICKLOCK Sadie Sadie2
```

Allows Sadie to change their nickname:

```plaintext
/NICKUNLOCK Sadie
```