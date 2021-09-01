---
title: v4 Change Log
---

{! 4/_support.md !}

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 4.0.0a4

**This pre-release version of InspIRCd was released on 2021-09-01.**

- `/SQUERY` is now unicast to the target service instead of being routed as a `/PRIVMSG`.

- `<oper:autologin>` now always respects the host field when set to `yes` like `if-host-match` from v3.

- Added `<admin:description>` for the second line of the `/ADMIN` output.

- Added `<limits:maxkey>` for configuring the maximum key length.

- Added support to `/CHECK` for finding users by an ident or real name mask.

- Changed the real ip/host field from `RPL_WHOISHOST` to `RPL_WHOISACTUALLY`.

- Changed the second line of `/ADMIN` to be optional instead of the first.

- Merged `<admin:nick>` with `<admin:name>`.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Removed usage of some deprecated OpenSSL APIs.

### InspIRCd 4.0.0a3

**This pre-release version of InspIRCd was released on 2021-08-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- The default value for `<limits:maxchan>` has been changed to 60.

- The default value for `<limits:maxkick>` has been changed to 130.

- The default value for `<limits:maxquit>` has been changed to 300.

- The default value for `<limits:maxreal>` has been changed to 130.

- The default value for `<limits:maxtopic>` has been changed to 330.

### InspIRCd 4.0.0a2

**This pre-release version of InspIRCd was released on 2021-07-01.**

- Fixed `<security:hideserver>` being able to be set to an invalid hostname.

- Fixed building on Haiku.

- Fixed building on Windows.

- Fixed local idle times being incorrect.

- Fixed module events not being fired correctly.

- Fixed WHOIS numerics not including the source of the message.

- Imported the opmoderated module from inspircd-contrib.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Refactored the compiler and linker flag logic in the makefile.

### InspIRCd 4.0.0a1

**This pre-release version of InspIRCd was released on 2021-06-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Added support for case insensitive regular expressions.

- Added support for fake honeypot channels to the securelist module.

- Added support for multi-line command syntax messages.

- Added support for named (i.e. `foo:n!u@h`) and inverted (i.e. `!f:n!u@h`) extbans.

- Added support for network-synchronised metadata on channel memberships.

- Added support for reloading TLS certificates as part of a normal rehash.

- Added support for sending 005 diffs when the server module state changes

- Added support for the sha224, sha384, and sha512 hash algorithms.

- Added the `servers/ignore-securelist` privilege to allow server operators to ignore the securelist module.

- Changed modules to use native platform file extensions (i.e. `.dylib` on macOS and `.dll` on Windows).

- Enabled the regex_stdlib module by default on all systems.

- Fixed losing the set time and setter of list modes when linking servers.
