---
title: Module Details (sqlite3)
---

{! 2/_support.md !}

## The "sqlite3" Module

!!! note ""
    This module depends on a third-party library ([SQLite](https://www.sqlite.org/index.html)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

     <pre><code>./configure --enable-extras m_sqlite3.cpp</code></pre>

### Description

This module provides the ability for SQL modules to query a SQLite 3 database.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_sqlite3.so">
```

#### `<database>`

The `<database>` tag defines a SQLite 3 database to connect to. This tag can be defined as many times as required.

Name     | Type   | Default Value | Description
-------- | ------ | ------------- | -----------
module   | Text   | *None*        | **Required!** *This MUST be set to "sqlite" to connect to a SQLite 3 database.*
id       | Text   | *None*        | **Required!** The name that SQL-using modules can refer to this `<database>` tag using.
hostname | Text   | *None*        | **Required!** The path to where the SQLite database is stored.

##### Example Usage

```xml
<database module="sqlite"
          id="opers"
          hostname="/path/to/database.sq3">
```
