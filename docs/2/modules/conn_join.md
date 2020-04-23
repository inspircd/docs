---
title: Module Details: conn_join (v2)
---

{! 2/_support.md !}

## The "conn_join" Module

### Description

This module allows the server administrator to force users to join one or more channels on connect.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_conn_join.so">
```

#### `<connect>`

This module extends the core `<connect>` tags with the following fields:

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
autojoin | Text | *None*        | A comma-delimited list of channels for users in this connect class to be joined to on connect.

##### Example Usage

Forces all users in the Example class to join #example1 and #example2 on connect:

```xml
<connect name="Example"
         ...
         autojoin="#example1,#example2">
```

#### `<autojoin>`

The `<autojoin>` tag defines settings about how the conn_join module should behave. This tag can only be defined once.

Name    | Type | Default Value | Description
------- | ---- | ------------- | -----------
channel | Text | *None*        | A comma-delimited list of channels for users to be joined to on connect.

##### Example Usage

Forces all users to join #example on connect:

```xml
<autojoin channel="#example">
```
