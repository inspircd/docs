---
title: Module Details (httpd_stats)
---

## The "httpd_stats" Module

### Description

This module provides XML-serialised statistics about the server, channels, and users over HTTP via the /stats path.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="httpd_stats">
```
#### `<httpstats>`

The `<httpstats>` tag defines settings about how the httpd_stats module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
enableparams | Boolean | No            | Whether parameterized queries are enabled. Disabled by default for performance reasons.

##### Example Usage

```xml
<httpstats enableparams="no">
```

### Special Notes

Leaking your server statistics over the internet is a privacy and security risk. You should avoid doing this by either configuring [the httpd module](/3/modules/httpd) to only listen for local connections or by using [the httpd_acl module](/3/modules/httpd_acl) to restrict who can view your server configuration.
