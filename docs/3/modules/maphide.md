---
title: Module Details (maphide)
---

## The "maphide" Module

### Description

This module allows the server administrator to replace the output of a `/MAP` and `/LINKS` with an URL.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="maphide">
```

#### `<security>`

This module extends the core `<security>` tag with the following fields:

Name    | Type | Default Value | Description
------- | ---- | ------------- | -----------
maphide | Text | *None*        | The URL to provide to users who run the `/MAP` and `/LINKS` commands.

##### Example Usage

```xml
<security ...
          maphide="http://www.example.com/servers">
```
