---
title: Module List
---

## Module List

This is a complete list of all modules that ship with InspIRCd. If you have [installed from source](/3/installation/source) you can also install third-party modules which have been created by the InspIRCd community using the [Module Manager](/3/module-manager).

### Default Modules

These modules require no dependencies and will always be available.

Name                                                | Description
--------------------------------------------------- | -----------
[abbreviation](/3/modules/abbreviation)             | Provides the ability to abbreviate commands a-la BBC BASIC keywords
[alias](/3/modules/alias)                           | Provides aliases of commands
[allowinvite](/3/modules/allowinvite)               | Provides channel mode +A to allow /INVITE freely on a channel, and extban 'A' to deny specific users it
[alltime](/3/modules/alltime)                       | Provides the ALLTIME command, displays timestamps from all servers connected to the network
[anticaps](/3/modules/anticaps)                     | Provides support for punishing users that send capitalised messages
[auditorium](/3/modules/auditorium)                 | Provides channel mode +u, auditorium channels where nobody can see others joining and parting or the nick list
[autoop](/3/modules/autoop)                         | Provides channel mode +w, basic channel access controls
[banexception](/3/modules/banexception)             | Provides channel mode +e, ban exceptions
[banredirect](/3/modules/banredirect)               | Allows an extended ban (+b) syntax redirecting banned users to another channel
[bcrypt](/3/modules/bcrypt)                         | Implements bcrypt hashing
[blockamsg](/3/modules/blockamsg)                   | Attempt to block /amsg or /ame, at least some of the irritating client scripts
[blockcaps](/3/modules/blockcaps)                   | Provides support to block all-CAPS channel messages and notices
[blockcolor](/3/modules/blockcolor)                 | Provides channel mode +c to block color
[botmode](/3/modules/botmode)                       | Provides user mode +B to mark the user as a bot
[callerid](/3/modules/callerid)                     | Implementation of callerid, provides user mode +g and the ACCEPT command
[cap](/3/modules/cap)                               | Provides support for CAP capability negotiation
[cban](/3/modules/cban)                             | Provides the CBAN command, like Q-lines, but for channels
[censor](/3/modules/censor)                         | Provides user and channel mode +G
[cgiirc](/3/modules/cgiirc)                         | Enables forwarding the real IP address of a user from a gateway to the IRC server
[chancreate](/3/modules/chancreate)                 | Provides snomasks 'j' and 'J', to which notices about newly created channels are sent
[chanfilter](/3/modules/chanfilter)                 | Provides channel-specific censor lists (like mode +G but varies from channel to channel)
[chanhistory](/3/modules/chanhistory)               | Provides channel mode +H, allows for the channel message history to be replayed on join
[chanlog](/3/modules/chanlog)                       | Logs snomask output to channel(s)
[channames](/3/modules/channames)                   | Implements config tags which allow changing characters allowed in channel names
[channelban](/3/modules/channelban)                 | Provides extban 'j', ban users that are present in another channel, and optionally on their status there
[check](/3/modules/check)                           | Provides the CHECK command to view user, channel, IP address or hostname information
[chghost](/3/modules/chghost)                       | Provides the CHGHOST command
[chgident](/3/modules/chgident)                     | Provides the CHGIDENT command
[chgname](/3/modules/chgname)                       | Provides the CHGNAME command
[classban](/3/modules/classban)                     | Provides extban 'n', connection class bans
[clearchan](/3/modules/clearchan)                   | Provides the CLEARCHAN command that allows opers to masskick, masskill or mass G/Z-line users on a channel
[cloaking](/3/modules/cloaking)                     | Provides masking of user hostnames
[clones](/3/modules/clones)                         | Provides the CLONES command to retrieve information on clones
[commonchans](/3/modules/commonchans)               | Provides user mode +c, requires users to share a common channel with you to private message you
[conn_join](/3/modules/conn_join)                   | Forces users to join the specified channel(s) on connect
[conn_umodes](/3/modules/conn_umodes)               | Sets (and unsets) modes on users when they connect
[conn_waitpong](/3/modules/conn_waitpong)           | Require pong prior to registration
[connectban](/3/modules/connectban)                 | Throttles the connections of IP ranges who try to connect flood
[connflood](/3/modules/connflood)                   | Connection throttle
[customprefix](/3/modules/customprefix)             | Provides custom prefix channel modes
[customtitle](/3/modules/customtitle)               | Provides the TITLE command, custom titles for users
[cycle](/3/modules/cycle)                           | Provides the CYCLE command, acts as a server-side HOP command to part and rejoin a channel
[dccallow](/3/modules/dccallow)                     | Provides the DCCALLOW command
[deaf](/3/modules/deaf)                             | Provides user modes +d and +D to block channel and user messages/notices
[delayjoin](/3/modules/delayjoin)                   | Provides channel mode +D, delay-join, users don't appear as joined to others until they speak
[delaymsg](/3/modules/delaymsg)                     | Provides channel mode +d &lt;int&gt;, to deny messages to a channel until &lt;int&gt; seconds have passed
[denychans](/3/modules/denychans)                   | Implements config tags which allow blocking of joins to channels
[disable](/3/modules/disable)                       | Provides support for disabling commands and modes
[dnsbl](/3/modules/dnsbl)                           | Provides handling of DNS blacklists
[exemptchanops](/3/modules/exemptchanops)           | Provides the ability to allow channel operators to be exempt from certain modes
[filter](/3/modules/filter)                         | Provides text (spam) filtering
[flashpolicyd](/3/modules/flashpolicyd)             | Flash Policy Daemon, allows Flash IRC clients to connect
[gecosban](/3/modules/gecosban)                     | Provides a way to ban users by their real name with the 'a' and 'r' extbans
[geoban](/3/modules/geoban)                         | Provides a way to ban users by country
[geoclass](/3/modules/geoclass)                     | Provides a way to assign users to connect classes by country
[globalload](/3/modules/globalload)                 | Allows global loading of a module
[globops](/3/modules/globops)                       | Provides the GLOBOPS command and snomask 'g'
[haproxy](/3/modules/haproxy)                       | Provides support for the HAProxy PROXY protocol
[helpop](/3/modules/helpop)                         | Provides the HELPOP command for useful information
[hidechans](/3/modules/hidechans)                   | Provides support for hiding channels with user mode +I
[hidelist](/3/modules/hidelist)                     | Provides support for hiding the list of listmodes
[hidemode](/3/modules/hidemode)                     | Provides support for hiding mode changes
[hideoper](/3/modules/hideoper)                     | Provides support for hiding oper status with user mode +H
[hostchange](/3/modules/hostchange)                 | Provides rule-based masking of user hostnames
[hostcycle](/3/modules/hostcycle)                   | Cycles users in all their channels when their host or ident changes
[httpd](/3/modules/httpd)                           | Provides HTTP serving facilities to modules
[httpd_acl](/3/modules/httpd_acl)                   | Provides access control lists (passwording of resources, IP restrictions, etc) to m_httpd dependent modules
[httpd_config](/3/modules/httpd_config)             | Allows for the server configuration to be viewed over HTTP via m_httpd
[httpd_stats](/3/modules/httpd_stats)               | Provides statistics over HTTP via m_httpd
[ident](/3/modules/ident)                           | Provides support for RFC1413 ident lookups
[inviteexception](/3/modules/inviteexception)       | Provides channel mode +I, invite exceptions
[ircv3](/3/modules/ircv3)                           | Provides support for extended-join, away-notify and account-notify CAP capabilities
[ircv3_accounttag](/3/modules/ircv3_accounttag)     | Provides the account-tag IRCv3 extension
[ircv3_batch](/3/modules/ircv3_batch)               | Provides the batch IRCv3 extension
[ircv3_capnotify](/3/modules/ircv3_capnotify)       | Provides the cap-notify IRCv3 extension
[ircv3_chghost](/3/modules/ircv3_chghost)           | Provides the chghost IRCv3 extension
[ircv3_ctctags](/3/modules/ircv3_ctctags)           | Provides the message-tags IRCv3 extension
[ircv3_echomessage](/3/modules/ircv3_echomessage)   | Provides the echo-message IRCv3 extension
[ircv3_invitenotify](/3/modules/ircv3_invitenotify) | Provides the invite-notify IRCv3 extension
[ircv3_msgid](/3/modules/ircv3_msgid)               | Provides the msgid IRCv3 tag
[ircv3_servertime](/3/modules/ircv3_servertime)     | Provides the server-time IRCv3 extension
[ircv3_sts](/3/modules/ircv3_sts)                   | Provides IRCv3 Strict Transport Security policy advertisement
[joinflood](/3/modules/joinflood)                   | Provides channel mode +j, join flood protection
[kicknorejoin](/3/modules/kicknorejoin)             | Provides channel mode +J, delays rejoins after kicks
[knock](/3/modules/knock)                           | Provides the KNOCK command and channel mode +K
[ldapauth](/3/modules/ldapauth)                     | Allow/deny connections based upon answers from an LDAP server
[ldapoper](/3/modules/ldapoper)                     | Adds the ability to authenticate opers via LDAP
[lockserv](/3/modules/lockserv)                     | Provides the LOCKSERV and UNLOCKSERV commands to lock the server and block all incoming connections until unlocked again
[maphide](/3/modules/maphide)                       | Replaces the output of the MAP and LINKS commands with an URL
[md5](/3/modules/md5)                               | Implements MD5 hashing
[messageflood](/3/modules/messageflood)             | Provides channel mode +f, message flood protection
[mlock](/3/modules/mlock)                           | Implements the ability to have server-side MLOCK enforcement
[modenotice](/3/modules/modenotice)                 | Provides the MODENOTICE command
[monitor](/3/modules/monitor)                       | Provides MONITOR support
[muteban](/3/modules/muteban)                       | Provides extban 'm', mute bans
[namedmodes](/3/modules/namedmodes)                 | Provides the ability to manipulate modes via long names
[namesx](/3/modules/namesx)                         | Provides the NAMESX (CAP multi-prefix) capability
[nationalchars](/3/modules/nationalchars)           | Provides an ability to have non-RFC1459 nicks & support for national CASEMAPPING
[nickflood](/3/modules/nickflood)                   | Provides channel mode +F, nick flood protection
[nicklock](/3/modules/nicklock)                     | Provides the NICKLOCK command, allows an oper to change a users nick and lock them to it until they quit
[noctcp](/3/modules/noctcp)                         | Provides user mode +T and channel mode +C to block CTCPs
[nokicks](/3/modules/nokicks)                       | Provides channel mode +Q to prevent kicks on the channel
[nonicks](/3/modules/nonicks)                       | Provides channel mode +N and extban 'N' which prevents nick changes on the channel
[nonotice](/3/modules/nonotice)                     | Provides channel mode +T to block notices to the channel
[nopartmsg](/3/modules/nopartmsg)                   | Provides extban 'p', part message bans
[ojoin](/3/modules/ojoin)                           | Provides the OJOIN command, allows an oper to join a channel and be immune to kicks
[operchans](/3/modules/operchans)                   | Provides support for oper-only channels via channel mode +O and extban 'O'
[operjoin](/3/modules/operjoin)                     | Forces opers to join the specified channel(s) on oper-up
[operlevels](/3/modules/operlevels)                 | Gives each oper type a 'level', cannot kill opers 'above' your level
[operlog](/3/modules/operlog)                       | Provides logging of all oper commands to the ircd log at the default loglevel
[opermodes](/3/modules/opermodes)                   | Sets (and unsets) modes on opers when they oper up
[opermotd](/3/modules/opermotd)                     | Shows a message to opers after oper-up and adds the OPERMOTD command
[operprefix](/3/modules/operprefix)                 | Gives opers channel mode +y which provides a staff prefix
[override](/3/modules/override)                     | Provides support for allowing opers to override certain things
[passforward](/3/modules/passforward)               | Sends server password to NickServ
[password_hash](/3/modules/password_hash)           | Provides the ability to hash passwords to other modules
[pbkdf2](/3/modules/pbkdf2)                         | Implements PBKDF2 hashing
[permchannels](/3/modules/permchannels)             | Provides channel mode +P to provide permanent channels
[randquote](/3/modules/randquote)                   | Provides random quotes on connect
[redirect](/3/modules/redirect)                     | Provides channel mode +L (limit redirection) and user mode +L (no forced redirection)
[regex_glob](/3/modules/regex_glob)                 | Regex provider module using plain wildcard matching
[remove](/3/modules/remove)                         | Provides the REMOVE command as an alternative to KICK, it makes users appear to have left the channel
[repeat](/3/modules/repeat)                         | Provides channel mode +E, blocking of similar messages
[restrictchans](/3/modules/restrictchans)           | Allows restricting who can create channels
[restrictmsg](/3/modules/restrictmsg)               | Forbids users from messaging each other, but users may still message opers and opers may message other opers
[rline](/3/modules/rline)                           | Provides support for banning users through regular expression patterns
[rmode](/3/modules/rmode)                           | Allows glob-based removal of list modes
[sajoin](/3/modules/sajoin)                         | Provides the SAJOIN command, allows opers to force-join users to channels
[sakick](/3/modules/sakick)                         | Provides the SAKICK command
[samode](/3/modules/samode)                         | Provides the SAMODE command, allows opers to change modes on channels and users
[sanick](/3/modules/sanick)                         | Provides the SANICK command, allows opers to change the nicknames of users
[sapart](/3/modules/sapart)                         | Provides the SAPART command, allows opers to force-part users from channels
[saquit](/3/modules/saquit)                         | Provides the SAQUIT command, allows opers to force-quit users
[sasl](/3/modules/sasl)                             | Provides support for IRC Authentication Layer (aka: SASL) via AUTHENTICATE
[satopic](/3/modules/satopic)                       | Provides the SATOPIC command
[securelist](/3/modules/securelist)                 | Disallows the LIST command for recently connected clients to hinder spam bots
[seenicks](/3/modules/seenicks)                     | Provides snomasks 'n' and 'N' to see local and remote nickchanges
[serverban](/3/modules/serverban)                   | Provides extban 's' to ban users connected to a specified server
[services_account](/3/modules/services_account)     | Provides support for ircu-style services accounts, including channel mode +R, etc
[servprotect](/3/modules/servprotect)               | Provides user mode +k to protect services from kicks, kills, and mode changes
[sethost](/3/modules/sethost)                       | Provides the SETHOST command
[setident](/3/modules/setident)                     | Provides the SETIDENT command
[setidle](/3/modules/setidle)                       | Provides the SETIDLE command, allows opers to set their idle time
[setname](/3/modules/setname)                       | Provides the SETNAME command
[sha1](/3/modules/sha1)                             | Implements SHA-1 hashing
[sha256](/3/modules/sha256)                         | Implements SHA-256 hashing
[showfile](/3/modules/showfile)                     | Provides support for showing text files to users
[showwhois](/3/modules/showwhois)                   | Provides user mode +W for opers to see when a user uses WHOIS on them
[shun](/3/modules/shun)                             | Provides the SHUN command, which stops a user from executing all except configured commands
[silence](/3/modules/silence)                       | Provides support for blocking users with the SILENCE command
[spanningtree](/3/modules/spanningtree)             | Allows servers to be linked
[sqlauth](/3/modules/sqlauth)                       | Allow/deny connections based upon an arbitrary SQL table
[sqloper](/3/modules/sqloper)                       | Allows storage of oper credentials in an SQL table
[sslinfo](/3/modules/sslinfo)                       | SSL Certificate Utilities
[sslmodes](/3/modules/sslmodes)                     | Provides user and channel mode +z to allow for SSL-only channels, queries and notices
[starttls](/3/modules/starttls)                     | Provides the STARTTLS command
[stripcolor](/3/modules/stripcolor)                 | Provides channel mode +S, strip ansi color
[svshold](/3/modules/svshold)                       | Implements SVSHOLD, like Q-lines, but can only be added/removed by Services
[swhois](/3/modules/swhois)                         | Provides the SWHOIS command which allows setting of arbitrary WHOIS lines
[timedbans](/3/modules/timedbans)                   | Provides the TBAN command, timed channel bans
[tline](/3/modules/tline)                           | Provides the TLINE command, used to test how many users a mask matches against
[topiclock](/3/modules/topiclock)                   | Implements server-side topic locks and the server-to-server command SVSTOPIC
[uhnames](/3/modules/uhnames)                       | Provides the UHNAMES (CAP userhost-in-names) capability
[uninvite](/3/modules/uninvite)                     | Provides the UNINVITE command which lets users un-invite other users from channels
[userip](/3/modules/userip)                         | Provides the USERIP command
[vhost](/3/modules/vhost)                           | Provides masking of user hostnames via the VHOST command
[watch](/3/modules/watch)                           | Provides WATCH support
[websocket](/3/modules/websocket)                   | Provides RFC 6455 WebSocket support
[xline_db](/3/modules/xline_db)                     | Provides the ability to store X-lines in a database file

