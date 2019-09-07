---
title: Module Details (connectban)
---

{! 2/_support.md !}

## The "connectban" Module

### Description

This module Z-lines IP addresses which make excessive connections to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_connectban.so">
```

#### `<connectban>`

The `<connectban>` tag defines settings about how the connectban module should behave. This tag can only be defined once.

Name        | Type     | Default Value | Description
----------- | -------- | ------------- | -----------
banduration | Duration | 10m           | The duration that an IP address should be banned for.
ipv4cidr    | Number   | 32            | The IPv4 CIDR range to treat as equivalent when looking for excessive connections.
ipv6cidr    | Number   | 128           | The IPv6 CIDR range to treat as equivalent when looking for excessive connections.
threshold   | Number   | 10            | The number of times that an IP address can connect within an hour.

##### Example Usage

```xml
<connectban banduration="10m"
            ipv4cidr="32"
            ipv6cidr="128"
            threshold="10">
```
