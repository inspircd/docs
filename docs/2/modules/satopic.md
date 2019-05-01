---
title: Module Details (satopic)
---

## The "satopic" Module

### Description

This module adds the `/SATOPIC` command which allows server operators to change the topic of a channel that they would not otherwise have the privileges to change.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_satopic.so">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax              | Description
------- | --------------- | ------------------- | -----------
SATOPIC | 2               | `<channel> <topic>` | Changes the topic of &lt;channel&gt; to &lt;topic&gt;.

#### Example Usage

Changes the topic of #animals to "I like turtles":

```plaintext
/SATOPIC #animals :I like turtles
```
