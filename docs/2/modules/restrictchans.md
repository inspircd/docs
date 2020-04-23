---
title: "Module Details: restrictchans (v2)"
---

{! 2/_support.md !}

## The "restrictchans" Module

### Description

This module prevents users who are not server operators from creating new channels.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_restrictchans.so">
```

#### `<allowchannel>`

The `<allowchannel>` tag defines a channel which may be created by non-server operators. This tag can be defined as many times as required.

Name | Type | Default Value | Description
---- | ---- | ------------- | -----------
name | Text | *None*        | **Required!** The name of a channel which can be created by non-server operators.

##### Example Usage

Allows non-server operators to create the #guests channel:

```xml
<allowchannel name="#guests">
```
