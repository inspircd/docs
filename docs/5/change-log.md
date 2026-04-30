---
title: v5 Change Log
---

<!--
TODO: create the pages that link to these:

[.](/5/moved-modules)
-->

{! 5/_support.md !}

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 5.0.0dev4

**This development snapshot version of InspIRCd was released on 2026-05-01.**

* Added a new interactive Python configure script that invokes CMake.

* Changed from a hand-made build system to using CMake on all platforms.

* Changed the Windows compatibility layer to build as a static library that is then linked into the core.

* Changed vendored libraries to be built as static libraries which then get linked to the appropriate modules.

* Developer: Added utility methods for finding pointer elements in a container.

* Developer: Changed `ListExtItem` to allow custom encoding for each list element.

* Developer: Moved various remaining methods from the stdalgo header to a new container utility header.

* Developer: Removed the type field from I/O hooks.

* Developer: Rewrote the internal TLS interface.

* Fixed some compiler warnings on CHERI systems like Arm Morello.

* Increased the amount of information in the long-form `/SSLINFO` output.

* Increased the security of TLS server links by either requiring a CA-validated certificate or a self-signed certificate with a pinned fingerprint.

* Moved enabling and disabling extra modules to the new Module Manager.

* Moved installed contrib modules to their own sub-directory.

* Replaced the `ssl_cert` metadata with the new `tls-cert` metadata.

* Rewrote the Module Manager from scratch in Python.

### InspIRCd 5.0.0dev3

**This development snapshot version of InspIRCd was released on 2026-04-01.**

- Added an optional target nickname parameter to the `/SETHOST`, `/SETIDENT`, and `/SETNAME` commands.

- Added methods for encoding and decoding individual elements to `ListExtItem`.

- Added support for configuring per-command target limits using the `<maxlimits>` tag.

- Added support for resending ISUPPORT entries when a server operator's config gives them different limits.

- Added the time the server configuration was read to the output of the `httpd_stats` module.

- Changed the `sasl` module to rely on the `services` module for determining the services server.

- Changed the contributor list in `/INFO` to be automatically generated from Git.

- Converted the `abbreviation` and `uninvite` module to use standard replies instead of InspIRCd-specific numerics.

- Converted the `cban`, `dnsbl`, `gateway`, `rline`, `shun`, `sethost`, `setident`, and `setname` modules to use standard replies instead of server notices.

- Developer: Added support for checking if a user matches any list mode entry instead of just a ban.

- Developer: Changed extensions to use `std::shared_ptr<>` instead of raw pointers.

- Developer: Changed modules to use `std::shared_ptr<>` instead of `reference<>`.

- Developer: Converted the `IS_*` free functions to `Is*` and `As*` member functions.

- Developer: Redesigned the internal service system to treat all services the same and split the service type from the name.

- Developer: Rewrote the mkauthors tool from Perl to Python.

- Merged all of the changes from the v4 development branch into the v5 development branch.

- Moved channel settings from `<options>` and `<security>` to `<channels>`.

- Moved the `banredirect` module to inspircd-contrib as it is obsolete now the `redirect` module can handle ban redirects.

- Moved translation of command paramerers from the core to the spanningtree module.

- Removed the `chghost`, `chgident`, and `chgname` modules as their functionality has been merged into the `sethost`, `setident`, and `setname` modules respectively.

- Reworked how IRC case-insensitive strings are casemapped.

### InspIRCd 5.0.0dev2

**This development snapshot version of InspIRCd was released on 2026-03-01.**

- Added spanningtree server protocol 1207.

- Added support for networking standard replies.

- Added support for not propagating X-lines.

- Added support for per-command maximum targets.

- Added support for using extbans with the `/SILENCE` command.

- Added the join time to channel memberships.

- Cleaned up `ERR_NOPRIVILEGES` messages.

- Merged all of the changes from the v4 development branch into the v5 development branch.

