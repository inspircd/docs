---
title: "Module Details: customprefix (v2)"
---

{! 2/_support.md !}

## The "customprefix" Module

### Description

This module allows the server administrator to configure custom channel prefix modes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_customprefix.so">
```

#### `<customprefix>`

The `<customprefix>` tag defines a custom channel prefix mode. This tag can be defined as many times as required.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
name      | Text    | *None*        | **Required!** The unique name of the mode.
letter    | Text    | *None*        | **Required!** The character used for the mode.
prefix    | Text    | *None*        | The prefix character used for the mode.
rank      | Number  | *None*        | The rank of the mode. Users with higher ranked prefix modes have privileges over users with lower ranks or no rank.
ranktoset | Number  | *None*        | The rank which is required to set this prefix mode.
depriv    | Boolean | *None*        | Whether a user with this prefix mode can remove it from themself.

##### Example Usage

Adds the founder and admin channel prefix modes as seen in other IRC servers:

```xml
<customprefix name="founder"
              letter="q"
              prefix="~"
              rank="50000"
              ranktoset="50000"
              depriv="yes">

<customprefix name="admin"
              letter="a"
              prefix="&"
              rank="40000"
              ranktoset="50000"
              depriv="yes">
```

Adds the half-operator channel prefix mode as seen in other IRC servers:

```xml
<customprefix name="halfop"
              letter="h"
              prefix="%"
              rank="20000"
              ranktoset="30000"
              depriv="yes">
```

### Special Notes

The ranks of the built-in channel prefix modes are:

- op (+o) &mdash; 30000

- voice (+v) &mdash; 10000

You should take note of this when adding new modes.
