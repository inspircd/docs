---
title: v3 Change Log
---

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 3.12.0

<!-- TODO: ensure changes after commit 1a49cc8be3019245d4ff96c7bec9aded2c5ad5c7 are added to this list before release. -->

**This version of InspIRCd has not yet been released.**

- Added `/CYCLE` and `/KNOCK` to the list of sanitisable shun commands.

- Added a warning about libdl incompatibilities when building against musl libc.

- Added support for manually specifying the WebIRC properties to trust from a gateway.

- Added support for rejecting WebSocket connections that don't request a subprotocol.

- Added support for retrieving client SSL certificate fingerprints from WebIRC gateways.

- Added the `channels/ignore-repeat` server operator privilege to allow ignoring the repeat mode.

- Changed the `OVERRIDE` 005 token to contain the letter of the mode needed to override.

- Developer: Added the `IOHook::IsHookReady` hook to determine whether an I/O hook is ready to send and receive data.

- Fixed DN strings being inconsistently processed across the TLS (SSL) modules.

- Fixed reading WebSocket proxy headers when the IRC server is behind multiple reverse proxies.

- Fixed sending `ERR_CHANOPRIVSNEEDED` instead of `ERR_RESTRICTED` in cases where privileges will not change the ability to perform an action.

- Fixed the `/SSLINFO` helpop not documenting how to view channel SSL information.

- Fixed the customprefix module allowing the creation of prefix modes with a space in the name.

- Fixed the default server name defaulting to `irc.example.com` instead of the machine name on Linux.

- Fixed the ldap module checking the return value of `ldap_compare_s` incorrectly.

- Fixed the public server name being used as a public server description instead of the network name when `<options:hideserver>` is set.

- Fixed the real server hostname being exposed to users in some cases when `<options:hideserver>` is set.

- Fixed the ssl_gnutls module not compiling on C++17 compilers due to the use of a removed feature.

- Fixed the ssl_openssl module not compiling on LibreSSL.

- Fixed unnecessary repeated mode lookups in the banredirect, messageflood, repeat, and timedbans modules.

- Fixed various text fields not being XML escaped in the httpd_stats output.

- Updated the libraries in the Windows Conan dependency file.

### InspIRCd 3.11.0

**This version of InspIRCd was released on 2021-08-27.**

- Added `<connectban:bootwait>` to allow delaying connectban until the specified time period has passed after boot.

- Added `<connectban:splitwait>` to allow delaying connectban until the specified time period has passed after a network partition.

- Added `<gnutls:onrehash>`, `<mbedtls:onrehash>`, and `<openssl:onrehash>` to allow reloading TLS (SSL) profiles on rehash.

- Added `<hostchange:ports>` to allow selection of rules based on the client's connection port.

- Added `<mkpasswd:operonly>` to restrict the `/MKPASSWD` command to server operators.

- Added a check that the filesystem is actually writable before attempting to generate the build system files.

- Added channel list mode limits to the S2S protocol to allow services to not exceed list limits.

- Added config variables for the config, data, log, module, and runtime directories that were configured at build time.

- Added support for building most extra modules on Windows with Conan.

- Added support for setting TLS 1.3+ ciphersuites in ssl_openssl.

- Added support for the `binary.inspircd.org` and `text.inspircd.org` WebSocket subprotocols to allow web clients to override `<websocket:sendastext>`.

- Added the `--disable-ownership` flag to configure to install without setting filesystem permissions or the user/group to run as.

- Change `RPL_WHOISOPERATOR` to say "is a network service" for U-lined clients when `<security:genericoper>` is enabled.

- Changed `<oper:autologin>` to accept a value of `if-host-match` to allow autologin to only proceed if the user's hostname matches the value in `<oper:host>`.

- Changed the delayjoin module to send the original join time on delayed join messages to clients with the `server-time` capability enabled.

- Changed the system-wide runtime directory on Linux to `/run/inspircd` to avoid a symlink issue with AppArmor.

