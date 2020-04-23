---
title: "Module Details: ldap (v3)"
---

## The "ldap" Module

!!! note ""
    This module depends on a third-party library ([OpenLDAP](https://www.openldap.org)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_ldap.cpp</pre></code>

### Description

This module provides the ability for LDAP modules to query a LDAP directory.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ldap">
```

#### `<database>`

The `<database>` tag defines a PostgreSQL database to connect to. This tag can be defined as many times as required.

Name        | Type     | Default Value | Description
----------- | -------- | ------------- | -----------
module      | Text     | *None*        | **Required!** *This MUST be set to "ldap" to connect to an LDAP directory.*
id          | Text     | *None*        | **Required!** The name that LDAP-using modules can refer to this `<database>` tag using.
bindauth    | Text     | *None*        | **Required!** The password for the Distinguished Name specified in the binddn field.
binddn      | Text     | *None*        | **Required!** The Distinguished Name to bind to for searching,
searchscope | Text     | subtree       | The scope of the search for the LDAP entry.
server      | Text     | *None*        | **Required** The `ldaps://` or `ldap://` URL for your LDAP server.
timeout     | Duration | 5s            | The time to wait before expiring an unresponsive LDAP connection.

The searchscope field should be set to one of the following values:

Value    | Description
-------- | -----------
base     | Search only the LDAP object itself.
onelevel | Search the LDAP object and its immediate children.
subtree  | Search the LDAP object and all descendants.

##### Example Usage

```xml
<database module="ldap"
          id="users"
          bindauth="password"
          binddn="cn=Manager,dc=inspircd,dc=org"
          searchscope="subtree"
          server="ldaps://localhost"
          timeout="5s">
```
