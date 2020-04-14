---
title: v3 Change Log
---

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 3.6.0

<!-- TODO: ensure changes after commit 256be7a are added to this list before release. -->

**This version of InspIRCd has not yet been released.**

- Added `<include:noenv>` to disable using environment variables in an included config file.

- Added `<oper:snomasks>`  and `<type:snomasks>` to allow configuring the snomasks that a server operator can use.

- Added `<options:modesinlist>` to allow customising whether channel modes are included with the `/LIST` response.

- Added `<sasl:requiressl>` to require users to be connected via TLS (SSL) in order to be able to use SASL authentication.

- Added support for the [RFC 2812](https://tools.ietf.org/html/rfc2812) `/SERVLIST` command.

- Added support for using environment variables in the server configuration using the `&env.FOO;` syntax.

- Added the `/ADMIN` and `/OPER` commands to the default list of commands that a shunned user can execute.

- Added the `servers/ignore-shun` privilege to allow server operators to ignore shuns placed on them.

- Developer: added a way to exempt a message from updating the origin user's idle time.

- Developer: added an overloadable function to the `Command` class to allow configuring the message sent when a user executes a command that they need to be registered to use.

- Developer: added an overloadable function to the `Command` class to allow configuring the message sent when a user executes a command without specifying enough parameters.

- Developer: added multi-parameter overloads to the `IRCv3::Replies::Reply::SendIfCap` method.

- Developer: added the `EventHandler::HasFd` method for checking if an event handler is configured with a file descriptor.

- Developer: added the `Numerics::CannotSendTo` class for sending the "can not send to channel/user" numerics.

- Developer: added the `USERMODES` 005 token to allow parsing mode changes easier.

- Developer: added the `User::HasSnomaskPermission` method for checking if a user can use a snomask.

- Developer: added the `UserManager::all_ulines` list which contains all services on U-lined servers.

- Developer: deprecated the `XLineManager::InvokeStats` methods in favour of a new overload which uses a generic numeric.

- Developer: stabilised support for the [IRCv3 Standard Replies](https://ircv3.net/specs/extensions/standard-replies) specification.

- Fixed a bug where previously changed display hostnames would be reset when a hostname lookup finishes.

- Fixed a memory leak in the dccallow module.

- Fixed being able to use the `MODE` command to look up the modes of a private or secret channel.

- Fixed leaking HTTPd sockets if they were closed with data left in their outgoing buffer.

- Fixed reloading core modules by their short name.

- Fixed sending `RPL_WHOISCOUNTRY` for services pseudoclients.

- Fixed sending mass-messages to other servers on the network.

- Fixed server filters applying to mass-messages sent by server operators.

- Fixed setting the permissions of a UNIX socket listener.

- Fixed showing a malformed sts capability if the configuration was invalid on rehash.

- Fixed silently failing when trying to load more than 31 capabilities.

- Fixed the chanlog module writing duplicate log messages when sending snotices is enabled.

- Fixed the entire DNS cache not being reloaded on rehash.

- Fixed the restrictchans module not telling the user when they are prevented from creating a channel.

- Fixed various config values using an empty value instead of the default if an empty value was specified.

- Fixed warning snotices not being sent when a user fails to login to a server operator account which requires TLS (SSL) and/or a matching client certificate fingerprint.

- Implemented support for [the IRCv3 SETNAME specification](https://ircv3.net/specs/extensions/setname.html).

- Implemented support for multi-line CAP responses.

- Improved the descriptions of all of the modules.

- Improved the error message shown when trying to load a module which is too old or too new for the current version.

- Improved the error messages shown by the ldap module.

### InspIRCd 3.5.0

**This version of InspIRCd was released on 2020-01-31.**

- Added support for [the IRCv3 Labeled Response specification](https://ircv3.net/specs/extensions/labeled-response.html).

- Added support for help topics to the helpop module.

- Added support for pagination to the index output of the `HELPOP` command.

- Added support for passing module names to `--{disable,enable}-extras` using their short names (e.g. `--enable-extras ssl_gnutls`).

- Added support for passing space-delimited module names to `--{disable,enable}-extras` (e.g. `--enable-extras "ssl_gnutls ssl_mbedtls"`).

- Added support for the `X-Real-IP` and `X-Forwarded-For` headers to the websocket module.

- Added the codepage module &mdash; a better solution for custom 8-bit character set support than the incredibly broken and undocumented nationalchars module.

- Changed the default for `<waitpong:sendsnotice>` to `no`.

- Changed the user count in `LUSERS` so that it no longer includes services pseudoclients.

- Developer: add `Channel::WriteRemoteNotice` which sends a notice to remote users as well as local users.

- Developer: add a status char option to `Channel::WriteNotice` for sending status messages.

- Developer: add the `ClientProtocol::MessageTagEvent` class to allow handling message tags easier.

- Developer: added `MessageTarget::GetName` to allow easily getting the name of a message target.

- Developer: added a status char option to the `TagMessage` constructor for sending status messages.

- Developer: added an "oper only" parameter to `Simple{Channel,User}ModeHandler`.

- Developer: added empty string checks to the `Numerics::NoSuch{Channel,Nick}` constructors.

- Developer: added several variadic overloads of the `IRCv3::Replies::Reply::Send` method.

- Developer: added the `OnCommandBlocked` event for when the execution of a command is blocked.

- Developer: added the `UserManager::ULineCount` method for counting pseudoclients on U-lined servers.

- Developer: added the `inspircd.org/poison` capability which rejects any attempt to request it to avoid clients requesting all available capabilities rather than the ones they support.

- Developer: added the `stdalgo:delete_zero` method for deleting and zeroing a pointer.

- Developer: deprecated the `ProtocolInterface::Send{Channel,User}Notice` methods in favour of `SendMessage`.

- Developer: disabled `CULLLIST` log messages unless the server has been built in debug mode.

- Developer: switched from Travis CI to GitHub Actions.

- Developer: the `FailedPort` type now contains the config tag that the listener was created from.

- Fix connections to ports which have an invalid I/O hook configured not being rejected.

- Fix various Perl tools not looking in the right directory for the `make::*` modules.

- Fixed a bug in `helpop.conf.example` where the SWHOIS key was not using the correct value name.

- Fixed allowing `TAGMSG` messages to be sent without any tags attached.

- Fixed boolean configuration options not being matched in a case insensitive way.

- Fixed not using case insensitive comparisons for the DCCALLOW subcommands.

- Fixed not using case insensitive matching when checking if a TLS (SSL) rehash has been requested.

- Fixed not using the `ERR_INVALIDMODEPARAM` numeric when not enough parameters are given to the `snomask` mode.

- Fixed not using the `RPL_REHASHING` numeric for remote rehashes.

- Fixed parsing CTCPs in the dccallow module.

- Fixed prioritisation of custom events provided by modules.

- Fixed spamming the log with DNS cache clearing notices when nothing was actually cleared.

- Fixed status messages not working with the `TAGMSG` command.

- Fixed the chanhistory module not storing message tags.

- Fixed the chanhistory module not storing notices.

- Fixed the chanhistory module storing CTCPs.

- Fixed the legacy `PROTOCTL NAMESX` command not using case insensitive matching.

- Fixed the legacy `PROTOCTL UHNAMES` command not using case insensitive matching.

- Fixed the nationalchars module allowing nicknames which begin with a number.

- Fixed the nationalchars module not rebuilding the 005 numerics on unload.

- Fixed the nationalchars module not restoring the previous casemapping name on unload.

- Fixed the systemd unit file starting InspIRCd before the network is online.

- Fixed unnecessarily making `N*2-1` too many copies of the command arguments when processing a command with multiple targets.

- Improve the warning process when starting InspIRCd as root.

- Improved the ban message shown to users if they are banned by an extban.

- Improved the output when a port can not be bound.

- Removed the preceding `-` from the MOTD, server operator MOTD, and any custom MOTDs added with the showfile module.

- Renamed `<chanhistory:notice>` to `<chanhistory:prefixmsg>` so the behaviour is less ambiguous.

- Replace the Windows getopt\_long shim with the ya\_getopt library.

- Updated the example MOTD and server operator MOTD to be a bit prettier and show off some of the escape codes.

### InspIRCd 3.4.0

**This version of InspIRCd was released on 2019-10-25.**

* Added `<alias:stripcolor>` to allow stripping formatting codes before matching an alias.

* Added `<cloak:ignorecase>` to ignore the case of a FQDN when cloaking.

* Added a check for the `channels/auspex` privilege to the hidemode module.

* Added a workaround for gateway IP addresses being banned by the connectban module.

* Added more information to timedbans addition/expiry notices.

* Added support for filtering part messages to the chanfilter module.

* Developer: added `ConfigStatus::initial` to find out if the config is being loaded for the first time.

* Developer: added `Events::ModuleEventProvider::{OnSubscribe,OnUnsubscribe}` to allow knowing when a module has subscribed to or unsubscribed from an event.

* Developer: added a parameter to the `OnServerSplit` event which specifies whether the split was intended or not.

* Developer: added an internal serialisation of the dccallow list.

* Developer: added an internal serialisation of the silence list.

* Developer: added the `GetId` method to the `Server` class.

* Developer: added the `GetNumericToken` method to the `irc::sepstream` class.

* Developer: added the `GetTypeStr` method to the `DNS::Manager` class.

* Developer: added the `OnServerBurst` event for executing actions after a server has finished bursting.

* Developer: added the `OnShutdown` event for executing actions shortly before shutdown.

* Developer: added the experimental `Serializable` class &amp; API and implemented it in the `Extensible`, `User` and `LocalUser` classes.

* Developer: changed `IS_{LOCAL,REMOTE,SERVER}` to be capable of handling null pointers.

* Developer: exposed variable list modes via the `VLIST` 005 token to make things easier for client developers.

* Disabled DNS, DNSBL, and ident lookups for unregistered KiwiIRC.com users in the example provider configs.

* Documented the `repeat` exemption type.

* Exempted the KiwiIRC.com servers from X-lines in the example provider configs.

* Fixed a bug in the HAProxy module where it would ignore any data received in the same packet as the header when using TCP connections.

* Fixed a crash on shutdown in the spanningtree module.

* Fixed linker errors caused by build objects from one compiler being used by another.

* Fixed not respecting the deprecated `<channels:users>` config tag.

* Fixed the DNSBL module banning a user after their IP address has changed.

* Fixed the IP addresses of the KiwiIRC.com servers in the example provider configs.

* Fixed the `OnSetUserIP` event being fired before the connect class has changed.

* Fixed the `u_noctcp` mode not being respected for CTCPs targeted at a channel.

* Fixed the config example path not being updated when the config path is changed in interactive mode.

* Fixed the example configs allowing voiced users to voice/devoice other users.

* Fixed the example provider config files not being installed.

* Fixed the silence module not being able to add or remove entries in some cases.

* Fixed various issues relating to hostname resolution.

* Raised the default value for `<connflood:bootwait>` from ten seconds to two minutes.

* Replaced the gdbargs file with the `--eval-command` option inside the init script.

* Updated the NetBSD `EV_SET` workaround now that upstream have fixed the issue.

### InspIRCd 3.3.0

**This version of InspIRCd was released on 2019-08-23.**

* Added PackageInfo directives for ArchLinux.

* Changed the maximum value for `<chanfilter:maxlen>` from 100 to 250.

* Developer: added an experimental header which implements the [IRCv3 Standard Replies draft](https://github.com/ircv3/ircv3-specifications/blob/master/extensions/standard-replies.md).

* Developer: added the OnConnectionFail event for suspending a user connection which is about to fail.

* Developer: added the `ExtensionItem::{To,From}{Human,Internal,Network}` methods to convert an extension item to and from various string forms.

* Developer: added the `MessageEventListener` class for adding tags to server messages.

* Developer: added the `{EventHandler,StreamSocket,UserIOHandler}::SwapInternals` methods to swap the internals of two sockets.

* Developer: deprecated the ServerEventListener clas and split the events contained within it into the `ServerProtocol::{BroadcastEventListener,LinkEventListener,SyncEventListener} classes.

* Developer: deprecated the `SerializeFormat` enum, and the `serialize`, `unserialize` methods of the `ExtensionItem` class, and the `LocalExtItem` class.

* [Fixed a **crash** in the MySQL module when built against mariadb-connector-c v3.0.5 or newer](/security/2019-02).

* Fixed allowing the `sasl` capability to be requested when the SASL server is offline.

* Fixed empty `GLOBOPS` and `WALLOPS` messages not failing with an `ERR_NOTEXTTOSEND` message.

* Fixed listener sockets with `<bind:replace>` enabled not being replaced in some circumstances.

* Fixed not applying IRCv3 `server-time` timestamps on the server the source is connecting from.

* Fixed not being able to use the `O` (oper) extban to server operators with a space in their server operator type.

* Fixed referring to registration timeouts as ping timeouts in the `conn_waitpong` module.

* Fixed sending IRCv3 `account-notify` and `chghost` messages to a user who has not sent the `NICK` and `USER` commands yet.

* Fixed sending IRCv3 `cap-notify` messages for capabilities which are not presently visible in `CAP LS`.

* Fixed the `geo_maxmind` module trying to interpret an `AF_UNIX` endpoint as an IP address.

* Improved the message sent to server operators when the maximum connections for a connect class is reached.

* Updated the vendored `utfcpp` library to v3.1.

### InspIRCd 3.2.0

**This version of InspIRCd was released on 2019-07-05.**

- Added a configure option, `--example-dir`, which specifies the directory that example config files get installed into.

- Added a flag to the filter module which allows registered users to be exempt from a filter.

- Added a warning when the user tries to build on OpenBSD as it ships very broken compilers.

- Added a warning when the user tries to build without TLS (SSL) support.

- Added example config files for enabling support for IRCCloud and KiwiIRC.com on your server.

- Added syntax hints for all modes with parameters to the `ERR_INVALIDMODEPARAM` numeric response.

- Added the ability to include all .conf files in a directory.

- Added `<bind:permissions>` to UNIX socket listeners to set who can access the socket.

- Added `<bind:replace>` to UNIX socket listeners to allow replacing existing sockets on boot.

- Added `<messageflood:notice>`, `<messageflood:privmsg>`, and `<messageflood:tagmsg>` to  the messageflood module to specify how many lines individual messages are equivalent to.

- Added `<permchanneldb:saveperiod>` to allow customising how often the permchannels module should check whether its database needs to be saved.

- Added `<sslprofile:tlsv11>` and `<sslprofile:tlsv12>` to the ssl_openssl module to easily allow disabling old TLS (SSL) versions.

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

- Show how many users in a channel are not using TLS (SSL) in the `ERR_ALLMUSTSSL` response.

- Updated the Module Manager source list for the new inspircd-contrib repository.

### InspIRCd 3.1.0

**This version of InspIRCd was released on 2019-05-17.**

- Added a configure option, `--disable-auto-extras`, which disables automatically enabling extras for which the dependencies are available.

- Added support for disabling a STS policy for users in specific connect classes.

- Added support for [the IRCv3 Message IDs specification](https://ircv3.net/specs/extensions/message-ids.html).

- Developer: added support for modules overriding the default access checks for `NOTICE`, `PRIVMSG`, and `TAGMSG`.

- Developer: added the `INSPIRCD_VERSION_BEFORE(MAJOR, MINOR)` and `INSPIRCD_VERSION_SINCE(MAJOR, MINOR)` macros for checking the InspIRCd version at compile time.

- Developer: allowed child classes of SSLIOHook to override `GetCertificate()` and `GetFingerprint()`.

- [Fixed a **crash** in the silence module on some older versions of GCC](/security/2019-01).

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