- Developer: added `IRCv3::WriteNeighborsWithCap::GetAlreadySentId()` for getting the event id of the message which was sent.

- Developer: added the OnPostChangeRealHost event which is fired after a user's real hostname has been changed.

- Developer: moved `/WHOIS` numerics from modules to the main module header file.

- Fixed `/MKPASSWD` disconnecting users if an error happened whilst generating a password.

- Fixed `/NAMES` sending `ERR_NOSUCHCHANNEL` when a channel does not exist.

- Fixed `<log:method>` not defaulting to file logging.

- Fixed `<security:userstats>` not having a sensible default value.

- Fixed a compiler error in the sha256 module on Haiku.

- Fixed a race condition relating to hostname lookups and the haproxy module.

- Fixed an off by one error in the `inspircd` help output.

- Fixed building the ssl_mbedtls module on mbedTLS v3.

- Fixed checking [GKZ]-lines on users who are connecting via a gateway.

- Fixed installing the runtime path if it did not exist.

- Fixed mistakenly registering services globally by their subname (e.g. ssl/websocket -> websocket).

- Fixed mistakenly sending `RPL_WHOISHOST` for U-lined clients.

- Fixed not sending the `CHARSET` 005 token when using a non-ASCII casemapping.

- Fixed sending special oper whois when hideoper is enabled.

- Fixed the `/SILENCE` list serialising `TAGMSG` silences in reverse.

- Fixed the `make deinstall` target to actually remove files properly.

- Fixed the httpd module not parsing headers correctly (this broke the httpd_acl module).

- Fixed the name of the strict-rfc1459 casemapping example config.

- Fixed the noctcp module not respecting the `users/ignore-noctcp` privilege and the `u_noctcp` channel mode for mass-messages.

- Fixed the websocket module not parsing HTTP headers properly.

- Fixed timed bans not being expired correctly if they were truncated.

- Fixed unusual list mode values being allowed.

- Fixed various spelling mistakes all over the codebase.

- Removed `RPL_WHOISSERVICE` as it conflicts with the considerably more popular `RPL_WHOISHELPOP` from UnrealIRCd.

- Removed the broken attempt at root dropping in the helper script.

### InspIRCd 3.10.0

**This version of InspIRCd was released on 2021-05-14.**

- Added a codepage file for iso-8859-2 casemapping.

- Added a human readable version of the cloak list for use with `/CHECK`.

- Added automatic pruning of expired entries to the chanhistory module.

- Added extended ban `w:` (gateway) which matches against a WebIRC gateway name.

- Added more logging to the http_acl module to allow debugging access issues.

- Added support for automatically enabling the ldap, regex_stdlib, and ssl_mbedtls modules when their dependencies are available.

- Added support for multiple hosts in `<connect:allow>` and `<connect:deny>`.

- Added support for optional includes that are only loaded if they exist.

- Added support for per-DNSBL timeouts and raised the default for torexit.dan.me.uk to 10 seconds.

- Added support for serialising filters to a config file.

- Added support for using the `--prefix` configure option with `--system`.

- Changed `RPL_WHOISGATEWAY` so it is visible by unprivileged users.

- Changed the default runtime directory in system-wide mode to /var/run/inspircd to allow writing files after dropping root.

- Changed the idle time in `/STATS P` to use a duration string instead of seconds.

- Changed the onchans `/CHECK` entry to show all of a user's prefix modes.

- Changed the storage engine for the MySQL sqloper module from MyISAM to InnoDB.

- Developer: added subclass of `IOHookProvider` for TLS (SSL) modules.

- Fixed a `/WHO` request with flags but no fields being considered fuzzy.

- Fixed an off by one error in various bitsets.

- Fixed configure not printing a newline after warnings in some cases.

- Fixed miscounting DNSBL stats when a user disconnects or a DNSBL is down.

- Fixed not being able to name a class a value beginning with `unnamed-`.

- Fixed not being able to print coloured text to the standard error stream on Windows.

- Fixed not being able to send a standard reply with no command in some cases.

