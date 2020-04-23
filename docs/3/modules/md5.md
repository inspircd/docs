---
title: Module Details: md5 (v3)
---

## The "md5" Module

### Description

This module allows other modules to generate [MD5](https://en.wikipedia.org/wiki/MD5) hashes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="md5">
```

This module requires no other configuration.

### Special Notes

MD5 is widely considered insecure and should not be used for hashing passwords. You should use hmac-sha256 for this purpose instead (requires [the password_hash module](/3/modules/password_hash) and [the sha256 module](/3/modules/sha256)).
