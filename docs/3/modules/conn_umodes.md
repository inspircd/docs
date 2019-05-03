---
title: Module Details (conn_umodes)
---

## The "conn_umodes" Module

### Description

This module allows the server administrator to set user modes on connecting users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="conn_umodes">
```

#### `<connect>`

This module extends the core `<connect>` tags with the following fields:

Name  | Type | Default Value | Description
----- | ---- | ------------- | -----------
modes | Text | *None*        | The user modes to set on connecting users.

##### Example Usage

Forces all users in the Example class to have user modes `iw` (invisible, wallops):

```xml
<connect name="Example"
         ...
         modes="+iw">
```

### Special Notes

This module can set disabled modes which allows you to set user modes on users which they can not then remove.
