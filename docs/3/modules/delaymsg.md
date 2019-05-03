---
title: Module Details (delaymsg)
---

## The "delaymsg" Module

### Description

This module adds channel mode `d` (delaymsg) which prevents newly joined users from speaking until the specified number of seconds have passed.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="delaymsg">
```

#### `<delaymsg>`

The `<delaymsg>` tag defines settings about how the delaymsg module should behave. This tag can only be defined once.

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
allownotice | Boolean | Yes           | Whether the delaymsg module also affects notices.

##### Example Usage

```xml
<delaymsg allownotice="yes">
```
### Channel Modes

Name     | Character | Type      | Parameter Syntax | Description
-------- | --------- | --------- | ---------------- | -----------
delaymsg | d         | Parameter | `<seconds>`      | Prevents newly joined users from speaking until &lt;seconds&gt; seconds have passed.

#### Example Usage

Prevents users from speaking for 60 seconds after joining:

```plaintext
/MODE #channel +d 60
```
