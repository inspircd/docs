---
title: v{{ version }} Module List
---

## Module List

This is a complete list of all modules that ship with InspIRCd. If you have [installed from source](/3/installation/source) you can also install third-party modules which have been created by the InspIRCd community using the [Module Manager](/3/module-manager).

### Default Modules

These modules require no dependencies and will always be available.

Name                                                      | Description
--------------------------------------------------------- | -----------
[abbreviation](/3/modules/abbreviation)                   | Allows commands to be abbreviated by appending a full stop.
[alias](/3/modules/alias)                                 | Allows the server administrator to define custom channel commands (e.g. !kick) and server commands (e.g. /OPERSERV).
[allowinvite](/3/modules/allowinvite)                     | Adds channel mode A (allowinvite) which allows unprivileged users to use the /INVITE command and extended ban A which bans specific masks from using the /INVITE command.
[alltime](/3/modules/alltime)                             | Adds the /ALLTIME command which allows server operators to see the current UTC time on all of the servers on the network.
[anticaps](/3/modules/anticaps)                           | Adds channel mode B (anticaps) which allows channels to block messages which are excessively capitalised.
[auditorium](/3/modules/auditorium)                       | Adds channel mode u (auditorium) which hides unprivileged users in a channel from each other.
[autoop](/3/modules/autoop)                               | Adds channel mode w (autoop) which allows channel operators to define an access list which gives status ranks to users on join.
[banexception](/3/modules/banexception)                   | Adds channel mode e (banexception) which allows channel operators to exempt user masks from the b (ban) channel mode.
[banredirect](/3/modules/banredirect)                     | Allows specifying a channel to redirect a banned user to in the ban mask.
[bcrypt](/3/modules/bcrypt)                               | Allows other modules to generate bcrypt hashes.
[blockamsg](/3/modules/blockamsg)                         | Blocks mass messages sent using the /AME and /AMSG commands that exist in clients such as mIRC and HexChat.
[blockcaps](/3/modules/blockcaps)                         | Adds channel mode B (blockcaps) which allows channels to block messages which are excessively capitalised.
[blockcolor](/3/modules/blockcolor)                       | Adds channel mode c (blockcolor) which allows channels to block messages which contain IRC formatting codes.
[botmode](/3/modules/botmode)                             | Adds user mode B (bot) which marks users with it set as bots in their /WHOIS response.
[callerid](/3/modules/callerid)                           | Provides user mode g (callerid) which allows users to require that other users are on their whitelist before messaging them.
[cap](/3/modules/cap)                                     | Implements support for the IRCv3 Client Capability Negotiation extension.
[cban](/3/modules/cban)                                   | Adds the /CBAN command which allows server operators to prevent channels matching a glob from being created.
[censor](/3/modules/censor)                               | Allows the server administrator to define inappropriate phrases that are not allowed to be used in private or channel messages.
[cgiirc](/3/modules/cgiirc)                               | Adds the ability for IRC gateways to forward the real IP address of users connecting through them.
[chancreate](/3/modules/chancreate)                       | Sends a notice to snomasks j (local) and J (remote) when a channel is created.
[chanfilter](/3/modules/chanfilter)                       | Adds channel mode g (filter) which allows channel operators to define glob patterns for inappropriate phrases that are not allowed to be used in the channel.
[chanhistory](/3/modules/chanhistory)                     | Adds channel mode H (history) which allows message history to be viewed on joining the channel.
[chanlog](/3/modules/chanlog)                             | Allows messages sent to snomasks to be logged to a channel.
[channames](/3/modules/channames)                         | Allows the server administrator to define what characters are allowed in channel names.
[channelban](/3/modules/channelban)                       | Adds the j extended ban which checks whether users are in a channel matching the specified glob pattern.
[check](/3/modules/check)                                 | Adds the /CHECK command which allows server operators to look up details about a channel, user, IP address, or hostname.
[chghost](/3/modules/chghost)                             | Adds the /CHGHOST command which allows server operators to change the displayed hostname of a user.
[chgident](/3/modules/chgident)                           | Adds the /CHGIDENT command which allows server operators to change the username (ident) of a user.
[chgname](/3/modules/chgname)                             | Adds the /CHGNAME command which allows server operators to change the real name (gecos) of a user.
[classban](/3/modules/classban)                           | Adds the n extended ban which check whether users are in a connect class matching the specified glob pattern.
[clearchan](/3/modules/clearchan)                         | Adds the /CLEARCHAN command which allows server operators to mass-punish the members of a channel.
[cloaking](/3/modules/cloaking)                           | Adds user mode x (cloak) which allows user hostnames to be hidden.
[clones](/3/modules/clones)                               | Adds the /CLONES command which allows server operators to view IP addresses from which there are more than a specified number of connections.
[codepage](/3/modules/codepage)                           | Allows the server administrator to define what characters are allowed in nicknames and how characters should be compared in a case insensitive way.
[commonchans](/3/modules/commonchans)                     | Adds user mode c (deaf_commonchan) which requires users to have a common channel before they can privately message each other.
[conn_join](/3/modules/conn_join)                         | Allows the server administrator to force users to join one or more channels on connect.
[conn_umodes](/3/modules/conn_umodes)                     | Allows the server administrator to set user modes on connecting users.
[conn_waitpong](/3/modules/conn_waitpong)                 | Requires all clients to respond to a PING request before they can fully connect.
[connectban](/3/modules/connectban)                       | Z-lines IP addresses which make excessive connections to the server.
[connflood](/3/modules/connflood)                         | Throttles excessive connections to the server.
[customprefix](/3/modules/customprefix)                   | Allows the server administrator to configure custom channel prefix modes.
[customtitle](/3/modules/customtitle)                     | Allows the server administrator to define accounts which can grant a custom title in /WHOIS and an optional virtual host.
[cycle](/3/modules/cycle)                                 | Allows channel members to part and rejoin a channel without needing to worry about channel modes such as +i (inviteonly) which might prevent rejoining.
[dccallow](/3/modules/dccallow)                           | Allows the server administrator to configure what files are allowed to be sent via DCC SEND and allows users to configure who can send them DCC CHAT and DCC SEND requests.
[deaf](/3/modules/deaf)                                   | Adds user modes d (deaf) and D (privdeaf) which prevents users from receiving channel (deaf) or private (privdeaf) messages.
[delayjoin](/3/modules/delayjoin)                         | Adds channel mode D (delayjoin) which hides JOIN messages from users until they speak.
[delaymsg](/3/modules/delaymsg)                           | Adds channel mode d (delaymsg) which prevents newly joined users from speaking until the specified number of seconds have passed.
[denychans](/3/modules/denychans)                         | Allows the server administrator to prevent users from joining channels matching a glob.
[disable](/3/modules/disable)                             | Allows commands, channel modes, and user modes to be disabled.
[dnsbl](/3/modules/dnsbl)                                 | Allows the server administrator to check the IP address of connecting users against a DNSBL.
[exemptchanops](/3/modules/exemptchanops)                 | Adds channel mode X (exemptchanops) which allows channel operators to grant exemptions to various channel-level restrictions.
[filter](/3/modules/filter)                               | Adds the /FILTER command which allows server operators to define regex matches for inappropriate phrases that are not allowed to be used in channel messages, private messages, part messages, or quit messages.
[flashpolicyd](/3/modules/flashpolicyd)                   | Allows connection policies to be served to IRC clients that use Adobe Flash.
[gecosban](/3/modules/gecosban)                           | Adds the r extended ban which checks whether users have a real name (gecos) matching the specified glob pattern.
[geoban](/3/modules/geoban)                               | Adds extended ban G which matches against two letter country codes.
[geoclass](/3/modules/geoclass)                           | Allows the server administrator to assign users to connect classes by the country they are connecting from.
[globalload](/3/modules/globalload)                       | Adds the /GLOADMODULE, /GRELOADMODULE, and /GUNLOADMODULE commands which allows server operators to load, reload, and unload modules on remote servers.
[globops](/3/modules/globops)                             | Adds the /GLOBOPS command which allows server operators to send messages to all server operators with the g (globops) snomask.
[haproxy](/3/modules/haproxy)                             | Allows IRC connections to be made using reverse proxies that implement the HAProxy PROXY protocol.
[helpop](/3/modules/helpop)                               | Adds the /HELPOP command which allows users to view help on various topics and user mode h (helpop) which marks a server operator as being available for help.
[hidechans](/3/modules/hidechans)                         | Adds user mode I (hidechans) which hides the channels users with it set are in from their /WHOIS response.
[hidelist](/3/modules/hidelist)                           | Allows list mode lists to be hidden from users without a prefix mode ranked equal to or higher than a defined level.
[hidemode](/3/modules/hidemode)                           | Allows mode changes to be hidden from users without a prefix mode ranked equal to or higher than a defined level.
[hideoper](/3/modules/hideoper)                           | Adds user mode H (hideoper) which hides the server operator status of a user from unprivileged users.
[hostchange](/3/modules/hostchange)                       | Allows the server administrator to define custom rules for applying hostnames to users.
[hostcycle](/3/modules/hostcycle)                         | Sends a fake disconnection and reconnection when a user's username (ident) or hostname changes to allow clients to update their internal caches.
[httpd](/3/modules/httpd)                                 | Allows the server administrator to serve various useful resources over HTTP.
[httpd_acl](/3/modules/httpd_acl)                         | Allows the server administrator to control who can access resources served over HTTP with the httpd module.
[httpd_config](/3/modules/httpd_config)                   | Allows the server configuration to be viewed over HTTP via the /config path.
[httpd_stats](/3/modules/httpd_stats)                     | Provides XML-serialised statistics about the server, channels, and users over HTTP via the /stats path.
[ident](/3/modules/ident)                                 | Allows the usernames (idents) of users to be looked up using the RFC 1413 Identification Protocol.
[inviteexception](/3/modules/inviteexception)             | Adds channel mode I (invex) which allows channel operators to exempt user masks from the i (inviteonly) channel mode.
[ircv3](/3/modules/ircv3)                                 | Provides the IRCv3 account-notify, away-notify, and extended-join client capabilities.
[ircv3_accounttag](/3/modules/ircv3_accounttag)           | Provides the IRCv3 account-tag client capability.
[ircv3_batch](/3/modules/ircv3_batch)                     | Provides the IRCv3 batch client capability.
[ircv3_capnotify](/3/modules/ircv3_capnotify)             | Provides the IRCv3 cap-notify client capability.
[ircv3_chghost](/3/modules/ircv3_chghost)                 | Provides the IRCv3 chghost client capability.
[ircv3_ctctags](/3/modules/ircv3_ctctags)                 | Provides the IRCv3 message-tags client capability.
[ircv3_echomessage](/3/modules/ircv3_echomessage)         | Provides the IRCv3 echo-message client capability.
[ircv3_invitenotify](/3/modules/ircv3_invitenotify)       | Provides the IRCv3 invite-notify client capability.
[ircv3_labeledresponse](/3/modules/ircv3_labeledresponse) | Provides support for the IRCv3 Labeled Response specification.
[ircv3_msgid](/3/modules/ircv3_msgid)                     | Provides support for the IRCv3 Message IDs specification.
[ircv3_servertime](/3/modules/ircv3_servertime)           | Provides the IRCv3 server-time client capability.
[ircv3_sts](/3/modules/ircv3_sts)                         | Adds support for the IRCv3 Strict Transport Security specification.
[joinflood](/3/modules/joinflood)                         | Adds channel mode j (joinflood) which helps protect against spammers which mass-join channels.
[kicknorejoin](/3/modules/kicknorejoin)                   | Adds channel mode J (kicknorejoin) which prevents users from rejoining after being kicked from a channel.
[knock](/3/modules/knock)                                 | Adds the /KNOCK command which allows users to request access to an invite-only channel and channel mode K (noknock) which allows channels to disable usage of this command.
[ldapauth](/3/modules/ldapauth)                           | Allows connecting users to be authenticated against an LDAP database.
[ldapoper](/3/modules/ldapoper)                           | Allows server operators to be authenticated against an LDAP database.
[lockserv](/3/modules/lockserv)                           | Adds the /LOCKSERV and /UNLOCKSERV commands which allows server operators to control whether users can connect to the local server.
[maphide](/3/modules/maphide)                             | Allows the server administrator to replace the output of a /MAP and /LINKS with an URL.
[md5](/3/modules/md5)                                     | Allows other modules to generate MD5 hashes.
[messageflood](/3/modules/messageflood)                   | Adds channel mode f (flood) which helps protect against spammers which mass-message channels.
[mlock](/3/modules/mlock)                                 | Allows services to lock channel modes so that they can not be changed.
[modenotice](/3/modules/modenotice)                       | Adds the /MODENOTICE command which sends a message to all users with the specified user modes set.
[monitor](/3/modules/monitor)                             | Adds the /MONITOR command which allows users to find out when their friends are connected to the server.
[muteban](/3/modules/muteban)                             | Adds extended ban m which bans specific masks from speaking in a channel.
[namedmodes](/3/modules/namedmodes)                       | Provides support for adding and removing modes via their long names.
[namesx](/3/modules/namesx)                               | Provides the IRCv3 multi-prefix client capability.
[nationalchars](/3/modules/nationalchars)                 | Allows the server administrator to define what characters are allowed in nicknames and channel names and how those characters should be compared in a case insensitive way.
[nickflood](/3/modules/nickflood)                         | Adds channel mode F (nickflood) which helps protect against spammers which mass-change nicknames.
[nicklock](/3/modules/nicklock)                           | Adds the /NICKLOCK command which allows server operators to change a user's nickname and prevent them from changing it again until they disconnect.
[noctcp](/3/modules/noctcp)                               | Adds channel mode C (noctcp) which allows channels to block messages which contain CTCPs and user mode T (u_noctcp) which allows users to block private messages that contain CTCPs.
[nokicks](/3/modules/nokicks)                             | Adds channel mode Q (nokick) which prevents privileged users from using the /KICK command.
[nonicks](/3/modules/nonicks)                             | Adds channel mode N (nonick) which prevents users from changing their nickname whilst in the channel.
[nonotice](/3/modules/nonotice)                           | Adds channel mode T (nonotice) which allows channels to block messages sent with the /NOTICE command.
[nopartmsg](/3/modules/nopartmsg)                         | Adds the p extended ban which blocks the part message of matching users.
[ojoin](/3/modules/ojoin)                                 | Adds the /OJOIN command which allows server operators to join a channel and receive the server operator-only Y (official-join) channel prefix mode.
[operchans](/3/modules/operchans)                         | Adds channel mode O (operonly) which prevents non-server operators from joining the channel.
[operjoin](/3/modules/operjoin)                           | Allows the server administrator to force server operators to join one or more channels when logging into their server operator account.
[operlevels](/3/modules/operlevels)                       | Allows the server administrator to define ranks for server operators which prevent lower ranked server operators from using /KILL on higher ranked server operators.
[operlog](/3/modules/operlog)                             | Allows the server administrator to make the server log when a server operator-only command is executed.
[opermodes](/3/modules/opermodes)                         | Allows the server administrator to set user modes on server operators when they log into their server operator account.
[opermotd](/3/modules/opermotd)                           | Adds the /OPERMOTD command which adds a special message of the day for server operators.
[operprefix](/3/modules/operprefix)                       | Adds the server operator-only y (operprefix) channel prefix mode.
[override](/3/modules/override)                           | Allows server operators to be given privileges that allow them to ignore various channel-level restrictions.
[passforward](/3/modules/passforward)                     | Allows the /PASS password to be forwarded to a services pseudoclient such as NickServ.
[password_hash](/3/modules/password_hash)                 | Adds the /MKPASSWD command which allows the generation of hashed passwords for use in the server configuration.
[pbkdf2](/3/modules/pbkdf2)                               | Allows other modules to generate PBKDF2 hashes.
[permchannels](/3/modules/permchannels)                   | Adds channel mode P (permanent) which prevents the channel from being deleted when the last user leaves.
[randquote](/3/modules/randquote)                         | Allows random quotes to be sent to users when they connect to the server.
[redirect](/3/modules/redirect)                           | Allows users to be redirected to another channel when the user limit is reached.
[regex_glob](/3/modules/regex_glob)                       | Provides a regular expression engine which uses the built-in glob matching system.
[remove](/3/modules/remove)                               | Adds the /FPART and /REMOVE commands which allows channel operators to force part users from a channel.
[repeat](/3/modules/repeat)                               | Adds channel mode E (repeat) which helps protect against spammers which spam the same message repeatedly.
[restrictchans](/3/modules/restrictchans)                 | Prevents unprivileged users from creating new channels.
[restrictmsg](/3/modules/restrictmsg)                     | Prevents users who are not server operators from messaging each other.
[rline](/3/modules/rline)                                 | Adds the /RLINE command which allows server operators to prevent users matching a nickname!username@hostname+realname regular expression from connecting to the server.
[rmode](/3/modules/rmode)                                 | Allows removal of channel list modes using glob patterns.
[sajoin](/3/modules/sajoin)                               | Adds the /SAJOIN command which allows server operators to force users to join one or more channels.
[sakick](/3/modules/sakick)                               | Adds the /SAKICK command which allows server operators to kick users from a channel without having any privileges in the channel.
[samode](/3/modules/samode)                               | Adds the /SAMODE command which allows server operators to change the modes of a target (channel, user) that they would not otherwise have the privileges to change.
[sanick](/3/modules/sanick)                               | Adds the /SANICK command which allows server operators to change the nickname of a user.
[sapart](/3/modules/sapart)                               | Adds the /SAPART command which allows server operators to force part users from one or more channels without having any privileges in these channels.
[saquit](/3/modules/saquit)                               | Adds the /SAQUIT command which allows server operators to disconnect users from the server.
[sasl](/3/modules/sasl)                                   | Provides the IRCv3 sasl client capability.
[satopic](/3/modules/satopic)                             | Adds the /SATOPIC command which allows server operators to change the topic of a channel that they would not otherwise have the privileges to change.
[securelist](/3/modules/securelist)                       | Prevents users from using the /LIST command until a predefined period has passed.
[seenicks](/3/modules/seenicks)                           | Sends a notice to snomasks n (local) and N (remote) when a user changes their nickname.
[serverban](/3/modules/serverban)                         | Adds the s extended ban which check whether users are on a server matching the specified glob pattern.
[services_account](/3/modules/services_account)           | Adds various channel and user modes relating to services accounts.
[servprotect](/3/modules/servprotect)                     | Adds user mode k (servprotect) which protects services pseudoclients from being kicked, being killed, or having their channel prefix modes changed.
[sethost](/3/modules/sethost)                             | Adds the /SETHOST command which allows server operators to change their displayed hostname.
[setident](/3/modules/setident)                           | Adds the /SETIDENT command which allows server operators to change their username (ident).
[setidle](/3/modules/setidle)                             | Adds the /SETIDLE command which allows server operators to change their idle time.
[setname](/3/modules/setname)                             | Adds the /SETNAME command which allows users to change their real name (gecos).
[sha1](/3/modules/sha1)                                   | Allows other modules to generate SHA-1 hashes.
[sha256](/3/modules/sha256)                               | Allows other modules to generate SHA-256 hashes.
[showfile](/3/modules/showfile)                           | Adds support for showing the contents of files to users when they execute a command.
[showwhois](/3/modules/showwhois)                         | Adds user mode W (showwhois) which allows users to be informed when someone does a /WHOIS query on their nick.
[shun](/3/modules/shun)                                   | Adds the /SHUN command which allows server operators to prevent users from executing commands.
[silence](/3/modules/silence)                             | Adds the /SILENCE command which allows users to ignore other users on server-side.
[spanningtree](/3/modules/spanningtree)                   | Allows linking multiple servers together as part of one network.
[sqlauth](/3/modules/sqlauth)                             | Allows connecting users to be authenticated against an arbitrary SQL table.
[sqloper](/3/modules/sqloper)                             | Allows server operators to be authenticated against an SQL table.
[sslinfo](/3/modules/sslinfo)                             | Adds user facing TLS (SSL) information, various TLS (SSL) configuration options, and the /SSLINFO command to look up TLS (SSL) certificate information for other users.
[sslmodes](/3/modules/sslmodes)                           | Adds channel mode z (sslonly) which prevents users who are not connecting using TLS (SSL) from joining the channel and user mode z (sslqueries) to prevent messages from non-TLS (SSL) users.
[starttls](/3/modules/starttls)                           | Provides the IRCv3 tls client capability.
[stripcolor](/3/modules/stripcolor)                       | Adds channel mode S (stripcolor) which allows channels to strip IRC formatting codes from messages.
[svshold](/3/modules/svshold)                             | Adds the /SVSHOLD command which allows services to reserve nicknames.
[swhois](/3/modules/swhois)                               | Adds the /SWHOIS command which adds custom lines to a user's WHOIS response.
[timedbans](/3/modules/timedbans)                         | Adds the /TBAN command which allows channel operators to add bans which will be expired after the specified period.
[tline](/3/modules/tline)                                 | Adds the /TLINE command which allows server operators to determine how many users would be affected by an X-line on a specified pattern.
[topiclock](/3/modules/topiclock)                         | Allows services to lock the channel topic so that it can not be changed.
[uhnames](/3/modules/uhnames)                             | Provides the IRCv3 userhost-in-names client capability.
[uninvite](/3/modules/uninvite)                           | Adds the /UNINVITE command which allows users who have invited another user to a channel to withdraw their invite.
[userip](/3/modules/userip)                               | Adds the /USERIP command which allows users to find out the IP address of one or more connected users.
[vhost](/3/modules/vhost)                                 | Allows the server administrator to define accounts which can grant a custom virtual host.
[watch](/3/modules/watch)                                 | Adds the /WATCH command which allows users to find out when their friends are connected to the server.
[websocket](/3/modules/websocket)                         | Allows WebSocket clients to connect to the IRC server.
[xline_db](/3/modules/xline_db)                           | Allows X-lines to be saved and reloaded on restart.

