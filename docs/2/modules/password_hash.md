---
title: Module Details (password_hash)
---

## The "password_hash" Module

### Description

This module adds the `/MKPASSWD` command which allows the generation of hashed passwords for use in the server configuration.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_password_hash.so">
```

This module requires no other configuration.

### Commands

Name     | Parameter Count | Syntax              | Description
-------- | --------------- | ------------------- | -----------
MKPASSWD | 1               | `<hash> <password>` | Hashes `<password>` using the `<hash>` algorithm.

{! 2/modules/_hash_table.md !}

#### Example Usage

Hashes the password "hunter2" using the HMAC-SHA-256 algorithm:

```plaintext
/MKPASSWD hmac-sha256 hunter2
```

### Special Notes

You should only run this command on a server that you trust as the plaintext password may be intercepted by an attacker.
