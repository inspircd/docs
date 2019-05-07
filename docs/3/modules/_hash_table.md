<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

The following hashing modules are included with InspIRCd:

Algorithm          | Module(s)                                                              | Description
------------------ | ---------------------------------------------------------------------- | -----------
bcrypt             | [bcrypt](/3/modules/bcrypt)                                            | Hashes using the [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm.
hmac-md5           | [password_hash](/3/modules/password_hash), [md5](/3/modules/md5)       | Hashes using the [MD5](https://en.wikipedia.org/wiki/MD5) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
hmac-sha1          | [password_hash](/3/modules/password_hash), [sha1](/3/modules/sha1)     | Hashes using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
hmac-sha256        | [password_hash](/3/modules/password_hash), [sha256](/3/modules/sha256) | Hashes using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
md5                | [md5](/3/modules/md5)                                                  | Hashes using the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm.
pbkdf2-hmac-md5    | [pbkdf2](/3/modules/pbkdf2), [md5](/3/modules/md5)                     | Hashes using the [MD5](https://en.wikipedia.org/wiki/MD5) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
pbkdf2-hmac-sha1   | [pbkdf2](/3/modules/pbkdf2), [sha1](/3/modules/sha1)                   | Hashes using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
pbkdf2-hmac-sha256 | [pbkdf2](/3/modules/pbkdf2), [sha256](/3/modules/sha256)               | Hashes using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
sha256             | [sha256](/3/modules/sha256)                                            | Hashes using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) algorithm.
sha1               | [sha1](/3/modules/sha1)                                                | Hashes using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) algorithm.