- Fixed not sending `ERR_BADCHANMASK` in response to OJOIN/SAJOIN when a channel name is invalid.

- Fixed not using the `ERR_INVALIDMODEPARAM` numeric when a parameter begins with `:` or contains a space.

- Fixed not using the default value for a bool/duration/int/uint config field when an empty value is specified.

- Fixed sending malformed pong messages in some cases.

- Fixed the deaf module not blocking tag messages.

- Fixed the ldapauth module not using the `<ldapauth:useusername>` field when it is documented to.

- Fixed unknown DNS record types preventing the retrieval of other DNS records.

- Fixed writing port bind errors to the standard output stream instead of the error stream.

- Improved the CTCP detection of the blockcolor module.

- Improved the messages sent when loading, unloading, or reloading modules.

- Improved the messages sent when trying to set or unset an unknown mode.

- Improved the output of `/STATS p` when multiple I/O hooks are in use.

- Renamed `<bind:ssl>` to `<bind:sslprofile>` (old configs will still work).

- Renamed `<link:ssl>` to `<link:sslprofile>` (old configs will still work).

- Renamed the latin1 codepage file to iso-8859-1.

- Warn about compiler and Perl versions for which support will be dropped in the future when using configure.

### InspIRCd 3.9.0

**This version of InspIRCd was released on 2021-02-26.**

- Added `<chanhistory:enableumode>` to allow enabling user mode `N` (nohistory) which allows users to opt-out of receiving channel history on join.

- Added `<connect:useconnectban>` to allow exempting classes from the connectban module.

- Added `<connect:useconnflood>` to allow exempting classes from the connflood module.

- Added a `/CAPAB` client command that will kill server connections made to client ports with a helpful message.

- Added a configure option, `--runtime-dir`, which specifies the directory that runtime files (i.e. the pid file) should be placed in.

- Added a DNS error class to the DNSBL stats.

- Added a human readable version of the geolocation data so it works in `/CHECK`.

- Added config entities which can be used for formatting IRC messages.

- Added default compiler flags for the ssl_openssl module to make building on distributions where OpenSSL is part of the base system easier.

- Added example provider configs for DroneBL, the EFnet RBL, and the dan.me.uk Tor exit node DNSBL.

- Added extended bans to the S2S protocol to allow services to validate bans easier.

- Added HTTP path normalisation to the httpd module.

- Added snomask privileges to the `/CHECK` output of a server operator.

- Added support for multi-prefix to `/WHOIS` channel lists.

- Added support for specifying multiple hostmasks in `<cgiirc:mask>`.

- Added support for the standard XML `&apos;`, `&gt;` and `&lt;` entities in the config.

- Added the `/HEXIP` command to the cgiirc module to allow encoding and decoding IP addresses from their ident format.

- Added the `<dns:enabled>` option to allow disabling DNS lookups entirely.

- Added the `<repeat:kickmessage>` option to allow configuring the message shown when a user is kicked by the repeat module.

- Added the `<shun:allowconnect>` option to allow configuring whether shuns should only be applied to users who are fully connected to the server.

- Developer: Added `ServerConfig::GetServer{Desc,Name}()` to allow retrieving the visible server name and description easier.

- Developer: added support for casting a `Cap::Reference` to a `Cap::Capability*`.

- Fixed `./configure --update` with cache files generated before v3.2.

- Fixed `/MAP` column alignment not taking into account the length of the server version.

- Fixed `<class:snomask>` not being parsed correctly when a type has multiple oper classes.

- Fixed a bunch of inconsistent Perl version requirements.

- Fixed a crash on shut down when started with `--debug --nofork`.

- Fixed being able to call events provided by modules that are dying.

- Fixed DNSBLs that return non-local addresses blocking connections.

- Fixed handling DNSBLs that return invalid lookup results.

- Fixed inconsistently hiding the server name when `<options:hideserver>` is set.

- Fixed modulemanager storing files in the incorrect directory if not executed from the root of the source directory.

- Fixed not being able to classban a class with spaces in the name.

- Fixed not being able to log into an server operator account with an IP whitelist when using ldapoper.

