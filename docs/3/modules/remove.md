---
title: "Module Details: remove (v3)"
---

## The "remove" Module

### Description

This module adds the `/FPART` and `/REMOVE` commands which allows channel operators to force part users from a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="remove">
```

#### `<remove>`

The `<remove>` tag defines settings about how the remove module should behave. This tag can only be defined once.

Name           | Type    | Default Value | Description
-------------- | ------- | ------------- | -----------
protectedrank  | Number  | 50000         | The rank above which users are protected from being force parted from a channel.
supportnokicks | Boolean | No            | Whether to prevent use of the `/FPART` and `/REMOVE` commands when channel mode `Q` (nokick) is set.

##### Example Usage

```xml
<remove protectedrank="50000"
        supportnokicks="yes">
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
