---
title: v4 Module List
---

{! 4/_support.md !}

## Module List

This is a complete list of all modules that ship with InspIRCd. If you have [installed from source](/4/installation/source) you can also install third-party modules which have been created by the InspIRCd community using the [Module Manager](/4/module-manager).

### Default Modules

These modules require no dependencies and will always be available.

Name                                                      | Description
--------------------------------------------------------- | -----------
[abbreviation](/4/modules/abbreviation)                   | Allows commands to be abbreviated by appending a full stop.
[account](/4/modules/account)                             | Adds various channel and user modes relating to accounts.
[alias](/4/modules/alias)                                 | Allows the server administrator to define custom channel commands (e.g. !kick) and server commands (e.g. /OPERSERV).
[allowinvite](/4/modules/allowinvite)                     | Adds channel mode A (allowinvite) which allows unprivileged users to use the /INVITE command and extended ban A: (blockinvite) which bans specific masks from using the /INVITE command.
[alltime](/4/modules/alltime)                             | Adds the /ALLTIME command which allows server operators to see the current UTC time on all of the servers on the network.
[anticaps](/4/modules/anticaps)                           | Adds channel mode B (anticaps) which allows channels to block messages which are excessively capitalised.
[auditorium](/4/modules/auditorium)                       | Adds channel mode u (auditorium) which hides unprivileged users in a channel from each other.
[autoop](/4/modules/autoop)                               | Adds channel mode w (autoop) which allows channel operators to define an access list which gives status ranks to users on join.
[banexception](/4/modules/banexception)                   | Adds channel mode e (banexception) which allows channel operators to exempt user masks from channel mode b (ban).
[banredirect](/4/modules/banredirect)                     | Allows specifying a channel to redirect a banned user to in the ban mask.
[bcrypt](/4/modules/bcrypt)                               | Allows other modules to generate bcrypt hashes.
[blockamsg](/4/modules/blockamsg)                         | Blocks mass messages sent using the /AME and /AMSG commands that exist in clients such as mIRC and HexChat.
[blockcolor](/4/modules/blockcolor)                       | Adds channel mode c (blockcolor) which allows channels to block messages which contain IRC formatting codes.
[botmode](/4/modules/botmode)                             | Adds user mode B (bot) which marks users with it set as bots in their /WHOIS response.
[callerid](/4/modules/callerid)                           | Provides user mode g (callerid) which allows users to require that other users are on their whitelist before messaging them.
[cap](/4/modules/cap)                                     | Implements support for the IRCv3 Client Capability Negotiation extension.
[cban](/4/modules/cban)                                   | Adds the /CBAN command which allows server operators to prevent channels matching a glob from being created.
[chancreate](/4/modules/chancreate)                       | Sends a notice to snomasks j (local) and J (remote) when a channel is created.
[chanfilter](/4/modules/chanfilter)                       | Adds channel mode g (filter) which allows channel operators to define glob patterns for inappropriate phrases that are not allowed to be used in the channel.
[chanhistory](/4/modules/chanhistory)                     | Adds channel mode H (history) which allows message history to be viewed on joining the channel.
[chanlog](/4/modules/chanlog)                             | Allows messages sent to snomasks to be logged to a channel.
[channames](/4/modules/channames)                         | Allows the server administrator to define what characters are allowed in channel names.
[channelban](/4/modules/channelban)                       | Adds extended ban j: (channel) which checks whether users are in a channel matching the specified glob pattern.
[check](/4/modules/check)                                 | Adds the /CHECK command which allows server operators to look up details about a channel, user, IP address, or hostname.
[chghost](/4/modules/chghost)                             | Adds the /CHGHOST command which allows server operators to change the displayed hostname of a user.
[chgident](/4/modules/chgident)                           | Adds the /CHGIDENT command which allows server operators to change the username (ident) of a user.
[chgname](/4/modules/chgname)                             | Adds the /CHGNAME command which allows server operators to change the real name of a user.
[classban](/4/modules/classban)                           | Adds extended ban n: (class) which check whether users are in a connect class matching the specified glob pattern.
[clearchan](/4/modules/clearchan)                         | Adds the /CLEARCHAN command which allows server operators to mass-punish the members of a channel.
[cloak](/4/modules/cloak)                                 | Adds user mode x (cloak) which allows user hostnames to be hidden.
[cloak_md5](/4/modules/cloak_md5)                         | This module adds the `half` and `full` cloaking methods for use with the cloak module.
[cloak_sha256](/4/modules/cloak_sha256)                   | This module adds the `hmac-sha256` and `hmac-sha256-ip` cloaking methods for use with the cloak module.
[codepage](/4/modules/codepage)                           | Allows the server administrator to define what characters are allowed in nicknames and how characters should be compared in a case insensitive way.
[commonchans](/4/modules/commonchans)                     | Adds user mode c (deaf_commonchan) which requires users to have a common channel before they can privately message each other.
[conn_join](/4/modules/conn_join)                         | Allows the server administrator to force users to join one or more channels on connect.
[conn_umodes](/4/modules/conn_umodes)                     | Allows the server administrator to set user modes on connecting users.
[conn_waitpong](/4/modules/conn_waitpong)                 | Requires all clients to respond to a PING request before they can fully connect.
[connectban](/4/modules/connectban)                       | Z-lines IP addresses which make excessive connections to the server.
[connflood](/4/modules/connflood)                         | Throttles excessive connections to the server.
[customprefix](/4/modules/customprefix)                   | Allows the server administrator to configure custom channel prefix modes.
[customtitle](/4/modules/customtitle)                     | Allows the server administrator to define accounts which can grant a custom title in /WHOIS and an optional virtual host.
[cycle](/4/modules/cycle)                                 | Allows channel members to part and rejoin a channel without needing to worry about channel modes such as +i (inviteonly) which might prevent rejoining.
[dccallow](/4/modules/dccallow)                           | Allows the server administrator to configure what files are allowed to be sent via DCC SEND and allows users to configure who can send them DCC CHAT and DCC SEND requests.
[deaf](/4/modules/deaf)                                   | Adds user mode d (deaf) which prevents users from receiving channel messages.
[delayjoin](/4/modules/delayjoin)                         | Adds channel mode D (delayjoin) which hides JOIN messages from users until they speak.
[delaymsg](/4/modules/delaymsg)                           | Adds channel mode d (delaymsg) which prevents newly joined users from speaking until the specified number of seconds have passed.
[denychans](/4/modules/denychans)                         | Allows the server administrator to prevent users from joining channels matching a glob.
[disable](/4/modules/disable)                             | Allows commands, channel modes, and user modes to be disabled.
[dnsbl](/4/modules/dnsbl)                                 | Allows the server administrator to check the IP address of connecting users against a DNSBL.
[exemptchanops](/4/modules/exemptchanops)                 | Adds channel mode X (exemptchanops) which allows channel operators to grant exemptions to various channel-level restrictions.
[filter](/4/modules/filter)                               | Adds the /FILTER command which allows server operators to define regex matches for inappropriate phrases that are not allowed to be used in channel messages, private messages, part messages, or quit messages.
[gateway](/4/modules/gateway)                             | Adds the ability for IRC gateways to forward the real IP address of users connecting through them.
[geoban](/4/modules/geoban)                               | Adds extended ban G: (country) which matches against two letter country codes.
[geoclass](/4/modules/geoclass)                           | Allows the server administrator to assign users to connect classes by the country they are connecting from.
[globalload](/4/modules/globalload)                       | Adds the /GLOADMODULE, /GRELOADMODULE, and /GUNLOADMODULE commands which allows server operators to load, reload, and unload modules on remote servers.
[globops](/4/modules/globops)                             | Adds the /GLOBOPS command which allows server operators to send messages to all server operators with the g (globops) snomask.
[haproxy](/4/modules/haproxy)                             | Allows IRC connections to be made using reverse proxies that implement the HAProxy PROXY protocol.
[helpop](/4/modules/helpop)                               | Adds the /HELPOP command which allows users to view help on various topics and user mode h (helpop) which marks a server operator as being available for help.
[hidechans](/4/modules/hidechans)                         | Adds user mode I (hidechans) which hides the channels users with it set are in from their /WHOIS response.
[hidelist](/4/modules/hidelist)                           | Allows list mode lists to be hidden from users without a prefix mode ranked equal to or higher than a defined level.
[hidemode](/4/modules/hidemode)                           | Allows mode changes to be hidden from users without a prefix mode ranked equal to or higher than a defined level.
[hideoper](/4/modules/hideoper)                           | Adds user mode H (hideoper) which hides the server operator status of a user from unprivileged users.
[hostchange](/4/modules/hostchange)                       | Allows the server administrator to define custom rules for applying hostnames to users.
[hostcycle](/4/modules/hostcycle)                         | Sends a fake disconnection and reconnection when a user's username (ident) or hostname changes to allow clients to update their internal caches.
[httpd](/4/modules/httpd)                                 | Allows the server administrator to serve various useful resources over HTTP.
[httpd_acl](/4/modules/httpd_acl)                         | Allows the server administrator to control who can access resources served over HTTP with the httpd module.
[httpd_config](/4/modules/httpd_config)                   | Allows the server configuration to be viewed over HTTP via the /config path.
[httpd_stats](/4/modules/httpd_stats)                     | Provides XML-serialised statistics about the server, channels, and users over HTTP via the /stats path.
[ident](/4/modules/ident)                                 | Allows the usernames (idents) of users to be looked up using the RFC 1413 Identification Protocol.
[inviteexception](/4/modules/inviteexception)             | Adds channel mode I (invex) which allows channel operators to exempt user masks from channel mode i (inviteonly).
[ircv3](/4/modules/ircv3)                                 | Provides the IRCv3 account-notify, away-notify, and extended-join client capabilities.
[ircv3_accounttag](/4/modules/ircv3_accounttag)           | Provides the IRCv3 account-tag client capability.
[ircv3_batch](/4/modules/ircv3_batch)                     | Provides the IRCv3 batch client capability.
[ircv3_capnotify](/4/modules/ircv3_capnotify)             | Provides the IRCv3 cap-notify client capability.
[ircv3_chghost](/4/modules/ircv3_chghost)                 | Provides the IRCv3 chghost client capability.
[ircv3_ctctags](/4/modules/ircv3_ctctags)                 | Provides the IRCv3 message-tags client capability.
[ircv3_echomessage](/4/modules/ircv3_echomessage)         | Provides the IRCv3 echo-message client capability.
[ircv3_invitenotify](/4/modules/ircv3_invitenotify)       | Provides the IRCv3 invite-notify client capability.
[ircv3_labeledresponse](/4/modules/ircv3_labeledresponse) | Provides support for the IRCv3 Labeled Response specification.
[ircv3_msgid](/4/modules/ircv3_msgid)                     | Provides support for the IRCv3 Message IDs specification.
[ircv3_servertime](/4/modules/ircv3_servertime)           | Provides the IRCv3 server-time client capability.
[ircv3_sts](/4/modules/ircv3_sts)                         | Adds support for the IRCv3 Strict Transport Security specification.
[joinflood](/4/modules/joinflood)                         | Adds channel mode j (joinflood) which helps protect against spammers which mass-join channels.
[kicknorejoin](/4/modules/kicknorejoin)                   | Adds channel mode J (kicknorejoin) which prevents users from rejoining after being kicked from a channel.
[knock](/4/modules/knock)                                 | Adds the /KNOCK command which allows users to request access to an invite-only channel and channel mode K (noknock) which allows channels to disable usage of this command.
[ldapauth](/4/modules/ldapauth)                           | Allows connecting users to be authenticated against an LDAP database.
[ldapoper](/4/modules/ldapoper)                           | Allows server operators to be authenticated against an LDAP database.
[log_sql](/4/modules/log_sql)                             | Provides the ability to write logs to an SQL database.
[maphide](/4/modules/maphide)                             | Allows the server administrator to replace the output of a /MAP and /LINKS with an URL.
[md5](/4/modules/md5)                                     | Allows other modules to generate MD5 hashes.
[messageflood](/4/modules/messageflood)                   | Adds channel mode f (flood) which helps protect against spammers which mass-message channels.
[mlock](/4/modules/mlock)                                 | Allows services to lock channel modes so that they can not be changed.
[monitor](/4/modules/monitor)                             | Adds the /MONITOR command which allows users to find out when their friends are connected to the server.
[muteban](/4/modules/muteban)                             | Adds extended ban m: (mute) which bans specific masks from speaking in a channel.
[namedmodes](/4/modules/namedmodes)                       | Provides support for adding and removing modes via their long names.
[namesx](/4/modules/namesx)                               | Provides the IRCv3 multi-prefix client capability.
[nickflood](/4/modules/nickflood)                         | Adds channel mode F (nickflood) which helps protect against spammers which mass-change nicknames.
[nicklock](/4/modules/nicklock)                           | Adds the /NICKLOCK command which allows server operators to change a user's nickname and prevent them from changing it again until they disconnect.
[noctcp](/4/modules/noctcp)                               | Adds channel mode C (noctcp) which allows channels to block messages which contain CTCPs and user mode T (u_noctcp) which allows users to block private messages that contain CTCPs.
[nokicks](/4/modules/nokicks)                             | Adds channel mode Q (nokick) which prevents privileged users from using the /KICK command.
[nonicks](/4/modules/nonicks)                             | Adds channel mode N (nonick) which prevents users from changing their nickname whilst in the channel.
[nonotice](/4/modules/nonotice)                           | Adds channel mode T (nonotice) which allows channels to block messages sent with the /NOTICE command.
[nopartmsg](/4/modules/nopartmsg)                         | Adds extended ban p: (partmsg) which blocks the part message of matching users.
[ojoin](/4/modules/ojoin)                                 | Adds the /OJOIN command which allows server operators to join a channel and receive the server operator-only Y (official-join) channel prefix mode.
[operchans](/4/modules/operchans)                         | Adds channel mode O (operonly) which prevents non-server operators from joining the channel.
[operjoin](/4/modules/operjoin)                           | Allows the server administrator to force server operators to join one or more channels when logging into their server operator account.
[operlevels](/4/modules/operlevels)                       | Allows the server administrator to define ranks for server operators which prevent lower ranked server operators from using /KILL on higher ranked server operators.
[operlog](/4/modules/operlog)                             | Allows the server administrator to make the server log when a server operator-only command is executed.
[opermodes](/4/modules/opermodes)                         | Allows the server administrator to set user modes on server operators when they log into their server operator account.
[opermotd](/4/modules/opermotd)                           | Adds the /OPERMOTD command which adds a special message of the day for server operators.
[operprefix](/4/modules/operprefix)                       | Adds the server operator-only y (operprefix) channel prefix mode.
[opmoderated](/4/modules/opmoderated)                     | Adds the ability for IRC gateways to forward the real IP address of users connecting through them.
[override](/4/modules/override)                           | Allows server operators to be given privileges that allow them to ignore various channel-level restrictions.
[passforward](/4/modules/passforward)                     | Allows an account password to be forwarded to a services pseudoclient such as NickServ.
[password_hash](/4/modules/password_hash)                 | Allows passwords to be hashed and adds the /MKPASSWD command which allows the generation of hashed passwords for use in the server configuration.
[pbkdf2](/4/modules/pbkdf2)                               | Allows other modules to generate PBKDF2 hashes.
[permchannels](/4/modules/permchannels)                   | Adds channel mode P (permanent) which prevents the channel from being deleted when the last user leaves.
[randquote](/4/modules/randquote)                         | Allows random quotes to be sent to users when they connect to the server.
[realnameban](/4/modules/realnameban)                     | Adds extended bans a: (realmask) and r:(realname) which checks whether users have a real name matching the specified glob pattern.
[redirect](/4/modules/redirect)                           | Allows users to be redirected to another channel when the user limit is reached.
[regex_glob](/4/modules/regex_glob)                       | Provides the glob regular expression engine which uses the built-in glob matching system.
[regex_stdlib](/4/modules/regex_stdlib)                   | Provides the stdregex regular expression engine which uses the C++11 std::regex regular expression matching system.
[remove](/4/modules/remove)                               | Adds the /REMOVE command which allows channel operators to force part users from a channel.
[repeat](/4/modules/repeat)                               | Adds channel mode E (repeat) which helps protect against spammers which spam the same message repeatedly.
[restrictchans](/4/modules/restrictchans)                 | Prevents unprivileged users from creating new channels.
[restrictmsg](/4/modules/restrictmsg)                     | Prevents users who are not server operators from messaging each other.
[rline](/4/modules/rline)                                 | Adds the /RLINE command which allows server operators to prevent users matching a nickname!username@hostname+realname regular expression from connecting to the server.
[rmode](/4/modules/rmode)                                 | Allows removal of channel list modes using glob patterns.
[sajoin](/4/modules/sajoin)                               | Adds the /SAJOIN command which allows server operators to force users to join one or more channels.
[sakick](/4/modules/sakick)                               | Adds the /SAKICK command which allows server operators to kick users from a channel without having any privileges in the channel.
[samode](/4/modules/samode)                               | Adds the /SAMODE command which allows server operators to change the modes of a target (channel, user) that they would not otherwise have the privileges to change.
[sanick](/4/modules/sanick)                               | Adds the /SANICK command which allows server operators to change the nickname of a user.
[sapart](/4/modules/sapart)                               | Adds the /SAPART command which allows server operators to force part users from one or more channels without having any privileges in these channels.
[saquit](/4/modules/saquit)                               | Adds the /SAQUIT command which allows server operators to disconnect users from the server.
[sasl](/4/modules/sasl)                                   | Provides the IRCv3 sasl client capability.
[satopic](/4/modules/satopic)                             | Adds the /SATOPIC command which allows server operators to change the topic of a channel that they would not otherwise have the privileges to change.
[securelist](/4/modules/securelist)                       | Prevents users from using the /LIST command until a predefined period has passed.
[seenicks](/4/modules/seenicks)                           | Sends a notice to snomasks n (local) and N (remote) when a user changes their nickname.
[serverban](/4/modules/serverban)                         | Adds extended ban s: (server) which check whether users are on a server matching the specified glob pattern.
[services](/4/modules/services)                           | Provides support for integrating with a services server.
[servprotect](/4/modules/servprotect)                     | Adds user mode k (servprotect) which protects services pseudoclients from being kicked, being killed, or having their channel prefix modes changed.
[sethost](/4/modules/sethost)                             | Adds the /SETHOST command which allows server operators to change their displayed hostname.
[setident](/4/modules/setident)                           | Adds the /SETIDENT command which allows server operators to change their username (ident).
[setidle](/4/modules/setidle)                             | Adds the /SETIDLE command which allows server operators to change their idle time.
[setname](/4/modules/setname)                             | Adds the /SETNAME command which allows users to change their real name.
[sha1](/4/modules/sha1)                                   | Allows other modules to generate SHA-1 hashes.
[sha2](/4/modules/sha2)                                   | Allows other modules to generate SHA-2 hashes.
[showfile](/4/modules/showfile)                           | Adds support for showing the contents of files to users when they execute a command.
[showwhois](/4/modules/showwhois)                         | Adds user mode W (showwhois) which allows users to be informed when someone does a /WHOIS query on their nick.
[shun](/4/modules/shun)                                   | Adds the /SHUN command which allows server operators to prevent users from executing commands.
[silence](/4/modules/silence)                             | Adds the /SILENCE command which allows users to ignore other users on server-side.
[spanningtree](/4/modules/spanningtree)                   | Allows linking multiple servers together as part of one network.
[sqlauth](/4/modules/sqlauth)                             | Allows connecting users to be authenticated against an arbitrary SQL table.
[sqloper](/4/modules/sqloper)                             | Allows server operators to be authenticated against an SQL table.
[sslinfo](/4/modules/sslinfo)                             | Adds user facing TLS information, various TLS configuration options, and the /SSLINFO command to look up TLS certificate information for other users.
[sslmodes](/4/modules/sslmodes)                           | Adds channel mode z (sslonly) which prevents users who are not connecting using TLS from joining the channel and user mode z (sslqueries) to prevent messages from non-TLS users.
[starttls](/4/modules/starttls)                           | Provides the IRCv3 tls client capability.
[stripcolor](/4/modules/stripcolor)                       | Adds channel mode S (stripcolor) which allows channels to strip IRC formatting codes from messages.
[svshold](/4/modules/svshold)                             | Adds the /SVSHOLD command which allows services to reserve nicknames.
[swhois](/4/modules/swhois)                               | Adds the /SWHOIS command which adds custom lines to a user's WHOIS response.
[timedbans](/4/modules/timedbans)                         | Adds the /TBAN command which allows channel operators to add bans which will be expired after the specified period.
[tline](/4/modules/tline)                                 | Adds the /TLINE command which allows server operators to determine how many users would be affected by an X-line on a specified pattern.
[topiclock](/4/modules/topiclock)                         | Allows services to lock the channel topic so that it can not be changed.
[uhnames](/4/modules/uhnames)                             | Provides the IRCv3 userhost-in-names client capability.
[uninvite](/4/modules/uninvite)                           | Adds the /UNINVITE command which allows users who have invited another user to a channel to withdraw their invite.
[vhost](/4/modules/vhost)                                 | Allows the server administrator to define accounts which can grant a custom virtual host.
[watch](/4/modules/watch)                                 | Adds the /WATCH command which allows users to find out when their friends are connected to the server.
[websocket](/4/modules/websocket)                         | Allows WebSocket clients to connect to the IRC server.
[xline_db](/4/modules/xline_db)                           | Allows X-lines to be saved and reloaded on restart.

