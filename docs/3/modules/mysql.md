---
title: "Module Details: mysql (v3)"
---

## The "mysql" Module

!!! note ""
    This module depends on a third-party library ([libmysqlclient](https://dev.mysql.com/downloads/connector/c/)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_mysql.cpp</code></pre>

### Description

This module provides the ability for SQL modules to query a MySQL database.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="mysql">
```

#### `<database>`

The `<database>` tag defines a MySQL database to connect to. This tag can be defined as many times as required.

Name    | Type   | Default Value | Description
------- | ------ | ------------- | -----------
module  | Text   | *None*        | **Required!** *This MUST be set to "mysql" to connect to a MySQL database.*
id      | Text   | *None*        | **Required!** The name that SQL-using modules can refer to this `<database>` tag using.
host    | Text   | *None*        | **Required!** The hostname or IP address of a MySQL server.
port    | Number | *None*        | **Required!** The port on which the MySQL server is listening.
user    | Text   | *None*        | **Required!** The username to log into the MySQL server with.
pass    | Text   | *None*        | **Required!** The password to log into the MySQL server with.
name    | Text   | *None*        | **Required!** The name of the MySQL database to use.
charset | Text   | *None*        | If defined then a custom character set to use with the MySQL server.

##### Example Usage

```xml
<database module="mysql"
          id="opers"
          host="localhost"
          port="3306"
          user="ircd_opers"
          pass="changeme"
          name="inspircd"
          charset="utf8">
```
