---
title: v5 Change Log
---

{! 5/_support.md !}

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 5.0.0dev2

<!-- TODO: ensure changes after commit 448c43477189e575e0d288fa04427992bba85bb7 are added to this list before release. -->

**This development snapshot version of InspIRCd has not yet been released.**

- Added spanningtree server protocol 1207.

- Added support for not propagating X-lines.

- Added support for using extbans with the `/SILENCE` command.

- Added the join time to channel memberships.

- Merged all of the changes from the v4 development branch into the v5 development branch.

- Modularised user I/O handling and moved socket user I/O handling from the core to the core_clients module.

- Moved the `<security:maphide>` configuration tag to `<maphide:url>`.

- Moved the `customtitle` module to inspircd-contrib.

- Removed K-lines in favour of local G-lines.

- Removed the `<sslinfo:welcomemsg>` setting with no replacement (now always disabled).

- Removed the u_ prefix from the names of channel mode `C` (noctcp), `r` (registered), and `S` (stripcolor).

- Renamed user mode `z` (sslqueries) to sslonly.

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
