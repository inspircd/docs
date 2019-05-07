---
title: Module Details (ircv3_sts)
---

## The "ircv3_sts" Module

### Description

This module adds support for the IRCv3 Strict Transport Security specification.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3_sts">
```

#### `<sts>`

The `<sts>` tag defines settings about how the sts module should behave. This tag can only be defined once.

Name     | Type     | Default Value  | Description
-------- | -------- | -------------- | -----------
host     | Text     | *None*         | **Required!** A glob pattern for the hostname a user must send to use STS.
duration | Duration | 60d            | The time period that the STS policy should last for.
port     | Number   | *None*         | **Required!** The port that clients should connect on securely.
preload  | Boolean  | No             | Whether the STS policy can be included in preload lists.

##### Example Usage

```xml
<sts host="*.example.com"
     duration="60d"
     port="6697"
     preload="yes">
```

### Client Capabilities

Name                                               | Description
-------------------------------------------------- | -----------
[sts](https://ircv3.net/specs/extensions/sts.html) | Defines a mechanism for clients to upgrade plaintext IRC connections to TLS.