### Extra Modules

These modules require third-party dependencies to be installed and have to be enabled at compile time. See the specific module page for details on how to enable these.

Name                                          | Description
--------------------------------------------- | -----------
[geo_maxmind](/3/modules/geo_maxmind)         | Provides Geolocation lookups using the libMaxMindDB library
[ldap](/3/modules/ldap)                       | Provides LDAP support
[mysql](/3/modules/mysql)                     | Provides MySQL support
[pgsql](/3/modules/pgsql)                     | PostgreSQL Service Provider module for all other m_sql\* modules
[regex_pcre](/3/modules/regex_pcre)           | Regex Provider Module for PCRE
[regex_posix](/3/modules/regex_posix)         | Regex Provider Module for POSIX Regular Expressions
[regex_re2](/3/modules/regex_re2)             | Regex Provider Module for RE2
[regex_stdlib](/3/modules/regex_stdlib)       | Regex Provider Module for std::regex
[regex_tre](/3/modules/regex_tre)             | Regex Provider Module for TRE Regular Expressions
[sqlite3](/3/modules/sqlite3)                 | Provides SQLite3 support
[ssl_gnutls](/3/modules/ssl_gnutls)           | Provides SSL support via GnuTLS
[ssl_mbedtls](/3/modules/ssl_mbedtls)         | Provides SSL support via mbedTLS (PolarSSL)
[ssl_openssl](/3/modules/ssl_openssl)         | Provides SSL support via OpenSSL
[sslrehashsignal](/3/modules/sslrehashsignal) | Reloads SSL credentials on SIGUSR1
