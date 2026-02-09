---
title: v4 Breaking Changes
---

## Breaking changes since InspIRCd 3

**NOTE** &mdash; This document only lists breaking changes between InspIRCd 3 and InspIRCd 4. There are many backwards compatible changes that have been made which are not listed in this document.

### System

- A compiler with C++17 support is now required to build InspIRCd. In practise this means you will need to use at least Clang 5, GCC 7, or MSVC 19.15.

- CMake 3.20+ is now required to build on Windows.

- Debian GNU/kFreeBSD is no longer supported. It is recommended that you switch to Debian GNU/Linux instead.

- GnuTLS 3.3.5+ is now required by the ssl_gnutls module.

- OpenSSL 1.1.1+ is now required by the ssl_openssl module.

- Perl 5.26+ is now required by `./configure` and all of the included Perl tools.

- Windows 10 April 2018 Update is now the minimum supported version of Windows.

### Modules

- The blockcaps module has been removed. If you wish to keep this behaviour then you should load the anticaps module instead. See the documentation in modules.example.conf for more details.

- The censor module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration or run `./modulemanager install censor` to install it.

- The clones module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration or run `./modulemanager install clones` to install it.

- The flashpolicyd module has been removed with no replacement. This module is no longer needed as [Flash Player has been retired by Adobe](https://web.archive.org/web/20170801000737/https://blogs.adobe.com/conversations/2017/07/adobe-flash-update.html).

- The hostchange module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration, run `./modulemanager install hostchange` to install it, or migrate to the [`cloak_static`](/4/modules/cloak_static) module and/or the [`cloak_user`](/4/modules/cloak_user) module.

- The lockserv module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration or run `./modulemanager install lockserv` to install it.

- The modenotice module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration or run `./modulemanager install modenotice` to install it.

- The nationalchars module has been removed. In order to upgrade you should migrate to [the codepage module](/4/modules/codepage).

- The nopartmsg module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration, run `./modulemanager install nopartmsg` to install it, or migrate to [the muteban module](/4/modules/muteban) which now also applies to part messages.

- The regex_pcre module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration, run `./modulemanager install regex_pcre` to install it, or migrate to [the regex_pcre2 module](/4/modules/regex_pcre2) which also provides the "pcre" regex engine so it should be a drop-in replacement.

- The ssl_mbedtls module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration, run `./modulemanager install ssl_mbedtls` to install it, or migrate to either [the ssl_gnutls module](/4/modules/ssl_gnutls) or [the ssl_openssl module](/4/modules/ssl_openssl).

- The userip module has been [moved to inspircd-contrib](/4/moved-modules). In order to upgrade either remove this module from your configuration, run `./modulemanager install userip` to install it, or migrate to [the check module](/4/modules/check).

### Config

- `<bind:ssl>` has been moved to `<bind:sslprofile>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<cban:glob>` has been removed with no replacement (now always enabled).

- `<cgiirc:opernotice>` has been removed. If you wish to keep this behaviour you can use server operator snomask privileges instead.

- `<chanhistory:enableumode>` has been removed with no replacement (now always enabled).

- `<channels:opers>` has been removed. If you wish to keep this behaviour then set `<oper:maxchans>` or `<type:maxchans>` instead. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<channels:users>` has been removed. If you wish to keep this behaviour then set `<connect:maxchans>` instead. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<class:snomasks>` no longer has a default value. In order to keep v3 behaviour you should set it to `*`.

- `<commonchans:invite>` has been removed with no replacement (now always enabled).

- `<config:format>` has been removed with no replacement. If you were previously using compat-style config parsing you will have to go through your config and replace all C-style escape sequences with XML-style escape sequences.

- `<connectban:duration>` has been moved to `<connectban:banduration>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<deaf:enableprivdeaf>` has been removed with no replacement (now always enabled).

- `<disabled:fakenonexistant>` has been moved to `<disabled:fakenonexistent>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<exemptfromfilter:channel>` has been moved to `<exemptfromfilter:target>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<gnutls>` has been removed (other than `<gnutls:onrehash>`). You should configure a TLS profile instead.

- `<httpstats:enableparams>` has been removed with no replacement (now always enabled).

- `<limits:maxgecos>` has been moved to `<limits:maxreal>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<link:ssl>` has been moved to `<link:sslprofile>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<noctcp:enableumode>` has been removed with no replacement (now always enabled).

- `<openssl>` has been removed (other than `<openssl:onrehash>`). You should configure a TLS profile instead.

- `<oper:autologin>` must now be set to "relaxed" or "strict" instead of "yes". To keep v3 behaviour you should set it to "relaxed".

- `<options:allowzerolimit>` has been removed with no replacement (now always disabled).

- `<options:casemapping>` has been removed with no replacement (ascii casemapping is now the only core option).

- `<options:moronbanner>` has been moved to `<options:xlinemessage>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<override:enableumode>` has been removed with no replacement (now always enabled).

- `<power>` has been removed. If you wish to keep this behaviour you can use server operator command privileges instead.

- `<repeat:maxsecs>` has been moved to `<repeat:maxtime>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<security:allowcoreunload>` has been removed with no replacement (now always disabled).

- `<security:hidewhois>` has been moved to `<security:hideserver>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<showwhois:showfromopers>` has been removed. If you wish to make a server operator immune from this mode then give them the `users/secret-whois` privilege.

- `<shun:affectsopers>` has been removed. If you wish to keep this behaviour then give your server operators the `servers/ignore-shuns` privilege.

- `<sslmodes:enableumode>` has been removed with no replacement (now always enabled).

- `<svshold:silent>` has been removed with no replacement (now always enabled).

- Several example files have been renamed. If you are including them without modification you will need to update your include files to point to their new names.

- The syntax of the passforward module's command fields has changed. You should switch your config to use the new style `%foo%` variables.

### Other

- Compatibility with the 1202 (v2) protocol has been removed. You will need to link against an intermediary v3 server if you are upgrading from v2 or are using an older services package that does not support the 1205 (v3) protocol.

- `inspircd-genssl` has been removed with no replacement. You should use a CA-validated certificate for your server rather than a self-signed one.

- The `/FPART` command has been removed. If you wish to keep this behaviour you should add an alias that calls the `/REMOVE` command.

- The `/PROTOCTL` command has been [moved to inspircd-contrib](/4/moved-modules). If you wish to keep this behaviour then you can run `./modulemanager install protoctl` to install it.
