---
title: Module Details (ldapauth)
---

## The "ldapauth" Module

<div class="alert alert-info" role="alert" markdown="1">

This module depends on a third-party library ([OpenLDAP](https://www.openldap.org)) and must be manually enabled at compile time.

Once you have installed the dependency you can enable this module using the following command:

```sh
./configure --enable-extras=m_ldapauth.cpp
```

</div>

### Description

This module allows connecting users to be authenticated against an LDAP database.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_ldapauth.so">
```

#### `<ldapauth>`

The `<ldapauth>` tag defines settings about how the ldapauth module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
allowpattern | Text    | *None*        | If defined then a glob pattern for nicknames that are exempted from the authentication requirement.
attribute    | Text    | *None*        | **Required!** The attribute which is used to locate an account by name. On POSIX systems this is usually "uid".
baserdn      | Text    | *None*        | **Required!** The base Distinguished Name to search in for users.
bindauth     | Text    | *None*        | **Required!** The password for the Distinguished Name specified in the binddn field.
binddn       | Text    | *None*        | **Required!** The Distinguished Name to bind to for searching,
host         | Text    | *None*        | If defined then the vhost to set on connecting users.
killreason   | Text    | *None*        | **Required!** The message to kill users that fail to authenticate with.
searchscope  | Text    | subtree       | The scope of the search for the LDAP entry.
server       | Text    | *None*        | **Required** The `ldaps://` or `ldap://` URL for your LDAP server.
userfield    | Boolean | No            | Whether to authenticate users against their username (ident) instead of their nick.
verbose      | Boolean | No            | Whether to log failed authentications to snomask `a` (local) and snomask `A` (remote).

The searchscope field should be set to one of the following values:

Value    | Description
-------- | -----------
base     | Search only the LDAP object itself.
onelevel | Search the LDAP object and its immediate children.
subtree  | Search the LDAP object and all descendants.

##### Example Usage

```xml
<ldapauth allowpattern="Guest*"
          attribute="uid"
          baserdn="ou=People,dc=example,dc=com"
          bindauth="secretpassword"
          binddn="cn=Manager,dc=example,dc=com"
          host="$cn.example.com"
          killreason="Access denied"
          searchscope="subtree"
          server="ldaps://ldap.example/com"
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