- Modularised user I/O handling and moved socket user I/O handling from the core to the core_clients module.

- Moved support for sending standard replies to the core.

- Moved the `<security:maphide>` configuration tag to `<maphide:url>`.

- Moved the `customtitle` module to inspircd-contrib.

- Removed K-lines in favour of local G-lines.

- Removed the `<sslinfo:welcomemsg>` setting with no replacement (now always disabled).

- Removed the c_ prefix from the name of channel mode `r` (registered).

- Removed the u_ prefix from the names of user mode `C` (noctcp), `r` (registered), and `S` (stripcolor).

- Renamed user mode `z` (sslqueries) to sslonly.

- Rewrote the `sajoin`, `sakick`, `samode`, `sanick`, `sapart`, `saquit`, and `satopic` modules from
scratch and merged into one `sacommands` module.

- Rewrote the `swhois` module from scratch with support for multiple swhois entries.

### InspIRCd 5.0.0dev1

**This development snapshot version of InspIRCd was released on 2025-08-01.**

- Added `<cloak:username>` for cloak_user cloaks to allow assigning a static username.

- Added `<security:banrealmask>` to allow disabling matching bans against user's real username, hostname, and IP address.

- Added support for services clearing all nickname reservations with `SVSHOLD`.

- Added support for services only removing bans against visible masks with `SVSCMODE`.

- Added support for usernames to the cloaking system.

- Added the "geolocation" module rehash type to the `geo_maxmind` module to allow reloading the Geolocation database without a full rehash.

- Added the `cloak_custom` module that integrates with the cloaking system replaces both the `vhost` module and allows services to apply vhosts to users in a way that integrates with cloaking.

- Added the `DISABLEDMODES` token to ISupport to allow clients to hide mode buttons for disabled modes.

- Changed the default for `<options:extbanformat>` from any to name.

- Changed the default for `<servicesintegration:disablemodes>` from no to yes.

- Config compatibility code for v3 has been removed.

- Moved `<security:customversion>` to `<options:customversion>`.

- Moved modules to their own top-level directory.

- Moved password checking from the core to the hashing modules.

- Moved the `cloak_md5` module to inspircd-contrib.

- Moved the `log_json` module out of extras.

- Moved the `md5` module to inspircd-contrib.

- Moved the `spanningtree` configuration from `<options>`, `<performance>`, and `<security>` to the `<spanningtree>` tag.

- Moved the `starttls` module to inspircd-contrib.

- Raised the minimum version of C++ to C++20.

- Raised the minimum version of GnuTLS from 3.3.5 to 3.6.0.

- Raised the minimum version of OpenSSL from 1.1.1 to 3.0.0.

- Removed `<cloak:enforcepsl>` for cloak_sha256 (now always enabled).

- Removed `<filteropts:enableflags>` (now always enabled).

- Removed `<messageflood:extended>` (now always enabled).

- Removed `<permchanneldb:writeversion>` (now always set to 2).

- Removed `<repeat:extended>` (now always enabled).

- Removed `<rline:useflags>` (now always enabled).

- Removed `<sslprofile:dhfile>` (this was already ignored on the library versions we now support).

- Removed support for bitmask-style DNSBL configurations (these are uncommon and are almost always misused).

- Removed support for in-query password comparison in sqlauth (this only ever worked with insecure algorithms).

- Removed support for the 1205 (v3) server protocol.

- Removed the deprecated `$ip` and `$ident` values for user SQL queries.

- Removed the requirement to have the `password_hash` module loaded to use HMAC passwords.

- Renamed the `sslrehashsignal` module to `rehashsignal` and added support for custom module rehashes.

- Replaced the Perl `inspircd-testssl` script with the Python `inspircd-test-tls` script.

- Rewrote all hashing modules and renamed them to have a "hash_" prefix.

- Rewrote all of the hashing modules from scratch with a new interface and runtime checks.

- Vendored yyjson instead of relying on an external copy.
