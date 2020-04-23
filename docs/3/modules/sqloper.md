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

### Special Notes

{! 3/modules/_sql_table.md !}

Schemas for the server operator database are available in [the `sql` subdirectory of the InspIRCd configuration directory](https://github.com/inspircd/inspircd/tree/master/docs/sql).
