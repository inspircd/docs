---
title: Module Details: restrictmsg (v2)
---

{! 2/_support.md !}

## The "restrictmsg" Module

### Description

This module prevents users who are not server operators from messaging each other.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_restrictmsg.so">
```

#### `<restrictmsg>`

The `<restrictmsg>` tag defines settings about how the restrictmsg module should behave. This tag can only be defined once.

Name  | Type    | Default Value | Description
----- | ------- | ------------- | -----------
uline | Boolean | No            | Whether users are allowed to message other users on U-lined servers (i.e. services pseudoclients).

##### Example Usage

```xml
<restrictmsg uline="yes">
```
