---
title: "Module Details: ident (v2)"
---

{! 2/_support.md !}

## The "ident" Module

### Description

This module allows the usernames (idents) of users to be looked up using the [RFC 1413 Identification Protocol](https://www.ietf.org/rfc/rfc1413.txt). This is useful for shared hosts where many users may be connecting from one IP address as it allows you to ban specific users without banning the entire provider.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_ident.so">
```

#### `<connect>`

This module extends the core `<connect>` tags with the following fields:

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
useident     | Boolean | Yes           | Whether users in this connect class should have their usernames (idents) looked up.
requireident | Boolean | No            | Whether users must have responded to a username (ident) lookup to be assigned to this class.

##### Example Usage

Disables username (ident) lookups for users in the WebChat class:

```xml
<connect name="WebChat"
         ...
         useident="no">
```

Requires users connecting from 192.0.2.0/24 to respond to username (ident) lookups to be assigned to the BNC class:

```xml
<connect name="BNC"
         allow="192.0.2.0/24"
         ...
         requireident="yes">
```

#### `<ident>`

The `<ident>` tag defines settings about how the ident module should behave. This tag can only be defined once.

Name    | Type   | Default Value | Description
------- | ------ | ------------- | -----------
timeout | Number | 5             | The number of seconds to timeout username (ident) lookups after.

##### Example Usage

```xml
<ident timeout="5">
```
