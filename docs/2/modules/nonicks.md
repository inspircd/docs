---
title: Module Details (nonicks)
---

## The "nonicks" Module

### Description

This module adds channel mode `N` (nonick) which prevents users from changing their nickname whilst in the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_nonicks.so">
```

#### `<nonicks>`

The `<nonicks>` tag defines settings about how the nonicks module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
operoverride | Boolean | No            | Whether server operators can change their nicknames regardless of channel mode `N` (nonick) being set.

##### Example Usage

```xml
<nonicks operoverride="yes">
```

### Channel Modes

Name   | Character | Type   | Parameter Syntax | Description
------ | --------- | ------ | ---------------- | -----------
nonick | N         | Switch | *None*           | Prevents users from changing their nickname whilst in the channel.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
N         | Acting | `N:<mask>` | Bans privileged users matching &lt;mask&gt; from changing their nickname whilst in the channel.

#### Example Usage

Bans privileged users matching `*!*@example.com` from changing their nickname whilst in the channel.

```plaintext
/MODE #channel +b N:*!*@example.com
```
