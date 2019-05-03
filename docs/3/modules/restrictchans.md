---
title: Module Details (restrictchans)
---

## The "restrictchans" Module

### Description

This module prevents unprivileged users from creating new channels.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="restrictchans">
```

#### `<allowchannel>`

The `<allowchannel>` tag defines a channel which may be created by non-server operators. This tag can be defined as many times as required.

Name | Type | Default Value | Description
---- | ---- | ------------- | -----------
name | Text | *None*        | **Required!** The name of a channel which can be created by non-server operators.

##### Example Usage

Allows unprivileged users to create the #guests channel:

```xml
<allowchannel name="#guests">
```

#### `<restrictchans>`

The `<restrictchans>` tag defines settings about how the restrictchans module should behave. This tag can only be defined once.

Name            | Type    | Default Value | Description
--------------- | ------- | ------------- | -----------
allowregistered | Boolean | Yes           | Whether users who are logged into an account can create channels.

##### Example Usage

```xml
<restrictchans allowregistered="yes">
```