- Fixed NOTICE, PRIVMSG, and TAGMSG with multiple status message characters.

- Fixed sending `ERR_NOSUCHNICK` instead of `ERR_NOSUCHSERVICE` when a U-line alias requirement is unavailable.

- Fixed server operators not being able to see module versions in `/MODULES`.

- Fixed silently failing when a DNSBL returns no IPv4 results.

- Fixed storing data files in `/var/inspircd` instead of `/var/lib/inspircd`.

- Fixed the `/GLOADMODULE`, `/GUNLOADMODULE`, and `/GRELOADMODULE` commands not sending error numerics across the network.

- Fixed the DNS socket not being closed when core_dns is unloaded.

- Fixed the fallback linker flags for the argon2 module.

- Fixed the grammar of the message broadcast when reloading the TLS (SSL) profiles.

- Fixed the helper script not storing Valgrind log files in the log directory.

- Fixed the name of the sha1 hash provider.

- Fixed the numeric sent when reloading a module which is not loaded.

- Fixed the path specified in `--prefix` being relevant at runtime.

- Fixed trying to set snomasks on non-server operators with SAMODE

- Fixed users with the same casemapped nick sometimes being lost by the codepage module.

- Fixed using the legacy TR1 header files when building with a C++11 compiler.

- Improved debug logging for HTTPd modules.

- Improved debug logging for service registration and deregistration.

- Improved the error messages sent by the httpd module.

- Removed the `/SERVER` stub command.

- Send `RPL_SAVENICK` numerics (from irc2) whenever a user's nick is forcibly changed to their UUID.

- Updated the `/SERVLIST` command to match against and show the oper type of services pseudoclients.

- Updated the `/SSLINFO` command to allow viewing information about channels.

- Updated the IRCCloud example configs to exempt it from DNSBL lookups, connectban bans, and connflood throttles.

### InspIRCd 3.8.1

**This version of InspIRCd was released on 2020-11-20.**

- Added a config file for using InspIRCd with AppArmor.

- [Fixed a **crash** in the websocket module when a user behind a HTTP proxy is [GKZ]-lined](/security/2020-02).

- Fixed a harmless compiler warning on recent versions of GCC.

- Fixed an off by one error in the error message shown when an invalid option is passed on the command line.

- Fixed connect class logging being unreliable and inconsistent.

- Fixed continuing with event hooks when a user is quit in the "IP changed" event.

- Fixed showing an incorrect error when a module could not be loaded.

- Fixed the connectban and dnsbl modules executing before core_xline.

- Fixed trailing and preceding whitespace not being stripped by `--{disable,enable}-extras`.

### InspIRCd 3.8.0

**This version of InspIRCd was released on 2020-10-30.**

- Added `<cban:glob>` to allow using glob matches within cbans.

- Added `<joinflood:bootwait>` to allow disengaging channel mode `j` (joinflood) when a server first starts up.

- Added `<joinflood:splitwait>` to allow disengaging channel mode `j` (joinflood) when a server splits from the network.

- Added `<shun:allowtags>` to allow configuring whether shunned users can send client-to-client tags.

- Added `<shun:cleanedcommands>` to allow configuring the commands that shunned users can run but that will be censored.

- Added a question to `./configure` for deleting previously created self-signed certificates.

- Added a warning about non-local unencrypted server connections being insecure.

