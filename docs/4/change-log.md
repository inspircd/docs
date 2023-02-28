---
title: v4 Change Log
---

{! 4/_support.md !}

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 4.0.0a20

**This pre-release version of InspIRCd was released on 2023-03-01.**

- Added `<chanhistory:maxduration>` to limit the maximum period to keep chat history for.

- Added `<sslinfo:localsecure>` to allow treating users connecting from localhost as if they were connected with TLS (SSL).

- Added users with user mode `h` (helpop) to the `/STATS P` output.

- Allowed clients to set themselves as away before they are fully connected to the server.

- Developer: exposed the cloak lists to the module API.

- Fixed being able to create a `half` or `full` cloak method without the md5 module loaded.

- Fixed being able to create a `hmac-sha256` or `hmac-sha256-ip` cloak without the sha256 module loaded.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Merged the servprotect module into the services module.

- Split the helpop module into two modules (help, helpmode).

### InspIRCd 4.0.0a19

**This pre-release version of InspIRCd was released on 2023-02-01.**

- Added `<websocket:nativeping>` for sending idle pings to WebSocket clients using WebSocket ping packets.

- Added support for SCTP user and server connections.

- Added support for synchronising server operator privileges between servers.

- Added templated variants of `UserManager::Find{Nick,UUID,}` which allow finding a remote or local user.

- Added the cloak_sha256 module which cloaks hostnames using a variant of the HMAC-SHA256 cloaking system from Plexus.

- Developer: moved duration functions from `InspIRCd` to the new `Duration` namespace.

- Developer: replaced `ConfigTag::get{Float,Int,UInt}` with the type safer `getNum` method.

- Developer: replaced `InspIRCd::Format` and `VAFORMAT` with a vendored copy of the {fmt} library.

- Developer: reworked the accessor methods in the User class to have names that make more sense.

- Made all modules which build against third-party dependencies print the library version on load where available.

- Reworked how users are assigned to connect classes and fixed counting class users.

- Split the cloaking module into the `cloak` module (core cloaking logic) and `cloak_md5` (the old md5-based cloaking system).

### InspIRCd 4.0.0a18

**This pre-release version of InspIRCd was released on 2023-01-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Added oper idle information to `/STATS P`.

- Added support for oper type specific MOTDs.

- Added support for overriding extban characters via the config file.

- Added support for overriding mode characters via the config file.

- Added support for requiring an oper to be logged into a user account.

- Changed the clock difference allowance between servers to be stricter (15s/5s for fail/warn vs 60s/15s in v3).

- Changed the default value for `<bind:replace>` to yes.

- Developer: added `ListExtItem` for wrapping a vector/set extension.

- Developer: added `SimpleExtItem::GetRef` to get a constant reference to an extension value using the default it does not exist.

- Developer: added a flag to the oper events that declares if an oper attempt was done automatically.

- Developer: added an option to `Percent::Encode` to encode as lower case.

- Developer: added the `irc::sockets::sockaddrs::is_local` method to determine if a socket address points to a local address.

- Developer: changed the socket address arguments to `Module::OnAcceptConnection` and various `IOHook` functions to be a constant referewnce instead of a pointer.

- Developer: changed various `SocketEngine` methods to take an `EventHandler` instead of a file descriptor.

- Developer: removed the automatic fallback from `ExtensionItem::FromInternal` to `ExtensionItem::FromNetwork`.

- Developer: removed the unused `Extensible` argument to `InspIRCd::PassCompare`.

- Fixed canonicalising an extban when added via the `/TBAN` command.

- Fixed parsing the v3 fallback config in the deaf module.

- Fixed the banredirect module breaking when encountering a long-style extban.

- Improved the log messages when an oper attempt succeeds or fails.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Moved `<oper:autologin>` to the core and reworked the config for it.

- Reworked the levels at which various messages are logged to make more sense.

### InspIRCd 4.0.0a17

**This pre-release version of InspIRCd was released on 2022-12-01.**

- Added the `inspircd.org/stats-tags` capability to get statistics data in message tags.

- Allow specifying commands, modes, privileges and snomasks in the oper type and account.

- Developer: refactored the oper types and events.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Moved the `o`, `O`, and `P` stats characters to core_oper and rewrote to be actually useful.

### InspIRCd 4.0.0a16

**This pre-release version of InspIRCd was released on 2022-11-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Added a compatibility layer to allow loading modules that were renamed in v4 with their names from v3.

- Developer: added a parameter to `UserManager::Find{Nick,UUID,}` to exclude partially connected users.

- Developer: made a bunch of APIs const correct.

