---
title: Module Details (ldapoper)
---

{! 2/_support.md !}

## The "ldapoper" Module

<div class="alert alert-info" role="alert" markdown="1">

This module depends on a third-party library ([OpenLDAP](https://www.openldap.org)) and must be manually enabled at compile time.

Once you have installed the dependency you can enable this module using the following command:

```sh
./configure --enable-extras=m_ldapoper.cpp
```

</div>

### Description

This module allows server operators to be authenticated against an LDAP database.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_ldapoper.so">
```

#### `<ldapoper>`

The `<ldapoper>` tag defines settings about how the ldapoper module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
attribute    | Text    | *None*        | **Required!** The attribute which is used to locate an account by name. On POSIX systems this is usually "uid".
baserdn      | Text    | *None*        | **Required!** The base Distinguished Name to search in for users.
bindauth     | Text    | *None*        | **Required!** The password for the Distinguished Name specified in the binddn field.
binddn       | Text    | *None*        | **Required!** The Distinguished Name to bind to for searching,
searchscope  | Text    | subtree       | The scope of the search for the LDAP entry.
server       | Text    | *None*        | **Required** The `ldaps://` or `ldap://` URL for your LDAP server.

The searchscope field should be set to one of the following values:

Value    | Description
-------- | -----------
base     | Search only the LDAP object itself.
onelevel | Search the LDAP object and its immediate children.
subtree  | Search the LDAP object and all descendants.

##### Example Usage

```xml
<ldapoper attribute="uid"
          baserdn="ou=People,dc=example,dc=com"
          bindauth="secretpassword"
          binddn="cn=Manager,dc=example,dc=com"
          searchscope="subtree"
          server="ldaps://ldap.example/com">
```
