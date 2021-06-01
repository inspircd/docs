---
title: v4 Breaking Changes
---

{! 4/_support.md !}

## Breaking changes since InspIRCd 3

NOTE: This document only lists breaking changes between InspIRCd 3 and InspIRCd 4. There are many backwards compatible changes that have been made which are not listed in this document.

## Moves

- `<disabled:fakenonexistant>` has been moved to `<disabled:fakenonexistent>`.

- `<exemptfromfilter:channel>` has been moved to `<exemptfromfilter:target>`.

- `<limits:maxgecos>` has been moved to `<limits:maxreal>`.

- `<options:moronbanner>` has been moved to `<options:xlinemessage>`.

- `<repeat:maxsecs>` has been moved to `<repeat:maxtime>`.

- `<security:hidewhois>` has been moved to `<security:hideserver>`.

- The censor module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_censor` to install it.

- The clones module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_clones` to install it.

- The lockserv module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_lockserv` to install it.

- The regex_tre module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_regex_tre` to install it.

## Removals

- Support for the 1202 (v2) protocol has been removed. You will need to link against an intermediary v3 server if you are upgrading from v2.

- The `<config:format>` option  has been removed. If you were previously using compat-style config parsing you will have to go through your config and replace all C-style escape sequences with XML-style escape sequences.

- The blockcaps module has been removed. If you wish to keep this behaviour then you should load the anticaps module instead. See the documentation in modules.conf.example for more details.

- The flashpolicyd module has been removed with no replacement. This module is no longer needed as [Flash Player has been retired by Adobe](https://blogs.adobe.com/conversations/2017/07/adobe-flash-update.html).

- `<channels:opers>` has been removed. If you wish to keep this behaviour then set `<oper:maxchans>` or `<type:maxchans>` instead.

- `<channels:users>` has been removed. If you wish to keep this behaviour then set `<connect:maxchans>` instead.

- `<deaf:enableprivdeaf>` has been removed with no replacement (now always enabled).

- `<noctcp:enableumode>` has been removed with no replacement (now always enabled).

- `<options:allowzerolimit>` has been removed with no replacement (now always disabled).

- `<options:casemapping>` has been removed with no replacement (ASCII casemapping is now the only option).

- `<override:enableumode>` has been removed with no replacement (now always enabled).

- `<security:allowcoreunload>` has been removed with no replacement (now always disabled).

- `<sslmodes:enableumode>` has been removed with no replacement (now always enabled).