- Developer: renamed (connection) registration to avoid a semantic conflict with account registration.

- Enabled services to inform the server of a list of nicknames that belong to an account.

- Fixed linking against v3 servers when the realnameban module is loaded.

- Fixed the sql_log module causing a cascade of snotices when it can't write to a database.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Reduced the memory usage of resolving server hostnames to IP addresses.

- Split the services_account module into two modules (account, services).

### InspIRCd 4.0.0a15

**This pre-release version of InspIRCd was released on 2022-10-01.**

- Changed `<hostname:charmap>` to disallow characters that have special meaning in the IRC wire format.

- Developer: changed command handler penalty to be measured in milliseconds instead of seconds

- Developer: changed command handlers to opt-in to empty trailing parameters instead of opting out.

- Developer: refactored the server notices sent to operators when loading and unloading a module.

- Developer: removed support for serialising and deserialising user data.

- Ensured that the `<hostname:charmap>` is synchronised across the network when linking to a v4 server.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Modernized the Windows compatibility layer.

### InspIRCd 4.0.0a14

**This pre-release version of InspIRCd was released on 2022-09-01.**

- Added support for logging JSON to stdout (`json-stdout`) and stderr (`json-stderr`) to the log_json message.

- Developer: changed `irc::sockets::sockaddrs` to be zero-initialized by default.

- Developer: converted `irc::sockets::{ap,un}tosa` to be `irc::sockets::sockaddrs` member functions.

- Developer: refactored the `FOREACH_MOD` and `FIRST_MOD_RESULT` macros.

- Developer: removed the string overload of `User::SetClientIP`.

- Developer: renamed `Module::OnSetUserIP` to `OnChangeRemoteAddress` to make it clear that client socket addresses can refer to a non-IP protocol.

- Developer: renamed the sockaddrs overload of `User::SetClientIP` to `ChangeRemoteAddress` to make it clear that client socket addresses can refer to a non-IP protocol.

- Fixed module loggers not being able to write the actual log time for messages that are cached on startup.

- Merged all of the changes from the v3 development branch into the v4 development branch.

### InspIRCd 4.0.0a13

**This pre-release version of InspIRCd was released on 2022-08-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Added the `~context` server tag to allow services to show a private message, notice, or tag message in a context of a channel.

- Merged all of the changes from the v3 development branch into the v4 development branch.

### InspIRCd 4.0.0a12

**This pre-release version of InspIRCd was released on 2022-07-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Added `<messageflood:kickmessage>` for customising the message flood kick reason.

- Added a new templating system for config-provided fields that contain variables.

- Added the `%diff%`, `%duration%`, `%lines%`, and `%seconds` template variables to the repeat module ban reason.

- Added the `%dnsbl%` and `%result%` template variables to the dnsbl module ban reason.

- Changed `<shun:cleanedcommands>` and `<shun:enabledcommands>` to use a token list instead of a set.

- Changed the passforward module to use the new templating system.

- Developer: made `ConfigTag::getEnum` return the default instead of throwing.

- Developer: sped up the build by reducing the number of unnecessary global headers.

- Fixed a crash caused by writing to a logger whilst unloading a logger.

- Fixed not blocking the loading, reloading, and unloading of modules by their short names.

- Fixed not shrinking module file names properly on macOS and Windows.

- Made all of the malformed config value error messages have a consistent format.

- Merged all of the changes from the v3 development branch into the v4 development branch.

### InspIRCd 4.0.0a11

**This pre-release version of InspIRCd was released on 2022-06-01.**

- Added support for named and indexed captures in the regex system.

- Added the log_json module for logging machine readable JSON messages to a file.

- Added the log_sql module for logging to an SQL database.

- Added the log_syslog module for logging to the system log on UNIX systems.

- Changed protection from being targeted by kicks/kills/etc to require user mode `k` (servprotect) instead of being on a services server.

- Changed the httpd_stats module to generate the output automatically instead of just emitting raw XML.

- Changed the log levels to better match how log messages are used.

- Deprecated the S2S version and fullversion SINFO keys and added the rawbranch and customversion keys to replace them.

- Fixed building the ISUPPORT token list before all modules have been initialized.

- Fixed log messages not being flushed for hours if a server wasn't particularly busy.

- Fixed repeated lookups of prefix modes by storing a sorted set of mode handlers instead of a string of mode characters.

- Fixed the server operator events duplicating data which is accessible from the user object.

- Merged all of the changes from the v3 development branch into the v4 development branch.

- Rewrote the entire account system from scratch.

- Rewrote the entire logging system from scratch.

### InspIRCd 4.0.0a10

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
