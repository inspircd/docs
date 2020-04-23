---
title: Module Details: pgsql (v3)
---

## The "pgsql" Module

!!! note ""
    This module depends on a third-party library ([libpq](https://www.postgresql.org/docs/current/static/libpq.html)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_pgsql.cpp</pre></code>

### Description

This module provides the ability for SQL modules to query a PostgreSQL database.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="pgsql">
```

#### `<database>`

The `<database>` tag defines a PostgreSQL database to connect to. This tag can be defined as many times as required.

Name   | Type    | Default Value | Description
------ | ------- | ------------- | -----------
module | Text    | *None*        | **Required!** *This MUST be set to "pgsql" to connect to a PostgreSQL database.*
id     | Text    | *None*        | **Required!** The name that SQL-using modules can refer to this `<database>` tag using.
host   | Text    | *None*        | **Required!** The hostname or IP address of a PostgreSQL server.
port   | Number  | *None*        | **Required!** The port on which the PostgreSQL server is listening.
ssl    | Boolean | No            | Whether to connect to the PostgreSQL server using TLS (SSL).
user   | Text    | *None*        | **Required!** The username to log into the PostgreSQL server with.
pass   | Text    | *None*        | **Required!** The password to log into the PostgreSQL server with.
name   | Text    | *None*        | **Required!** The name of the PostgreSQL database to use.

##### Example Usage

```xml
<database module="pgsql"
          id="opers"
          host="localhost"
          port="3306"
          ssl="yes"
          user="ircd_opers"
          pass="changeme"
          name="inspircd">
```
