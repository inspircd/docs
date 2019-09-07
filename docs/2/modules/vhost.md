---
title: Module Details (vhost)
---

{! 2/_support.md !}

## The "vhost" Module

### Description

This module allows the server administrator to define accounts which can grant a custom virtual host.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_vhost.so">
```

#### `<vhost>`

The `<vhost>` tag defines a virtual host account. This tag can be defined as many times as required.

Name | Type | Default Value | Description
---- | ---- | ------------- | -----------
user | Text | *None*        | **Required!** The username used when logging into the account.
pass | Text | *None*        | **Required!** The password used when logging into the account.
hash | Text | *None*        | The algorithm that the password is hashed with.
host | Text | *None*        | The vhost for users who log into this account.

{! 2/modules/_hash_table.md !}

##### Example Usage

Adds a virtual host account with the username Sadie and a hashed password:

```xml
<vhost user="Sadie"
       pass="Ohf74jA8$GwQ083Z/Jl2Vi6WpYKu2ABTU5HAKO+Zk8NWw7sdt7cQ"
       hash="hmac-sha256"
       host="helper.example.com">
```

### Commands

Name  | Parameter Count | Syntax                  | Description
----- | --------------- | ----------------------- | -----------
VHOST | 2               | `<username> <password>` | Log into the account with the specified username and password.

#### Example Usage

Logs into the account with the name Sadie and password fl00fyc4pyb4r4:

```plaintext
/VHOST Sadie fl00fyc4pyb4r4
```
