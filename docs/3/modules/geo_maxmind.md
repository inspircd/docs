---
title: "Module Details: geo_maxmind (v3)"
---

## The "geo_maxmind" Module

!!! note ""
    This module depends on a third-party library ([libMaxMindDB](https://maxmind.github.io/libmaxminddb/)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras geo_maxmind</code></pre>

### Description

This module allows the server to perform geolocation lookups on both IP addresses and users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_geo_maxmind.so">
```

#### `<maxmind>`

The `<maxmind>` tag defines settings about how the geo_maxmind module should behave. This tag can only be defined once.

Name | Type | Default Value         | Description
---- | ---- | --------------------- | -----------
file | Text | GeoLite2-Country.mmdb | The location of the GeoLite2 database to read locations from.

##### Example Usage

```xml
<maxmind file="GeoLite2-Country.mmdb">
```
