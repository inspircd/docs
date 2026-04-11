---
title: v4 Change Log
---

## Change Log

This page lists changes which have happened between releases.

## InspIRCd 4.10.1

**This version of InspIRCd was released on 2026-04-11.**

- Fixed the Windows binary containing the wrong version in the main executable.

- Relaxed validation of usernames in `USER` as it broke some clients.

- Whitelisted the `+channel-context` tag in the ircv3_ctctags module.

## InspIRCd 4.10.0

**This version of InspIRCd was released on 2026-04-04.**

- Added `<ctctags:clientonlytags>` as a replacement for `<ctctags:allowclientonlytags>`  with an additional `known` option to allow filtering to known IRCv3 message tags.

- Added an example config file that contains `<securehost>` tags for known safe IRC crawlers.

- Added extended ban `d:` (redirect) to the redirect module.

- Added support for the IRCv3 ACCOUNTEXTBAN ISupport token.

- Added support for the IRCv3 no-implicit-names specification to the ircv3 module.

- Added support for the IRCv3 UTF8ONLY specification.

- Added support for validating extended bans before they are set.

- Added the `<classban:operonly>` option to allow restricting setting extended ban `n:` (class) to server operators.

- Added the `zline` and `zlineopers` options for `<blockamsg:action>` which Z-lines users who send mass-messages.

- Added the ability to mark modules as deprecated.

- Added the sharebans module which allows bans to be shared between channels.

- Changed extended ban `z:` (fingerprint) to be only settable by server operators when TLS fingerprints are only visible to server operators (with an opt-out config option).

- Deduplicated checking command access.

- Deprecated the banredirect module in favour of extended ban `d:` (redirect) from the redirect module.

- Documented the existence of the `/DNSBL` command.

- Fixed cap-notify to not send `CAP DEL` before `CAP NEW` when the value of a capability changes.

- Fixed channel mode `f` (messageflood) miscounting user messages when a memory address is reused.

- Fixed checking the length limit for usernames, hostnames, and real names.

- Fixed counting the number of connections the server has had.

- Fixed erroneously being able to message unencrypted users when user mode `z` (sslqueries) is set.

- Fixed erroneously networking some user metadata for partially connected users.

- Fixed erroneously sending `MONITOR` notifications for partially-connected users.

- Fixed extended ban `a:` (realmask) and `r:` (realname) being unable to ban real names containing spaces.

- Fixed not being able to message TLS-using users who are not on your accept list when user mode `z` (sslqueries) is set.

- Fixed reading the help channel list.

- Fixed sending a `FAIL` message when a `NOTE` message should have been sent when using the `/CLOAK` command.

- Fixed sending the wrong username in the `ERR_INVALIDUSERNAME` numeric.

- Fixed sending too many `RPL_ENDOFNAMES` numerics when the user list of multiple channels is requested.

- Fixed some S2S commands erroneously being case sensitive.

- Improved the documentation of extended bans in the example help config.

- Increased the amount of modes the redirect module can redirect users to include banned users, uninvited users, and users beyond the limit.

- Updated the Windows dependencies.

### InspIRCd 4.9.0

**This version of InspIRCd was released on 2025-12-06.**

- Added `<autoconnect:bootperiod>` to allow autoconnecting faster on first boot.

- Added `<messageflood:resetonhit>` to allow opting-out of the new flood enforcement behaviour.

- Added support for multiple groups when using the ssl_openssl module.

- Added the `%duration.long%` template variable to `<messageflood:message>`.

- Added the `%duration.long%` template variable to `<repeat:message>`.

- Changed the default of `<messageflood:tagmsg>` from 0.2 to 0.1.

- Changed the messageflood module to use a per-user flood counter.

- Fixed a dead link in the example configs.

- Fixed a lack of error message sanitisation in the pgsql module.

- Fixed being able to use expired or otherwise invalid client certificates in some circumstances.

- Fixed channel mode `f` (flood) only blocking the first flood message.

- Fixed not using the OpenSSL security level when connecting as a client.

- Fixed the core_dns module logging a debug message at the critical level.

- Fixed the ssl_gnutls module mistakenly marking self-signed client certificates as invalid.

- Fixed the ssl_openssl module logging CA errors when a custom CA has not been specified.

- Fixed the syntax of the `/DNSBL` command.

- Improved the diagnostic errors logged when a oper fails to log in because of an incorrect client certificate.

- Improved the diagnostic errors logged when a server fails to link because of an incorrect client certificate.

- Improved the error messages from the config parser.

- Re-imported a cut-down version of the the genssl script for generating long-lasting certificates for server linking.

- Re-imported the regex_tre module now TRE is maintained again.

- Updated the vendored libraries.

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

- Added extended ban names to help.example.conf.

- Added support for help channels in which users with user mode `h` (helpop) will be automatically granted a channel prefix mode.

- Added support to Module Manager for linking to module documentation on install.

- Added the `%duration.long%` and `%remaining.long%` template variables to `<options:xlinequit>` and `<security:publicxlinequit>`.

- Added the `SAFERATE` 005 token to allow modern clients (e.g. Soju) to know when fakelag is enabled and relax their internal message buffering.

- Changed various messages to use long duration strings (e.g. "1 day, 2 hours, 3 minutes") instead of short duration strings (e.g. 1d2h3m).

- Developer: added `Duration::ToLongString` to convert a duration to a format which is more readable.

- Developer: added a formatting overload of the `ModuleException` constructor.

- Developer: added constants to the `Time` namespace for commonly used time formats.

- Fixed flushing the standard output stream after startup when not forking into the background.

- Fixed help.example.conf to correctly list all current exemptions, extended bans, and modes.

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

- Fixed removing regular bans that look like an extended ban.

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

- Added advertisement of the preferred extended ban format for services.

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

- Fixed extended bans silently overwriting extended bans with the same character from other modules.

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

- Fixed unregistering extended bans when a module unloads.

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
