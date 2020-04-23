---
title: "Module Details: globops (v2)"
---

{! 2/_support.md !}

## The "globops" Module

### Description

This module adds the `/GLOBOPS` command which allows server operators to send messages to all server operators with the `g` (globops) snomask.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_globops.so">
```

This module requires no other configuration.

### Commands

Name    | Parameter Count | Syntax      | Description
------- | --------------- | ----------- | -----------
GLOBOPS | 1               | `<message>` | Sends &lt;message&gt; to all server operators with the `g` (globops) snomask.

#### Example Usage

Sends a server notice saying "I like turtles." to all server operators with the `g` (globops) snomask:

```plaintext
/GLOBOPS :I like turtles.
```

### Server Notice Masks

Character | Description
--------- | -----------
g         | Messages from server operators on the local server.
G         | Messages from server operators on a remote server.
