---
title: Module Details: ldapauth (v3)
---

## The "ldapauth" Module

### Description

This module allows connecting users to be authenticated against an LDAP database.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ldapauth">
```

#### `<ldapauth>`

The `<ldapauth>` tag defines settings about how the ldapauth module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
allowpattern | Text    | *None*        | If defined then a glob pattern for nicknames that are exempted from the authentication requirement.
attribute    | Text    | *None*        | **Required!** The attribute which is used to locate an account by name. On POSIX systems this is usually "uid".
baserdn      | Text    | *None*        | **Required!** The base Distinguished Name to search in for users.
dbid         | Text    | *None*        | **Required!** The id of the `<database>` tag that contains the required LDAP configuration.
host         | Text    | *None*        | If defined then the vhost to set on connecting users.
killreason   | Text    | *None*        | **Required!** The message to kill users that fail to authenticate with.
userfield    | Boolean | No            | Whether to authenticate users against their username (ident) instead of their nick.
verbose      | Boolean | No            | Whether to log failed authentications to snomask `a` (local) and snomask `A` (remote).

##### Example Usage

```xml
<ldapauth allowpattern="Guest*"
          attribute="uid"
          baserdn="ou=People,dc=example,dc=com"
          dbid="ldap-users"
          host="$cn.example.com"
          killreason="Access denied"
          userfield="no"
          verbose="yes">
```

#### `<ldaprequire>`

The `<ldaprequire>` tag defines LDAP attributes that must be set on users in order for them to be able to connect. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
attribute | Text    | *None*        | **Required!** The name of an LDAP attribute that must be set on a user.
value     | Text    | *None*        | **Required!** The value of an LDAP attribute that must be set on a user.

##### Example Usage

```xml
<ldaprequire attribute="ou"
             value="People">
```

#### `<ldapwhitelist>`

The `<ldapwhitelist>` tag defines CIDR ranges which are exempt from the authentication requirement. This tag can only be defined once.

Name | Type    | Default Value | Description
---- | ------- | ------------- | -----------
cidr | Text    | *None*        | **Required!** A CIDR range which is exempt from the authentication requirement.

##### Example Usage

```xml
<ldapwhitelist cidr="127.0.0.0/8">
```