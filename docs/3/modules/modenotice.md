---
title: Module Details (modenotice)
---

## The "modenotice" Module

### Description

This module adds the `/MODENOTICE` command which Sends a message to all users with the specified user modes set.


### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="modenotice">
```

This module requires no other configuration.

### Commands

Name       | Parameter Count | Syntax              | Description
---------- | --------------- | ------------------- | -----------
MODENOTICE | 2               | `<modes> <message>` | Sends `<message>` to all users with the `<modes>` user modes set.

#### Example Usage

Sends a message to every user with user mode `i` (invisible) set:

```plaintext
/MODENOTICE i :Hello invisible people!
```