- Added the new tinside server and IP blocks to the IRCCloud provider config file.`

- Added support for specifying the output directory when using `inspircd-genssl`.

- Added support for the Argon2 key derivation function.

- Developer: added a non-const override of `CommandBase::Params::GetTags()` to allow the modification of tags in OnPreCommand.

- Fixed `--{disable,enable}-extras` not erroring when an non-existent extra module is specified.

- Fixed `<dnsbl:action>` not being matched case insensitively.

- Fixed a bunch of outdated and/or incorrect comments in the example configs.

- Fixed a bunch of warnings about deprecated copy constructors on C++11 compilers.

- Fixed a minor crash in the disable module when a nonexistent mode is specified.

- Fixed allowing many entries in `<limits>` to be set to 0 or more than the max line length.

- Fixed disconnecting users who try to enable user mode `x` (cloak) when the md5 module is not loaded.

- Fixed not using short module names (i.e. foo instead of m_foo) in a bunch of places.

- Fixed the `NAMELEN` 005 token not being used.

- Fixed the format of the `MAXLIST` 005 token.

- Fixed the syntax and help for the `/PING` command.

- Fixed xlines not being rechecked when a user's real hostname changes.

- Updated `./configure` to put store self-signed certificates in the .configure directory.

### InspIRCd 3.7.0

**This version of InspIRCd was released on 2020-07-31.**

- Added `<botmode:forcenotice>` to allow forcing bots to use NOTICEs instead of PRIVMSGs.

- Added a log message reminding admins that if they have defined a `<sslprofile>` tag they need to use the value of `<sslprofile:name>` in `<bind:ssl>` and `<link:ssl>` not the name of a TLS (SSL) module.

- Added a warning about LibreSSL support being deprecated.

- Added an error response when a user without the `users/mass-message` server operator privilege tries to send a mass-message.

- Added support for disabling client-to-client tags without disabling features which depend on the `message-tags` capability.

- Added support for disabling the creation/expiry notices sent to channel operators by the timedbans module.

- Added the --portable `./configure` option to build in portable mode.

- Added the `B` token to `/WHO` lines when the user in question is marked as a bot.

- Added the `inspircd-testssl` tool for checking whether a server is configured correctly for TLS (SSL) connections.

- Allowed server admins to disable the `/COMMANDS` command.

- Developer: added support for changing the type of a message in OnUserPreMessage.

- Developer: added the `BOT` 005 token to allow bots to automatically mark themselves as a bot.

- Fixed `/SVSHOLD` sending a global snotice instead of a local one.

- Fixed bcrypt and PBKDF2 hashes not being compared in a timing-safe way.

- Fixed building InspIRCd when the current working directory does not contain the source tree.

- Fixed shuns not being applied correctly.

- Fixed the `/SERVLIST` command not being documented in the example helpop config.

- Fixed the `<class:dnsbl>` option not matching marked DNSBL users.

- Fixed the `<hostchange:ports>` option never matching users.

- Fixed the ojoin module hardcoding the server operator mode instead of using a ModeReference.

- Fixed the systemd service depending on the Perl init script.

- Fixed WebSocket users not being detected as using a secure connection when they are.

- Removed support for TLSA record generation from inspircd-genssl (no clients adopted this).

- Removed the example config file for KiwiIRC as requested by upstream.

### InspIRCd 3.6.0

**This version of InspIRCd was released on 2020-04-24.**

- Added `<class:snomasks>` to allow configuring the snomasks that a server operator can use.

- Added `<include:noenv>` to disable using environment variables in an included config file.

- Added `<options:modesinlist>` to allow customising whether channel modes are included with the `/LIST` response.

- Added `<sasl:requiressl>` to require users to be connected via TLS (SSL) in order to be able to use SASL authentication.

- Added `<securelist:showmsg>` to configure whether the user should be told that they need to wait to run `/LIST`.

- Added support for [the IRCv3 SETNAME specification](https://ircv3.net/specs/extensions/setname.html).

- Added support for multi-line CAP responses.

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

- Developer: added the `inspircd.org/standard-replies` capability for opting-in to receiving IRCv3 Standard Replies instead of notices.

- Developer: deprecated the `XLineManager::InvokeStats` methods in favour of a new overload which uses a generic numeric.

- Developer: stabilised support for the [IRCv3 Standard Replies](https://ircv3.net/specs/extensions/standard-replies) specification.

- [Fixed a **crash** in the pgsql module when connecting to a server fails](/security/2020-01).

- Fixed a bug where previously changed display hostnames would be reset when a hostname lookup finishes.

- Fixed a bunch of typos with misspell-fixer.

- Fixed a memory leak in the dccallow module.

- Fixed a memory leak in the pgsql module.

- Fixed being able to use the `MODE` command to look up the modes of a private or secret channel.

- Fixed being unable to log in to server operator accounts using the ldapauth module.

- Fixed leaking HTTPd sockets if they were closed with data left in their outgoing buffer.

- Fixed leaking the value of some server operator config options when a user tries to log into an account which requires TLS (SSL) or a client certificate fingerprint.

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

- Improved the descriptions of all of the modules.

- Improved the error message shown when trying to load a module which is too old or too new for the current version.

- Improved the error messages shown by the ldap module.

- Improved the output of the `SSLINFO` command.

- Updated messages to refer to TLS as "TLS (SSL)" instead of SSL.

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

- Fixed a bug in `helpop.conf.example` where the swhois key was not using the correct value name.

- Fixed allowing `TAGMSG` messages to be sent without any tags attached.

- Fixed boolean configuration options not being matched in a case insensitive way.

- Fixed not using case insensitive comparisons for the `/DCCALLOW` subcommands.

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

- Fixed the legacy `/PROTOCTL NAMESX` command not using case insensitive matching.

- Fixed the legacy `/PROTOCTL UHNAMES` command not using case insensitive matching.

- Fixed the nationalchars module allowing nicknames which begin with a number.

- Fixed the nationalchars module not rebuilding the 005 numerics on unload.

- Fixed the nationalchars module not restoring the previous casemapping name on unload.

- Fixed the systemd unit file starting InspIRCd before the network is online.

- Fixed unnecessarily making `N*2-1` too many copies of the command arguments when processing a command with multiple targets.

- Improve the warning process when starting InspIRCd as root.

- Improved the ban message shown to users if they are banned by an extended ban.

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

* Developer: deprecated the ServerEventListener class and split the events contained within it into the `ServerProtocol::{BroadcastEventListener,LinkEventListener,SyncEventListener} classes.

