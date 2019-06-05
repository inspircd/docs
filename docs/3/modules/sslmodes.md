---
title: Module Details (sslmodes)
---

## The "sslmodes" Module

### Description

This module adds channel mode `z` (sslonly) which prevents users who are not connecting using SSL from joining the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sslmodes">
```

#### `<sslmodes>`

The `<sslmodes>` tag defines settings about how the sslmodes module should behave. This tag can only be defined once.

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
enableumode | Boolean | No            | Whether user mode `z` (sslqueries) is enabled.

##### Example Usage

```xml
<sslmodes enableumode="yes">
```

### Channel Modes

Name    | Character | Type   | Parameter Syntax | Description
------- | --------- | ------ | ---------------- | -----------
sslonly | z         | Switch | *None*           | Prevents users who are not connected using SSL from joining the channel.

### User Modes

Name       | Character | Type   | Parameter Syntax | Description
---------- | --------- | ------ | ---------------- | -----------
sslqueries | z         | Switch | *None*           | Prevents messages from being sent to or received from a user that is not connected using SSL.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
z         | Matching | `z:<pattern>` | Checks whether users have an SSL client certificate with a fingerprint matching &lt;pattern&gt;.

#### Example Usage

Bans users with an SSL client certificate fingerprint of 5d7499e1a3537687a2e875fed60b171508a4d1384351e276c4f961ab80729249:

```plaintext
/MODE #channel +b z:5d7499e1a3537687a2e875fed60b171508a4d1384351e276c4f961ab80729249
```

### Special Notes

If you want to link against InspIRCd v2 servers you must not enable user mode `z` (sslqueries).
