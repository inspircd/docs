---
title: Modules moved to Module Manager in v5
---

## Modules moved to Module Manager

Occasionally we move modules that previously shipped with the previous major version of InspIRCd to the Module Manager. This is usually because they are obsolete or because they have other problems but they are made available to allow networks that need to keep compatibility with an older branch.

These modules will not be updated to the next major version of InspIRCd. If you wish to take over maintainership of one of these modules feel free to send a pull request updating the `ModAuthor` directive to your name and email address.

## Modules moved in v4

### banredirect

This module uses complicated ban parsing that does not work with extended bans. Its behaviour has been replaced with extended ban `d:` (redirect) from the redirect module which will automatically rewrite banredirect bans into extended bans.

### cloak_md5

This module was deprecated in v4 as it relies on insecure cryptography and, in the case of the half cloaking method, can be bypassed by anyone who is capable of doing IPv4 enumeration over at the most 65,536 addresses. There shouldn't be a use to need this anymore. All users should migrate to the cloak_sha256 module.

### customtitle

This module has been replaced by the newly rewritten swhois module. All users should migrate to the swhois module.

### hash_md5

This module was deprecated in v4 as it implements an obsolete hashing algorithm. It is extremely insecure to use this for passwords and the only other use (hash_md5) was also deprecated and moved to contrib in v5.

### starttls

IRCv3 has deprecated the `tls` capability [because of issues with opportunistic TLS](https://nostarttls.secvuln.info/) and recommends that people migrate to STS instead. You should load the ircv3_sts module instead.

### vhost

The behaviour of this module has been entirely replaced by the cloak_custom module only with the additional benefit of integrating with the cloaking system. You should load the cloak_custom module instead.
