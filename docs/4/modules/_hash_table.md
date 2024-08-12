<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

The following hashing modules are included with InspIRCd:

Algorithm          | Module(s)                                                          | Description
------------------ | ------------------------------------------------------------------ | -----------
argon2d            | [argon2](/4/modules/argon2)                                        | Hashes using the [Argon2d](https://en.wikipedia.org/wiki/Argon2) algorithm.
argon2i            | [argon2](/4/modules/argon2)                                        | Hashes using the [Argon2i](https://en.wikipedia.org/wiki/Argon2) algorithm.
argon2id           | [argon2](/4/modules/argon2)                                        | Hashes using the [Argon2id](https://en.wikipedia.org/wiki/Argon2) algorithm.
bcrypt             | [bcrypt](/4/modules/bcrypt)                                        | Hashes using the [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm.
hmac-md5           | [password_hash](/4/modules/password_hash), [md5](/4/modules/md5)   | *Deprecated!* Hashes using the [MD5](https://en.wikipedia.org/wiki/MD5) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
hmac-sha1          | [password_hash](/4/modules/password_hash), [sha1](/4/modules/sha1) | Hashes using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
hmac-sha224        | [password_hash](/4/modules/password_hash), [sha2](/4/modules/sha2) | Hashes using the [SHA-224](https://en.wikipedia.org/wiki/SHA-2) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
hmac-sha256        | [password_hash](/4/modules/password_hash), [sha2](/4/modules/sha2) | Hashes using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
hmac-sha384        | [password_hash](/4/modules/password_hash), [sha2](/4/modules/sha2) | Hashes using the [SHA-384](https://en.wikipedia.org/wiki/SHA-2) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
hmac-sha512        | [password_hash](/4/modules/password_hash), [sha2](/4/modules/sha2) | Hashes using the [SHA-512](https://en.wikipedia.org/wiki/SHA-2) and [HMAC](https://en.wikipedia.org/wiki/HMAC) algorithms.
md5                | [md5](/4/modules/md5)                                              | *Deprecated!* Hashes using the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm.
pbkdf2-hmac-md5    | [pbkdf2](/4/modules/pbkdf2), [md5](/4/modules/md5)                 | *Deprecated!* Hashes using the [MD5](https://en.wikipedia.org/wiki/MD5) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
pbkdf2-hmac-sha1   | [pbkdf2](/4/modules/pbkdf2), [sha1](/4/modules/sha1)               | Hashes using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
pbkdf2-hmac-sha224 | [pbkdf2](/4/modules/pbkdf2), [sha2](/4/modules/sha2)               | Hashes using the [SHA-224](https://en.wikipedia.org/wiki/SHA-2) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
pbkdf2-hmac-sha256 | [pbkdf2](/4/modules/pbkdf2), [sha2](/4/modules/sha2)               | Hashes using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
pbkdf2-hmac-sha384 | [pbkdf2](/4/modules/pbkdf2), [sha2](/4/modules/sha2)               | Hashes using the [SHA-384](https://en.wikipedia.org/wiki/SHA-2) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
pbkdf2-hmac-sha512 | [pbkdf2](/4/modules/pbkdf2), [sha2](/4/modules/sha2)               | Hashes using the [SHA-512](https://en.wikipedia.org/wiki/SHA-2) and [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithms.
sha1               | [sha1](/4/modules/sha1)                                            | Hashes using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) algorithm.
sha224             | [sha2](/4/modules/sha2)                                            | Hashes using the [SHA-224](https://en.wikipedia.org/wiki/SHA-2) algorithm.
sha256             | [sha2](/4/modules/sha2)                                            | Hashes using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) algorithm.
sha384             | [sha2](/4/modules/sha2)                                            | Hashes using the [SHA-384](https://en.wikipedia.org/wiki/SHA-2) algorithm.
sha512             | [sha2](/4/modules/sha2)                                            | Hashes using the [SHA-512](https://en.wikipedia.org/wiki/SHA-2) algorithm.
