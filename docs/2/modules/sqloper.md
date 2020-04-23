---
title: Module Details: sqloper (v2)
---

{! 2/_support.md !}

## The "sqloper" Module

### Description

This module allows server operators to be authenticated against an SQL table.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_sqloper.so">
```

#### `<sqloper>`

The `<sqloper>` tag defines settings about how the sqloper module should behave. This tag can only be defined once.

Name  | Type | Default Value                                                                                     | Description
----- | ---- | ------------------------------------------------------------------------------------------------- | -----------
dbid  | Text | *None*                                                                                            | **Required!** The name of the database connection to execute the query against.
hash  | Text | *None*                                                                                            | The algorithm that server operator passwords are hashed with.
query | Text | SELECT hostname as host, type FROM ircd_opers WHERE username='$username' AND password='$password' | The SQL query to retrieve the server operator with.

The query field can contain any of the following template variables:

Variable  | Description
--------- | -----------
$gecos    | The real name (gecos) of the user.
$host     | The real hostname of the user.
$ident    | The username (ident) of the user.
$ip       | The IP address of the user.
$nick     | The nickname of the user.
$password | The password that the user specified in the `/OPER` command. Hashed with the algorithm specified in the server configuration.
$server   | The name of the server the user who is attempting to log into an operator account connected to.
$username | The username that the user specified in the `/OPER` command.
$uuid     | The UUID of the user.

{! 2/modules/_hash_table.md !}

##### Example Usage

```xml
<sqloper dbid="sqloper"
         hash="hmac-sha256"
         query="SELECT hostname as host, type FROM ircd_opers WHERE username='$username' AND password='$password'">
```

### Special Notes

{! 2/modules/_sql_table.md !}

Schemas for the server operator database are available in [the extras directory in the root of the InspIRCd source code](https://github.com/inspircd/inspircd/tree/insp20/extras).
