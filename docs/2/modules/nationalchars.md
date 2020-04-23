---
title: "Module Details: nationalchars (v2)"
---

{! 2/_support.md !}

## The "nationalchars" Module

### Description

This module allows the server administrator to define what characters are allowed in nicknames and channel names and how those characters should be compared in a case insensitive way.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_nationalchars.so">
```

#### `<nationalchars>`

The `<nationalchars>` tag defines settings about how the nationalchars module should behave. This tag can only be defined once.

Name        | Type | Default Value | Description
----------- | ---- | ------------- | -----------
casemapping | Text | *None*        | The name for the character map which will be sent to users in the `005` (RPL_ISUPPORT) numeric.
file        | Text | *None*        | The location of the locale file on disk.

##### Example Usage

```xml
<nationalchars casemapping="iso88591"
               file="/path/to/locales/iso88591">
```

### Special Notes

A list of files for use with this module are present in the locales directory which exists in the root of the source tarball.

You can also create your own locale file. See the rules documented in `locales/readme.txt` for more information.
