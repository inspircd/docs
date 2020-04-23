---
title: Module Details: httpd (v2)
---

{! 2/_support.md !}

## The "httpd" Module

### Description

This module allows the server administrator to serve various useful resources over HTTP.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_httpd.so">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following listener types:

Name  | Description
----- | -----------
httpd | Listens for HTTP connections.

##### Example Usage

Listens for plaintext HTTP connections on the 127.0.0.1:8080 endpoint:

```xml
<bind address="127.0.0.1"
      port="8080"
      ...
      type="httpd">
```

#### `<httpd>`

The `<httpd>` tag defines settings about how the httpd module should behave. This tag can only be defined once.

Name    | Type   | Default Value | Description
------- | ------ | ------------- | -----------
timeout | Number | 0             | The number of seconds to timeout HTTP connections after.

##### Example Usage

```xml
<httpd timeout="10">
```

### Special Notes

The following HTTP resource modules can be used in conjunction with this module:

Name                                    | Description
--------------------------------------- | -----------
[httpd_acl](/2/modules/httpd_acl)       | Allows access to other HTTP resources to be restricted.
[httpd_config](/2/modules/httpd_config) | Allows the server configuration to be viewed over HTTP.
[httpd_stats](/2/modules/httpd_stats)   | Provides statistics about the server and the channels and users on it.
