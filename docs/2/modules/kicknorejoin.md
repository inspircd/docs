---
title: Module Details (kicknorejoin)
---

## The "kicknorejoin" Module

### Description

This module adds channel mode `J` (kicknorejoin) which prevents users from rejoining after being kicked from a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_kicknorejoin.so">
```

#### `<kicknorejoin>`

The `<kicknorejoin>` tag defines settings about how the kicknorejoin module should behave. This tag can only be defined once.

Name    | Type     | Default Value | Description
------- | -------- | ------------- | -----------
maxtime | Duration | 30m           | The maximum time that can be set as a parameter for channel mode `J` (kicknorejoin).

### Channel Modes

Name         | Character | Type      | Parameter Syntax | Description
------------ | --------- | --------- | ---------------- | -----------
kicknorejoin | J         | Parameter | `<seconds>`      | Prevents who have been kicked for rejoining until &lt;seconds&gt; seconds have passed.

#### Example Usage

Prevents kicked users from rejoining for 30 seconds:

```plaintext
/MODE #channel +J 30
```
