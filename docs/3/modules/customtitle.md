---
title: Module Details (customtitle)
---

## The "customtitle" Module

### Description

This module allows the server administrator to define accounts which can grant a custom title in `/WHOIS` and an optional virtual host.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="customtitle">
```

#### `<customtitle>`

The `<customtitle>` tag defines a title account. This tag can be defined as many times as required.

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
name     | Text | *None*        | **Required!** The username used when logging into the account.
password | Text | *None*        | **Required!** The password used when logging into the account.
hash     | Text | *None*        | The algorithm that the password is hashed with.
host     | Text | \*@\*         | A glob pattern for the user@host mask of users that can log into this account.
title    | Text | *None*        | **Required!** The custom title shown in `/WHOIS` for users who log into this account.
vhost    | Text | *None*        | The vhost for users who log into this account.

{! 3/modules/_hash_table.md !}

##### Example Usage

Adds a title account with the username Sadie and a hashed password:

```xml
<title name="Sadie"
       password="Ohf74jA8$GwQ083Z/Jl2Vi6WpYKu2ABTU5HAKO+Zk8NWw7sdt7cQ"
       hash="hmac-sha256"
       host="*@*.example.com"
       title="is an Example-Net Helper"
       vhost="helper.example.com">
```

### Commands

Name  | Parameter Count | Syntax                  | Description
----- | --------------- | ----------------------- | -----------
TITLE | 2               | `<username> <password>` | Log into the account with the specified username and password.

#### Example Usage

Logs into the account with the name Sadie and password fl00fyc4pyb4r4:

```plaintext
/TITLE Sadie fl00fyc4pyb4r4
```
