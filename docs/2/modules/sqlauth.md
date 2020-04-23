---
title: Module Details: sqlauth (v2)
---

{! 2/_support.md !}

## The "sqlauth" Module

### Description

This module allows connecting users to be authenticated against an arbitrary SQL table.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_sqlauth.so">
```

#### `<sqlauth>`

The `<sqlauth>` tag defines settings about how the sqlauth module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
allowpattern | Text    | *None*        | If defined then a glob pattern for nicknames that are exempted from the authentication requirement.
dbid         | Text    | *None*        | **Required!** The name of the database connection to execute the query against.
killreason   | Text    | *None*        | **Required!** The message to kill users that fail to authenticate with.
query        | Text    | *None*        | **Required!** The SQL query to authenticate users with. If this query returns one or more rows it is considered a success otherwise it is considered a failure.
verbose      | Boolean | No            | Whether to log failed authentications to snomask `a` (local) and snomask `A` (remote).

The query field can contain any of the following template variables:

Variable    | Description
----------- | -----------
$gecos      | The real name (gecos) of the connecting user.
$host       | The real hostname of the connecting user.
$ident      | The username (ident) of the connecting user.
$ip         | The IP address of the connecting user.
$md5pass    | An MD5 hash of the password sent with `/PASS` by the connecting user (requires [the md5 module](/2/modules/md5)).
$nick       | The nickname of the connecting user.
$pass       | The password sent with `/PASS` by the connecting user.
$server     | The name of the server the connecting user connected to.
$sha256pass | A SHA-256 hash of the password sent with `/PASS` by the connecting user (requires [the sha256 module](/2/modules/sha256)).
$uuid       | The UUID of the connecting user.

##### Example Usage

```xml
<sqlauth allowpattern="Guest*"
         dbid="sqlauth"
         killreason="Access denied"
         query="SELECT * FROM users WHERE name='$nick' AND password='$sha256pass' LIMIT 1"
         verbose="no">
```

### Special Notes

{! 2/modules/_sql_table.md !}
