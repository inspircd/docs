---
title: Module Details: clearchan (v3)
---

## The "clearchan" Module

### Description

This module adds the `/CLEARCHAN` command which allows server operators to mass-punish the members of a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="clearchan">
```

This module requires no other configuration.

### Commands

Name      | Parameter Count | Syntax                            | Description
--------- | --------------- | --------------------------------- | -----------
CLEARCHAN | 2-3             | `<channel> [<action>] [<reason>]` | Mass punishes the members of the specified channel.

The action parameter should be set to one of the following values:

Value | Description
----- | -----------
KILL  | Kill all members of the channel (default behaviour).
KICK  | Kick all members of the channel.
G     | G-line all members of the channel for one hour.
Z     | Z-line all members of the channel for one hour.

#### Example Usage

Kills all members of #spam:

```plaintext
/CLEARCHAN #spam
```

Kicks all members of #spam:

```plaintext
/CLEARCHAN #spam KICK
```

G-lines all members of #spam with the reason "Spamming is bad":

```plaintext
/CLEARCHAN #spam G :Spamming is bad
```
