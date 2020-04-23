---
title: Module Details: maphide (v2)
---

{! 2/_support.md !}

## The "maphide" Module

### Description

This module allows the server administrator to replace the output of a `/MAP` and `/LINKS` with an URL.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_maphide.so">
```

#### `<security>`

This module extends the core `<security>` tag with the following fields:

Name    | Type | Default Value | Description
------- | ---- | ------------- | -----------
maphide | Text | *None*        | **Required!** The URL to provide to users who run the `/MAP` and `/LINKS` commands.

##### Example Usage

```xml
<security ...
          maphide="https://www.example.com/servers">
```