* Developer: deprecated the `SerializeFormat` enum, and the `serialize`, `unserialize` methods of the `ExtensionItem` class, and the `LocalExtItem` class.

* [Fixed a **crash** in the MySQL module when built against mariadb-connector-c v3.0.5 or newer](/security/2019-02).

* Fixed allowing the `sasl` capability to be requested when the SASL server is offline.

* Fixed empty `/GLOBOPS` and `/WALLOPS` messages not failing with an `ERR_NOTEXTTOSEND` message.

* Fixed listener sockets with `<bind:replace>` enabled not being replaced in some circumstances.

* Fixed not applying IRCv3 `server-time` timestamps on the server the source is connecting from.

* Fixed not being able to use the `O` (oper) extended ban to server operators with a space in their server operator type.

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

- Fixed routing tags on `/TAGMSG` messages between servers.

- Fixed server operators with the `channels/auspex` privilege not being able to request the topic of secret/private channels with the `/TOPIC` command.

- Fixed the `/TAGMSG` message forwarding all tags regardless of whether they had been whitelisted.

- Fixed the `<connect:usests>` option being inverted.

- Fixed the autoop module checking the prefix mode add rank when removing list entries.

- Fixed the conn_umodes module setting user modes before the MOTD has been sent.

- Fixed the default log directory in system-wide mode to be `/var/log/inspircd`.

- Fixed the denychans module not checking whether the redirect channel is allowed properly.

- Fixed the exemptchanops module not validating list entries.

- Fixed the grammar of the error messages sent by the repeat module.

- Fixed the Perl helper script finding the location of the PID file.

- Fixed the sslinfo module not being able to place WebIRC users into the appropriate connect classes.

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

- Fixed the `MAXLIST` 005 token not reflecting the true lower limit.

- Fixed the parameters for the `/NAMES` command in the syntax hint and example helpop config.

- Raised the connection timeout in the example configs to 20s. This should give more time for clients on slow connections that want to do a lot of things (request caps, do SASL auth, etc) on connect.

- Silenced a harmless compiler warning in the pgsql module on newer GCCs.
