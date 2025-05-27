---
title: v4 Change Log
---

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 4.8.0

**This version of InspIRCd was released on 2025-08-02.**

- Added `<sslprofile:securitylevel>` to the ssl_openssl module for setting the OpenSSL security level.

- Added an OpenRC init script to the scripts directory.

- Added support for building against system packages for vendored libraries.

- Added support for regex flags to the rline module.

- Changed --portable to imply --disable-ownership.

- Changed some config keys removed in v4 to hard error in order to help upgrading users.

- Developer: added a method to the DNS manager for getting the default timeout.

- Fixed a confusing error message from the sqlite3 moduile.

- Fixed a loop caused by logging from logger when using a module logger.

- Fixed configuring files with a junk group and user when configured with --disable-ownership.

- Fixed enforcing the use of the Public Suffix List in link data.

- Fixed link data being emitted with an empty value instead of no value.

- Fixed mapping the deprecated verbose log level to debug as intended.

- Fixed sorting the `/COMMANDS` output.

- Fixed the permissions of the launchd service plist.

- Fixed the system PSL database not being included in the AppArmor profile.

- Improved the performance of the `/COMMANDS` command.

- Updated the vendored libraries.

- Updated the Windows dependencies.

- Upgraded the Windows dependency system to use Conan 2.

### InspIRCd 4.7.0

**This version of InspIRCd was released on 2025-03-29.**

- [Fixed a **crash** when a server operator with a custom connect class quits.](/security/2025-01)

- Added extban names to help.example.conf.

- Added support for help channels in which users with user mode `h` (helpop) will be automatically granted a channel prefix mode.

- Added support to Module Manager for linking to module documentation on install.

- Added the `%duration.long%` and `%remaining.long%` template variables to `<options:xlinequit>` and `<security:publicxlinequit>`.

- Added the `SAFERATE` 005 token to allow modern clients (e.g. Soju) to know when fakelag is enabled and relax their internal message buffering.

- Changed various messages to use long duration strings (e.g. "1 day, 2 hours, 3 minutes") instead of short duration strings (e.g. 1d2h3m).

- Developer: added `Duration::ToLongString` to convert a duration to a format which is more readable.

- Developer: added a formatting overload of the `ModuleException` constructor.

- Developer: added constants to the `Time` namespace for commonly used time formats.

- Fixed flushing the standard output stream after startup when not forking into the background.

- Fixed help.example.conf to correctly list all current exemptions, extbans, and modes.

- Improved the performance of formatting various messages.

### InspIRCd 4.6.0

**This version of InspIRCd was released on 2025-03-01.**

- Added the `RPL_STATSCONN` numeric for compatibility with ircu.

- Added the creating user's IP address to the chancreate oper snotice.

- Added the real hostname and IP address of proxied WebSocket users to the whois output.

- Added the user's IP address and userhost to the seenicks oper snotice.

- Added the WebIRC origin name to the whois output.

- Changed the `/ALLTIME` command to use the RPL_TIME numeric instead of a notice.

- Changed the `/CBAN`, `/ELINE`, `/GLINE`, `/KLINE`, `/QLINE`, `/RLINE`, and `/ZLINE` commands to make the duration field optional (defaults to permanent).

- Changed the dnsbl module to default to the record type if not otherwise specified.

- Changed the httpd_stats module to pad base 64 output.

- Deprecated support for bitmask-type DNSBL entries.

- Fixed building the 005 numerics for users in removed connect classes.

- Fixed finding the config file on portable installations (i.e. Windows).

- Fixed linking against v3 servers when using the repeat module.

- Fixed removing regular bans that look like an extban.

- Fixed sending some rehash snotices to the announcement snomask character.

- Fixed showing the correct mask when removing an extended ban.

- Fixed the accuracy of human-readable durations when converting from the number of seconds.

- Fixed the list of exemptions in the help.

- Fixed the list of server notice masks.

- Fixed TLS fingerprint fallback in SASL when using Atheme.

- Improved the performance of the logging system.

- Improved the time format used in `RPL_TIME`.

- Optimised counting the local and global servers in `/LUSERS`.

- Removed obsolete snotices sent when a server operator specifies the wrong server name in `/DIE` and `/RESTART`.

- Updated the vendored libraries.

### InspIRCd 4.5.0

**This version of InspIRCd was released on 2025-01-04.**

- Added a "sslrehash" command to the helper script (requires the sslrehashsignal module).

- Added support for explicitly disabling the ojoin and operprefix characters.

- Fixed a compiler warning on BSD.

- Fixed a crash from {fmt} when writing the pid file fails.

- Fixed clearing the output buffer in the pgsql module.

- Fixed matching extended bans when multiple bans of a specific type are set.

- Fixed stripping multiple formatting codes in a row.

- Fixed various compiler warnings on Haiku.

- Improved the format of the RPL_CREATED numeric message.

- Updated the vendored libraries.

### InspIRCd 4.4.0

**This version of InspIRCd was released on 2024-11-02.**

- Added `<anticaps:message>` to allow customising the error shown when blocking an overly capitalised message.

- Added `<chanhistory:savefrombots>` to allow omitting messages from bots.

