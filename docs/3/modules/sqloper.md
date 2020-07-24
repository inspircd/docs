---
title: "Module Details: sqloper (v3)"
---

## The "sqloper" Module

### Description

This module allows server operators to be authenticated against an SQL table.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sqloper">
```

#### `<sqloper>`

The `<sqloper>` tag defines settings about how the sqloper module should behave. This tag can only be defined once.

Name  | Type | Default Value                           | Description
----- | ---- | --------------------------------------- | -----------
dbid  | Text | *None*                                  | **Required!** The name of the database connection to execute the query against.
query | Text | SELECT * FROM ircd_opers WHERE active=1 | The SQL query to retrieve the server operators with.

{! 3/modules/_hash_table.md !}

##### Example Usage

```xml
<sqloper dbid="sqloper"
         query="SELECT * FROM ircd_opers WHERE active=1">
```

```xml
<sqloper dbid="sqloper"
         query="SELECT username as name, '*' as host, oper_class as type, sha256_password as password, 'sha256' as hash FROM users WHERE oper_class IS NOT NULL">
```

 For each row an <oper> will be defined using the field values returned. See the [<oper> configuration docs](https://docs.inspircd.org/3/configuration/#ltopergt) for column names, default values and required columns.

### Special Notes

{! 3/modules/_sql_table.md !}

Example schemas for the server operator database are available in [the `sql` subdirectory of the InspIRCd configuration directory](https://github.com/inspircd/inspircd/tree/master/docs/sql). You can define your own schema as long as your query returns the required columns.
