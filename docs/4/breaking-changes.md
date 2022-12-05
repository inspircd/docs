---
title: v4 Breaking Changes
---

{! 4/_support.md !}

## Breaking changes since InspIRCd 3

**NOTE** &mdash; This document only lists breaking changes between InspIRCd 3 and InspIRCd 4. There are many backwards compatible changes that have been made which are not listed in this document.

### System

- A compiler with C++17 support is now required to build InspIRCd. In practise this means you will need to use at least Clang 5, GCC 7, or MSVC 19.15.

- Debian GNU/kFreeBSD is no longer supported. It is recommended that you switch to Debian GNU/Linux instead.

- GnuTLS 3.3.5+ is now required by the ssl_gnutls module.

- OpenSSL 1.1.1+ is now required by the ssl_openssl module.

- PCRE2 is now required by the regex_pcre module. Most regular expressions should be compatible but if not you can use `./modulemanager install m_regex_oldpcre` to install the a module that uses the PCRE1 library.

- Perl 5.26+ is now required by `./configure` and all of the included Perl tools.

- Windows 10 build 17061 is now the minimum supported version of Windows.

### Modules

- The blockcaps module has been removed. If you wish to keep this behaviour then you should load the anticaps module instead. See the documentation in modules.conf.example for more details.

- The censor module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_censor` to install it.

- The clones module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_clones` to install it.

- The flashpolicyd module has been removed with no replacement. This module is no longer needed as [Flash Player has been retired by Adobe](https://web.archive.org/web/20170801000737/https://blogs.adobe.com/conversations/2017/07/adobe-flash-update.html).

- The lockserv module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_lockserv` to install it.

- The modenotice module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_modenotice` to install it.

- The nationalchars module has been removed. In order to upgrade you should switch to the codepage module instead.

- The regex_tre module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_regex_tre` to install it.

- The userip module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install userip` to install it.

### Config

- `<cban:glob>` has been removed with no replacement (now always enabled).

- `<cgiirc:opernotice>` has been removed. If you wish to keep this behaviour you can use server operator snomask privileges instead.

- `<chanhistory:enableumode>` has been removed with no replacement (now always enabled).

- `<channels:opers>` has been removed. If you wish to keep this behaviour then set `<oper:maxchans>` or `<type:maxchans>` instead.

- `<channels:users>` has been removed. If you wish to keep this behaviour then set `<connect:maxchans>` instead.

- `<class:snomasks>` no longer has a default value. In order to keep v3 behaviour you should set it to `*`.

- `<commonchans:invite>` has been removed with no replacement (now always enabled).

- `<config:format>` has been removed with no replacement. If you were previously using compat-style config parsing you will have to go through your config and replace all C-style escape sequences with XML-style escape sequences.

- `<connectban:duration>` has been moved to `<connectban:banduration>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<deaf:enableprivdeaf>` has been removed with no replacement (now always enabled).

- `<disabled:fakenonexistant>` has been moved to `<disabled:fakenonexistent>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<exemptfromfilter:channel>` has been moved to `<exemptfromfilter:target>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<gnutls>` has been removed. You should configure a TLS (SSL) profile instead.

- `<limits:maxgecos>` has been moved to `<limits:maxreal>`. This move originally happened in v3 so if you are using a v3 config you probably don't need to do anything.

- `<mbedtls>` has been removed. You should configure a TLS (SSL) profile instead.

- `<noctcp:enableumode>` has been removed with no replacement (now always enabled).

- `<openssl>` has been removed. You should configure a TLS (SSL) profile instead.

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

- The syntax of the passforward module's command fields has changed. You should switch your config to use the new style `%foo%` variables.

### Other

- Compatibility with the 1202 (v2) protocol has been removed. You will need to link against an intermediary v3 server if you are upgrading from v2.

- `inspircd-genssl` has been removed with no replacement. You should use a CA-validated certificate for your server rather than a self-signed one.

- The `/FPART` command has been removed. If you wish to keep this behaviour you should add an alias that calls the `/REMOVE` command.

- The `/PROTOCTL` command has been moved to inspircd-contrib. If you wish to keep this behaviour then you can run `./modulemanager install m_protoctl` to install it.