### Extra Modules

These modules require third-party dependencies to be installed and have to be enabled at compile time. See the specific module page for details on how to enable these.

Name                                          | Description
--------------------------------------------- | -----------
[argon2](/4/modules/argon2)                   | Allows other modules to generate Argon2 hashes.
[geo_maxmind](/4/modules/geo_maxmind)         | Allows the server to perform geolocation lookups on both IP addresses and users.
[ldap](/4/modules/ldap)                       | Provides the ability for LDAP modules to query a LDAP directory.
[log_json](/4/modules/log_json)               | Provides the ability to write logs to a JSON file.
[log_syslog](/4/modules/log_syslog)           | Provides the ability to write logs to syslog.
[mysql](/4/modules/mysql)                     | Provides the ability for SQL modules to query a MySQL database.
[pgsql](/4/modules/pgsql)                     | Provides the ability for SQL modules to query a PostgreSQL database.
[regex_pcre](/4/modules/regex_pcre)           | Provides the pcre regular expression engine which uses the PCRE library.
[regex_posix](/4/modules/regex_posix)         | Provides the posix regular expression engine which uses the POSIX.2 regular expression matching system.
[regex_re2](/4/modules/regex_re2)             | Provides the re2 regular expression engine which uses the RE2 library.
[sqlite3](/4/modules/sqlite3)                 | Provides the ability for SQL modules to query a SQLite 3 database.
[ssl_gnutls](/4/modules/ssl_gnutls)           | Allows TLS encrypted connections using the GnuTLS library.
[ssl_mbedtls](/4/modules/ssl_mbedtls)         | Allows TLS encrypted connections using the mbedTLS library.
[ssl_openssl](/4/modules/ssl_openssl)         | Allows TLS encrypted connections using the OpenSSL library.
[sslrehashsignal](/4/modules/sslrehashsignal) | Allows the SIGUSR1 signal to be sent to the server to reload TLS certificates.
