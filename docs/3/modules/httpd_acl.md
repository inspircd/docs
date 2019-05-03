---
title: Module Details (httpd_acl)
---

## The "httpd_acl" Module

### Description

This module allows the server administrator to control who can access resources served over HTTP with [the httpd module](/3/modules/httpd).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="httpd_acl">
```

#### `<httpdacl>`

The `<httpdacl>` tag defines settings about how the httpd_acl module should behave. This tag can only be defined once.

Name      | Type | Default Value | Description
--------- | ---- | ------------- | -----------
path      | Text | *None*        | **Required!** The path to protect with this ACL rule.
types     | Text | *None*        | **Required!** A comma-delimited list of types which apply to this ACL rule.
blacklist | Text | *None*        | **Required for the blacklist type!** A comma-delimited list of IP addresses to deny access to this path from.
password  | Text | *None*        | **Required for the password type!** The password that HTTP connections must provide with their request.
username  | Text | *None*        | **Required for the password type!** The username that HTTP connections must provide with their request.
whitelist | Text | *None*        | **Required for the blacklist type!** A comma-delimited list of IP addresses to allow access to this path from.

The types field should be set to one or more of the following values:

Value     | Description
--------- | -----------
blacklist | Deny connections from the specified IP addresses.
password  | Require connections to provide the specified username and password.
whitelist | Allow connections from the specified IP addresses.

##### Example Usage

Denies access to the /stats\* path from 192.0.2.\* and 192.198.51.100.\*:

```xml
<httpdacl path="/stats*"
          types="blacklist"
          blacklist="192.0.2.*,192.198.51.100.*">
```

Only allows access to the /config\* path from 203.0.113.\*:

```xml
<httpdacl path="/config*"
          types="whitelist"
          whitelist="203.0.113.*">
```

Requires requests to provide the username "inspircd" and password "correct horse battery staple":

```xml
<httpdacl path="/*"
          types="password"
          username="inspircd"
          password="correct horse battery staple">
```