- Added `<hidechans:hideservices>` to allow showing the channel list of services pseudoclients to server operators.

- Added a `/STATS` character to the sslinfo module for viewing ciphersuite info.

- Added a faster method of converting values to a string for types that support it.

- Added advertisement of the preferred extban format for services.

- Added support for matching account bans against the entire nick group.

- Added support for name-only extended bans.

- Added support for named DNSBL replies and the `%reason%` variable in `<dnsbl:reason>`.

- Added support for regex flags to the filter module.

- Added the "opers" option to `<options:modesinlist>` to allow only showing modes to an operator with the `channels/auspex` privilege.

- Added the `%channel%` template variable to the messageflood and repeat error messages.

- Changed the ldap module to use the Windows API for parsing LDAP URLs.

- Changed the minimum value for `<connectban:threshold>` from 1 to 2.

- Developer: added `Time::FromNow` to convert a duration into a future timestamp.

- Developer: moved core numerics back to a global header again.

- Developer: switched several methods to take a string_view instead of a string.

- Fixed "no tags to send" errors on some clients when `<ctctags:allowclientonlytags>` is disabled.

- Fixed extbans silently overwriting extbans with the same character from other modules.

- Fixed potentially generating a malformed permchannels database.

- Fixed rebuilding the 004 numeric when core_info is reloaded.

- Fixed resending the 005 numerics when a user changes connect class.

- Fixed the connectban module potentially generating a Z-line on a malformed CIDR range.

- Fixed users not being removed from the services list when their server stops being a services server.

- Fixed warning users about raw I/O logging after a rehash when started with `--nolog`.

- Improved the restrictchans error message.

- Improved the xline_db log messages.

- Renamed `<chanhistory:bots>` to `<chanhistory:sendtobots>`.

- Reverted omission of services pseudoclients from the user count in `/LUSERS`.

- Updated the location of the InspIRCd IRC channels.

- Updated the Windows dependencies.

### InspIRCd 4.3.0

**This version of InspIRCd was released on 2024-09-07.**

- Added `<whowas:nickupdate>` to allow updating the whowas database on nick change as well as quit.

- Added support for building against yyjson to the log_json module.

- Added support for human readable colour names in MOTD files using `\c[fg-color,bg-color]`

- Added the `&dir.example;` config variable to make it easier to include example configs on system-wide installs.

- Changed command processing to check whether a command is usable before registration before the parameter count is checked .

- Changed the example `<define>` tags to be actually useful.

- Developer: added `InspIRCd::ProcessColors(std::string)` and deprecated the vector overload.

- Developer: added formatting overloads for `{Membership,User}::WriteNotice`.

- Developer: added the `Numeric::push_fmt` method to push a formatted parameter onto a numeric.

- Developer: deprecated the non-printable overload of `InspIRCd::GenRandomStr` in favour of `GenRandom`.

- Developer: refactored the `InspIRCd` and `ServerStats` types.

- Fixed `/AUTHENTICATE` being silently dropped when the user does not have the `sasl` capability or when a malformed `<trailing>` parameter is sent.

- Fixed `/WHOWAS` not showing the real server name to operators with the `services/auspex` privilege.

- Fixed `InspIRCd::StripColor` not stripping the value of hex colours.

- Fixed `InspIRCd::StripColor` stripping some legitimate non-formatting characters.

- Fixed bursting metadata between servers.

- Fixed downgrading `LMODE` messages when broadcasting to remote servers.

- Fixed downgrading `SINFO` messages when broadcasting to remote servers.

- Fixed exceptions from loggers not being handled.

- Fixed measuring the CPU load on Windows.

- Fixed retrieving database rows in the MySQL module.

- Fixed the argon2 module erroneously treating lanes as separate to threads.

- Fixed the blockcolor module blocking some legitimate non-formatting characters.

- Fixed the build when compiling with C++20 or newer.

- Made it clear that the cloak_md5 and md5 modules are deprecated.

- Reduced the memory usage of the whowas database.

- Refactored the Perl init script somewhat.

- Replaced the InspIRCd-specific `RPL_WHOWASIP` numeric with `RPL_WHOISACTUALLY`.

- Tweaked the defaults for `<whowas>` to make more sense for most networks.

- Tweaked the message for `RPL_WHOISCERTFP` to make it clear if the fingerprint is hashed using a compatibility algorithm.

### InspIRCd 4.2.0

**This version of InspIRCd was released on 2024-08-03.**

- Added support for the IRCv3 WebSocket subprotocols.

- Developer: added a `Module` constructor overload to allow modules to define the version to show in `/MODULES`.

- Developer: added the `ExtensionItem::OnSync` callback for when an extensible is synchronised across the network.

- Developer: merged `ProtocolServer ` and `Server`.

- Fixed allowing text websockets when the server has a non-utf8 charset.

- Fixed automatic synchronisation of unset extensibles.

- Fixed escaping semicolons in message tags.

- Fixed exposing the real hostname of users when recloaking.

- Fixed parsing S2S `UID` messages from 1205 (v3) servers.

- Fixed unescaping message tags that end with a `\`.

- Silenced some harmless log messages when parsing malformed CIDR ranges.

- Updated the vendored libraries.

- Updated the Windows dependencies.

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
