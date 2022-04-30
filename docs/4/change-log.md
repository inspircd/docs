---
title: v4 Change Log
---

{! 4/_support.md !}

## Change Log

This page lists changes which have happened between releases.

# InspIRCd 4.0.0a10

**This pre-release version of InspIRCd was released on 2022-05-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Added `<options:extbanformat>` to allow specifying the format to normalise extbans to.

- Added support for cleaning up malformed extban values.

- Added support for detecting the local hostname on Windows.

- Added support for UNIX socket listeners on Windows.

- Added support for writing a pid file on Windows.

- Cleaned up unnecessary inclusion of system header files.

- Improved cleaning up broken masks specified by users.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Removed support for automatically tidying list mode entries.

- Removed support for changing `<pid:file>` after the server has started.

- Removed validation of list mode entries that were set by a remote server.

- Replaced the command line argument parser with a more user friendly one.

### InspIRCd 4.0.0a9

**This pre-release version of InspIRCd was released on 2022-04-01.**

- Added support for numeric mode characters.

- Changed end of list numerics to be automatically generated based on the mode name.

- Fixed disabled commands being shown in `/COMMANDS`.

- Increased the minimum customprefix rank from 0 to 1.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Refactored the opermodes module.

### InspIRCd 4.0.0a8

**This pre-release version of InspIRCd was released on 2022-02-01.**

- Add support for connect class-specific 005 numerics.

- Developer: Kill vendor_directory in favour of adding the vendor directory to the include path.

- Developer: Refactored exception handling classes.

- Developer: Replaced consolecolors with the vendored rang library.

- Fix an infinite synchronisation loop with automatically synchronised extensibles.

- Fix extensibles being synchronisable when they are marked as non-synchronisable.

- Fix extensions being able to be set on the wrong type of extensible.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Moved DNS stats from the core to core_dns.

- Removed the nationalchars module.

- Replace the inlined md5 implementation with the vendored md5 library.

### InspIRCd 4.0.0a7

**This pre-release version of InspIRCd was released on 2021-12-15.**

- Added snomask `r` (REHASH) and moved all rehash messages to it.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Reject config files from ancient outdated tutorials.

- Removed support for remote `/INFO`.

### InspIRCd 4.0.0a6

**This pre-release version of InspIRCd was released on 2021-11-15.**

- Developer: Added support for specifying multiple `ModAuthor` directives in contrib modules.

- Developer: Removed support for `ModAuthorMail` in contrib modules.

- Developer: Removed the `time_t TIME` field from the `Tick()` method of timer classes.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Removed the old regex_pcre module that uses the PCRE1 library.

- Renamed regex_pcre2 to regex_pcre to replace the now removed PCRE1 module.

### InspIRCd 4.0.0a5

**This pre-release version of InspIRCd was released on 2021-10-01.**

- Added the FRHOST S2S command to change the real hostname of a remote user.

- Added the regex_pcre2 module which implements a regex engine that uses the PCRE2 library.

- Changed the operlog module to use the oper snomask instead of its own snomask.

- Fixed sending standard replies with variable parameters.

- Merged all of the changes from the v3 development branch into the v4 development branch.

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
