---
title: Module Details (ldapoper)
---

## The "ldapoper" Module

### Description

This module allows server operators to be authenticated against an LDAP database.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ldapoper">
```

#### `<ldapoper>`

The `<ldapoper>` tag defines settings about how the ldapoper module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
attribute    | Text    | *None*        | **Required!** The attribute which is used to locate an account by name. On POSIX systems this is usually "uid".
baserdn      | Text    | *None*        | **Required!** The base Distinguished Name to search in for users.
dbid         | Text    | *None*        | **Required!** The id of the `<database>` tag that contains the required LDAP configuration.

##### Example Usage

```xml
<ldapoper attribute="uid"
          baserdn="ou=People,dc=example,dc=com"
          dbid="ldap-opers">
```
