---
title: v4 Modules moved to Module Manager
---

## Modules moved to Module Manager

Occasionally we move modules that previously shipped with the previous major version of InspIRCd to [the Module Manager](/4/module-manager). This is usually because they are obsolete or because they have other problems but they are made available to allow networks that need to keep compatibility with an older branch.

These modules will not be updated to the next major version of InspIRCd. If you wish to take over maintainership of one of these modules feel free to send a pull request updating the `ModAuthor` directive to your name and email address.

## Modules moved in v4

### censor

This module is trivial to bypass as it only provides basic text matching. It also requires config accesss to add or remove entries. It is recommended that you migrate to [the filter module](/4/modules/filter) for server-wide message blocking using regular expressions. You might also find [the chanfilter](/4/modules/chanfilter) module useful to allow channels to configure their own filtered messages using glob patterns.

### clones

This module was intended for finding clones used for flooding but the way malicious bots work nowadays is by using masses of infected proxy hosts which don't share the same IP. It also didn't provide any other information about the clone subnets which isn't very useful.

### hostchange

This module is obsolete thanks to the new v4 cloaking system which implements the same behaviour. It also only applies hostnames on connect which means that hostnames are not updated on change and non-SASL account logins will not result in a hostname change. Users of this module should consider migrating to [the cloak_user module](/4/modules/cloak_user) if they use the "addaccount" or "addnick" actions and [the cloak_static module](/4/modules/cloak_static) if they use the "set" action.

### lockserv

This module is extremely niche and there's not really any circumstances in which it would be useful. If disabling a server due to planned updates you are a lot better off removing it from your DNS round robin and waiting for it to empty.

### modenotice

This module is extremely niche as there's not really any circumstances in which you would want to send messages to users with a specific user mode set other than wallops [which has its own command](/4/commands#wallops-message). It mostly existed in v3 for compatibility with v2 when it was a core command.

### protoctl

This module was not included with v3 but provides support for an obsolete protocol negotiation system which was previously implemented by [the multiprefix module](/4/modules/multiprefix) and [the uhnames modules](/4/modules/uhnames). It should not be necessary for modern clients which implement support for IRCv3 Capability Negotiation.

### regex_pcre

This module depends on PCRE which [is no longer maintained by its author](https://lists.exim.org/lurker/message/20210615.162400.c16ff8a3.en.html). The author's recommendation is that you should migrate to PCRE2. Support for the newer PCRE2 library is provided by [the regex_pcre2 module](/4/modules/regex_pcre2) which provides a regular expression engine with the same internal name so it shouild be a drop-in replacement.

### regex_tre

This module depends on TRE library which is less commonly used. The main benefit of it was that it has time and memory consumption linear to the size of the input but this is a feature also provided by more widely used RE2 library as provided by [the regex_re2 module](/4/modules/regex_re2).

### ssl_mbedtls

This module was never really feature complete to the same level as the ssl_gnutls and ssl_openssl modules. Most notably it never gained SNI support or support for SPKI fingerprints. Additionally, the current mbedTLS maintainers have also broken C++ support multiple times (e.g. mbedTLS bugs #7087 and #8866) and relicensed the library from GPLv2 to the Apache License which means we can no longer ship binaries linked against it. Considering these factors it was decided to remove the module. Users are recommended to migrate to [the ssl_gnutls module](/4/modules/ssl_gnutls).

### userip

This module provides more or less the same information as [the check module](/4/modules/check) but in a less useful way. It is recommended that you migrate to [the check module](/4/modules/check).
