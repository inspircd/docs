---
title: Module Details (modenotice)
---

## The "modenotice" Module

### Description

This module adds the `/MODENOTICE` command which sends a message to all users with the specified user modes set. If multiple user modes are specified, the notice is only sent to users who have all of them set.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="modenotice">
```

This module requires no other configuration.

### Commands

Name       | Parameter Count | Syntax              | Description
---------- | --------------- | ------------------- | -----------
MODENOTICE | 2               | `<modes> <message>` | Sends &lt;message&gt; to all users with the &lt;modes&gt; user modes set.

#### Example Usage

Sends a message to every user with user mode `i` (invisible) set:

```plaintext
/MODENOTICE i :Hello invisible people!
```
