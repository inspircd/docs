---
title: Module Details (starttls)
---

## The "starttls" Module

### Description

This module provides the IRCv3 `tls` client capability.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="starttls">
```

#### `<starttls>`

The `<starttls>` tag defines settings about how the starttls module should behave. This tag can only be defined once.

Name     | Type     | Default Value | Description
-------- | -------- | ------------- | -----------
provider | Text     | *None*        | The name of the SSL profile to use for STARTTLS clients.

##### Example Usage

```xml
<starttls provider="gnutls">
```

### Client Capabilities

Name                                                   | Description
------------------------------------------------------ | -----------
[tls](https://ircv3.net/specs/extensions/tls-3.1.html) | Allows plain text connections to upgrade to TLS.
