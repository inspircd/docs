---
title: v4 Change Log
---

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 4.1.0

**This version of InspIRCd was released on 2024-07-14.**

- Added support for retrieving random data using `getentropy()` from POSIX 2024.

- Added the `%dnsbl.url`, `%network%`, and `%network.url` template variables to the DNSBL reason field.

- Allowed `/ACCEPT` to bypass more message restriction user modes.

- Changed system version functions to use `/etc/os-release` instead of `lsb_release`.

- Developer: const corrected various APIs.

- Fixed a memory leak in the regex_pcre2 module.

- Fixed building the core with PIE.

- Fixed high CPU and network usage caused by rebursting the account nick list.

- Fixed mistakenly allowing $ModConfig directives to use build system functions.

- Fixed mistakenly skipping empty lines in MOTD files.

- Fixed unregistering extbans when a module unloads.

- Merged the build time compiler validation checks.

- Modernized the AppArmor configuration file.

- Reduced the memory usage of the geo_maxmind module.

- Reduced unnecessary allocations in `ListExtItem`.

- Updated the package directives to support more distributions.

### InspIRCd 4.0.1

**This version of InspIRCd was released on 2024-07-03.**

- [Fixed a **crash** in the spanningtree module](/security/2024-01).

- Fixed the passforward module unnecessarily looking up connect class passwords from the config.

- Fixed various minor documentation issues.

- Updated the example tables for the sqloper module to include all core fields.

- Updated the log_sql tables to use non-null columns.

- Updated the vendored libraries.

### InspIRCd 4.0.0

**This version of InspIRCd was released on 2024-06-29.**

Please see [the overview](/4/overview) for an high level list of changes and [the breaking changes list](/4/breaking-changes) for a list of incompatibilities with v3.

You may also be interested in [the v4 development change log](/4/change-log-dev) for the changes that happened between development releases.
