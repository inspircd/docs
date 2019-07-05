---
title: v3 Change Log
---

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 3.2.0

**This version of InspIRCd was released on 2019-06-05.**

- Added a configure option, `--example-dir`, which specifies the directory that example config files get installed into.

- Added a flag to the filter module which allows registered users to be exempt from a filter.

- Added a warning when the user tries to build on OpenBSD as it ships very broken compilers.

- Added a warning when the user tries to build without SSL support.

- Added example config files for enabling support for IRCCloud and KiwiIRC.com on your server.

- Added syntax hints for all modes with parameters to the `ERR_INVALIDMODEPARAM` numeric response.

- Added the ability to include all .conf files in a directory.

- Added `<bind:permissions>` to UNIX socket listeners to set who can access the socket.

- Added `<bind:replace>` to UNIX socket listeners to allow replacing existing sockets on boot.

- Added `<messageflood:notice>`, `<messageflood:privmsg>`, and `<messageflood:tagmsg>` to  the messageflood module to specify how many lines individual messages are equivalent to.

- Added `<permchanneldb:saveperiod>` to allow customising how often the permchannels module should check whether its database needs to be saved.

- Added `<sslprofile:tlsv11>` and `<sslprofile:tlsv12>` to the ssl_openssl module to easily allow disabling old SSL versions.

- Added `<xlinedb:saveperiod>` to allow customising how often the xline_db module should check whether its database needs to be saved.

- All SQL queries are now logged at the debug log level to enable easier debugging of SQL issues.

- Developer: added support for marking a socket to be closed once it has finished receiving all the data sent to it.

- Developer: added support for retrieving the end message of a batch.

- Developer: added the OnUserPreQuit event for changing quit messages before a user disconnects.

- Developer: added the `FileSystem::GetFileList()` function to get a list of files in a directory matching a glob pattern.

- Developer: added the `irc::sockets::isunix()` function for checking if a string is a valid UNIX socket path.

- Developer: ignore any `SIGUSR1` or `SIGUSR2` with no handlers instead of killing the process.

- Fixed a misleading debug message in the sslinfo module.

- Fixed calculating the human-readable version of durations.

- Fixed closing HTTP connections before the entire http_stats module output had been sent.

- Fixed linking the spanningtree module on OpenBSD.

- Fixed modules that are in the process of being unloaded sometimes having events called on them.

- Fixed not checking if the cap module is enabled before enabling the `NAMESX` and `UHNAMES` 005 tokens.

- Fixed outgoing UNIX socket server connections.

- Fixed routing tags on TAGMSG messages between servers.

- Fixed server operators with the `channels/auspex` privilege not being able to request the topic of secret/private channels with the `/TOPIC` command.

- Fixed the autoop module checking the prefix mode add rank when removing list entries.

- Fixed the conn_umodes module setting user modes before the MOTD has been sent.

- Fixed the default log directory in system-wide mode to be `/var/log/inspircd`.

- Fixed the denychans module not checking whether the redirect channel is allowed properly.

- Fixed the exemptchanops module not validating list entries.

- Fixed the grammar of the error messages sent by the repeat module.

- Fixed the Perl helper script finding the location of the PID file.

- Fixed the sslinfo module not being able to place WebIRC users into the appropriate connect classes.

- Fixed the TAGMSG message forwarding all tags regardless of whether they had been whitelisted.

- Fixed the `<connect:usests>` option being inverted.

- Fixed various harmless compiler warnings in the httpd module.

- Fixed `<pid:file>` not being relative to the data directory as was intended.

- Fixed `server-time` timestamps only being accurate to the second.

- Made the error message sent by the alias module when an alias requires a U-lined target but the target is not U-lined more accurate.

- Show how many users in a channel are not using SSL in the `ERR_ALLMUSTSSL` response.

- Updated the Module Manager source list for the new inspircd-contrib repository.

### InspIRCd 3.1.0

**This version of InspIRCd was released on 2019-05-17.**

- Added a configure option, `--disable-auto-extras`, which disables automatically enabling extras for which the dependencies are available.

- Added support for disabling a STS policy for users in specific connect classes. 

- Added support for [the IRCv3 Message IDs specification](https://ircv3.net/specs/extensions/message-ids.html).

- Developer: added support for modules overriding the default access checks for `NOTICE`, `PRIVMSG`, and `TAGMSG`.

- Developer: added the `INSPIRCD_VERSION_BEFORE(MAJOR, MINOR)` and `INSPIRCD_VERSION_SINCE(MAJOR, MINOR)` macros for checking the InspIRCd version at compile time.

- Developer: allowed child classes of SSLIOHook to override `GetCertificate()` and `GetFingerprint()`.

- Fixed a **crash** in the silence module on some older versions of GCC.

- Fixed linking against v2 servers running the ASCII case mapping module from inspircd-contrib.

- Fixed an inverted condition in the commonchans module which made the module not work.

- Fixed configure not failing when invalid options were passed to it.

- Fixed pending X-lines only being applied to a single user.

- Fixed servers not specifying whether they are hidden. If no visibility is specified then servers default to the visibility of their parent server.

### InspIRCd 3.0.1

**This version of InspIRCd was released on 2019-05-10.**

- Documented the anticaps exemption in both the main config and in the example helpop config.

- Documented user mode `O` (override) in the helpop config.

- Fixed building against older versions of glibc.

- Fixed compiling with the kqueue socket engine on NetBSD.

- Fixed relying on PWD being set in the makefile.

- Fixed the `--distribution-label` configure option erroneously making the configure script require the `--development` flag to be passed.

- Fixed the example `<wsorigin>` tag erroneously suggesting that a path was included.

- Fixed the filesystem permissions that files are installed with.

- Fixed the MAXLIST 005 token not reflecting the true lower limit.

- Fixed the parameters for the `/NAMES` command in the syntax hint and example helpop config.

- Raised the connection timeout in the example configs to 20s. This should give more time for clients on slow connections that want to do a lot of things (request caps, do SASL auth, etc) on connect.

- Silenced a harmless compiler warning in the pgsql module on newer GCCs.