### Extra Modules

These modules require third-party dependencies to be installed and have to be enabled at compile time. See the specific module page for details on how to enable these.

Name                                          | Description
--------------------------------------------- | -----------
[argon2](/3/modules/argon2)                   | Allows other modules to generate Argon2 hashes.
[geo_maxmind](/3/modules/geo_maxmind)         | Allows the server to perform geolocation lookups on both IP addresses and users.
[ldap](/3/modules/ldap)                       | Provides the ability for LDAP modules to query a LDAP directory.
[mysql](/3/modules/mysql)                     | Provides the ability for SQL modules to query a MySQL database.
[pgsql](/3/modules/pgsql)                     | Provides the ability for SQL modules to query a PostgreSQL database.
[regex_pcre](/3/modules/regex_pcre)           | Provides a regular expression engine which uses the PCRE library.
[regex_posix](/3/modules/regex_posix)         | Provides a regular expression engine which uses the POSIX.2 regular expression matching system.
[regex_re2](/3/modules/regex_re2)             | Provides a regular expression engine which uses the RE2 library.
[regex_stdlib](/3/modules/regex_stdlib)       | Provides a regular expression engine which uses the C++11 std::regex regular expression matching system.
[regex_tre](/3/modules/regex_tre)             | Provides a regular expression engine which uses the TRE library.
[sqlite3](/3/modules/sqlite3)                 | Provides the ability for SQL modules to query a SQLite 3 database.
[ssl_gnutls](/3/modules/ssl_gnutls)           | Allows TLS (SSL) encrypted connections using the GnuTLS library.
[ssl_mbedtls](/3/modules/ssl_mbedtls)         | Allows TLS (SSL) encrypted connections using the mbedTLS library.
[ssl_openssl](/3/modules/ssl_openssl)         | Allows TLS (SSL) encrypted connections using the OpenSSL library.
[sslrehashsignal](/3/modules/sslrehashsignal) | Allows the SIGUSR1 signal to be sent to the server to reload TLS (SSL) certificates.
