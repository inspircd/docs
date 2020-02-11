---
title: Module Details (sslinfo)
---

## The "sslinfo" Module

### Description

This module adds user facing SSL information, various SSL configuration options, and the `/SSLINFO` command to look up SSL certificate information for other users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sslinfo">
```

#### `<connect>`

This module extends the core `<connect>` tags with the following fields:

Name       | Type | Default Value | Description
---------  | ---- | ------------- | -----------
requiressl | Text | no            | Whether users must be using SSL to use this class.

The requiressl field should be set to one of the following values:

Value   | Description
------- | -----------
no      | SSL is not required to use this class.
trusted | SSL is required and and a CA-verified client certificate must be provided to use this class.
yes     | SSL is required to use this class.

##### Example Usage

Requires users to be using SSL to be assigned to the Secure class:

```xml
<connect name="Secure"
         ...
         requiressl="yes">
```

#### `<oper>`

This module extends the core `<oper>` tag with the following fields:

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
autologin   | Boolean | No            | Whether to automatically log server operators in when they connect to the server.
fingerprint | Text    | *None*        | If defined then a space-delimited list of fingerprints of this server operator's SSL client certificates.
sslonly     | Boolean | No            | Whether this server operator must be connected using SSL to log into their account.

##### Example Usage

```xml
<oper name="Sadie"
      ...
      autologin="no"
      fingerprint="5d7499e1a3537687a2e875fed60b171508a4d1384351e276c4f961ab80729249"
      sslonly="yes">
```

#### `<sslinfo>`

The `<sslinfo>` tag defines settings about how the sethost module should behave. This tag can only be defined once.

Name     | Type    | Default Value  | Description
-------- | ------- | -------------- | -----------
operonly | Boolean | No             | Whether user SSL certificate fingerprints are only visible to server operators.

##### Example Usage

```xml
<sslinfo operonly="no">
```

### Commands

Name    | Parameter Count | Syntax       | Description
------- | --------------- | ------------ | -----------
SSLINFO | 1               | `<nickname>` | Views the SSL certificate information for &lt;nickname&gt;.

#### Example Usage

Views the SSL certificate information for Sadie:

```plaintext
/SSLINFO Sadie
```

### Special Notes

{! 3/modules/_ssl_table.md !}
