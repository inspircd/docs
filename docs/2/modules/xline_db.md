---
title: "Module Details: xline_db (v2)"
---

{! 2/_support.md !}

## The "xline_db" Module

### Description

This module allows X-lines to be saved and reloaded on restart.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_xline_db.so">
```

#### `<xlinedb>`

The `<xlinedb>` tag defines settings about how the xline_db module should behave. This tag can only be defined once.

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
filename | Text | data/xline.db | The location to read/write the X-line database from.

##### Example Usage

```xml
<xlinedb filename="data/xline.db">
```
