---
title: Module Details (remove)
---

## The "remove" Module

### Description

This module adds the `/REMOVE` command which allows channel operators to force part users from a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_remove.so">
```

#### `<remove>`

The `<remove>` tag defines settings about how the remove module should behave. This tag can only be defined once.

Name           | Type    | Default Value | Description
-------------- | ------- | ------------- | -----------
supportnokicks | Boolean | No            | Whether to prevent use of the `/FPART` and `/REMOVE` commands when channel mode `Q` (nokick) is set.

##### Example Usage

```xml
<remove supportnokicks="yes">
```
### Commands

Name   | Parameter Count | Syntax                        | Description
------ | --------------- | ----------------------------- | -----------
FPART  | 2-3             | `<channel> <nick> [<reason>]` | Force parts &lt;nick&gt; from &lt;channel&gt; optionally with the reason specified in &lt;reason&gt;.
REMOVE | 2-3             | `<nick> <channel> [<reason>]` | Force parts &lt;nick&gt; from &lt;channel&gt; optionally with the reason specified in &lt;reason&gt;.

#### Example Usage

Force parts Soni from #channel:

```plaintext
/FPART #channel Soni :Disruptive behaviour is not allowed
```

Force parts Soni from #channel:

```plaintext
/REMOVE Soni #channel :Disruptive behaviour is not allowed
```
