---
title: Module Details (flashpolicyd)
---

## The "flashpolicyd" Module

### Description

This module allows connection policies to be served to IRC clients that use Adobe Flash.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="flashpolicyd">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following listener types:

Name         | Description
------------ | -----------
flashpolicyd | Listens for Adobe Flash policy connections.

##### Example Usage

Listens for plaintext Adobe Flash policy connections on the 127.0.0.1:8080 endpoint:

```xml
<bind address="127.0.0.1"
      port="8080"
      ...
      type="flashpolicyd">
```

#### `<flashpolicyd>`

The `<flashpolicyd>` tag defines settings about how the flashpolicyd module should behave. This tag can only be defined once.

Name    | Type     | Default Value | Description
------- | -------- | ------------- | -----------
file    | Text     | *None*        | If defined then the location of a file which contains Adobe Flash policy XML to use instead of the default.
timeout | Duration | 5s            | The duration to timeout Adobe Flash policy connections after.

##### Example Usage

```xml
<flashpolicyd timeout="5s">
```
