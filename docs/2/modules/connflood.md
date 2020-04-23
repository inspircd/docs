---
title: "Module Details: connflood (v2)"
---

{! 2/_support.md !}

## The "connflood" Module

### Description

This module throttles IP addresses which make excessive connections to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_connflood.so">
```

#### `<connflood>`

The `<connflood>` tag defines settings about how the connflood module should behave. This tag can only be defined once.

Name     | Type   | Default Value | Description
-------- | ------ | ------------- | -----------
bootwait | Number | *None*        | The number of seconds to wait after starting up before connections should be throttled.
maxconns | Number | *None*        | The maximum number of connections to allow before throttling.
seconds  | Number | *None*        | The number of seconds after which the connection counter is reset.
timeout  | Number | *None*        | The number of seconds to disallow connections for after passing the throttling threshold.
quitmsg  | Text   | *None*        | The message to quit throttled users with.

##### Example Usage

```xml
<connflood bootwait="10"
           maxconns="3"
           seconds="30"
           timeout="30"
           quitmsg="Throttled">
```
