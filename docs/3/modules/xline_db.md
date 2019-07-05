---
title: Module Details (xline_db)
---

## The "xline_db" Module

### Description

This module allows X-lines to be saved and reloaded on restart.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="xline_db">
```

#### `<xlinedb>`

The `<xlinedb>` tag defines settings about how the xline_db module should behave. This tag can only be defined once.

Name       | Type     | Default Value | Description
---------- | -------- | ------------- | -----------
filename   | Text     | xline.db      | The location to read/write the X-line database from.
saveperiod | Duration | 5s            | [**New in v3.2.0!**](/3/change-log/#inspircd-320) The time period between attempts to check whether the X-line database needs to be written.

##### Example Usage

```xml
<xlinedb filename="xline.db"
         saveperiod="5s">
```
