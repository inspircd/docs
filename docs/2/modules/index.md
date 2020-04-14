---
title: v2 Module List
---

{! 2/_support.md !}

## Module List

This is a complete list of all modules that ship with InspIRCd. If you have [installed from source](/2/installation/source) you can also install third-party modules which have been created by the InspIRCd community using the [Module Manager](/2/module-manager).

### Default Modules

These modules require no dependencies and will always be available.

Name                                            | Description
----------------------------------------------- | -----------
[abbreviation](/2/modules/abbreviation)         | Provides the ability to abbreviate commands a-la BBC BASIC keywords.
[alias](/2/modules/alias)                       | Provides aliases of commands.
[allowinvite](/2/modules/allowinvite)           | Provides support for channel mode +A, allowing /invite freely on a channel and extban A to deny specific users it.
[alltime](/2/modules/alltime)                   | Display timestamps from all servers connected to the network.
[auditorium](/2/modules/auditorium)             | Allows for auditorium channels (+u) where nobody can see others joining and parting or the nick list.
[autoop](/2/modules/autoop)                     | Provides support for the +w channel mode.
[banexception](/2/modules/banexception)         | Provides support for the +e channel mode.
[banredirect](/2/modules/banredirect)           | Allows an extended ban (+b) syntax redirecting banned users to another channel.
[blockamsg](/2/modules/blockamsg)               | Attempt to block /amsg, at least some of the irritating mIRC scripts.
[blockcaps](/2/modules/blockcaps)               | Provides support to block all-CAPS channel messages and notices.
[blockcolor](/2/modules/blockcolor)             | Provides channel mode +c to block color.
[botmode](/2/modules/botmode)                   | Provides user mode +B to mark the user as a bot.
[callerid](/2/modules/callerid)                 | Implementation of callerid, usermode +g, /accept.
[cap](/2/modules/cap)                           | Client CAP extension support.
[cban](/2/modules/cban)                         | Gives /cban, aka C:lines. Think Q:lines, for channels.
[censor](/2/modules/censor)                     | Provides user and channel +G mode.
[cgiirc](/2/modules/cgiirc)                     | Change user's hosts connecting from known CGI:IRC hosts.
[chancreate](/2/modules/chancreate)             | Provides snomasks 'j' and 'J', to which notices about newly created channels are sent.
[chanfilter](/2/modules/chanfilter)             | Provides channel-specific censor lists (like mode +G but varies from channel to channel).
[chanhistory](/2/modules/chanhistory)           | Provides channel history replayed on join.
[chanlog](/2/modules/chanlog)                   | Logs snomask output to channel(s).
[channames](/2/modules/channames)               | Implements config tags which allow changing characters allowed in channel names.
[channelban](/2/modules/channelban)             | Extban 'j' - channel status/join ban.
[chanprotect](/2/modules/chanprotect)           | Founder and Protect modes (+qa).
[check](/2/modules/check)                       | CHECK command, view user, channel, IP address or hostname information.
[chghost](/2/modules/chghost)                   | Provides support for the CHGHOST command.
[chgident](/2/modules/chgident)                 | Provides support for the CHGIDENT command.
[chgname](/2/modules/chgname)                   | Provides support for the CHGNAME command.
[cloaking](/2/modules/cloaking)                 | Provides masking of user hostnames.
[clones](/2/modules/clones)                     | Provides the /CLONES command to retrieve information on clones.
[close](/2/modules/close)                       | Provides /CLOSE functionality.
[commonchans](/2/modules/commonchans)           | Adds user mode +c, which if set, users must be on a common channel with you to private message you.
[conn_join](/2/modules/conn_join)               | Forces users to join the specified channel(s) on connect.
[conn_umodes](/2/modules/conn_umodes)           | Sets (and unsets) modes on users when they connect.
[conn_waitpong](/2/modules/conn_waitpong)       | Require pong prior to registration.
[connectban](/2/modules/connectban)             | Throttles the connections of IP ranges who try to connect flood.
[connflood](/2/modules/connflood)               | Connection throttle.
[customprefix](/2/modules/customprefix)         | Provides custom prefix channel modes.
[customtitle](/2/modules/customtitle)           | Custom Title for users.
[cycle](/2/modules/cycle)                       | Provides command CYCLE, acts as a server-side HOP command to part and rejoin a channel.
[dccallow](/2/modules/dccallow)                 | Provides support for the /DCCALLOW command.
[deaf](/2/modules/deaf)                         | Provides usermode +d to block channel messages and channel notices.
[delayjoin](/2/modules/delayjoin)               | Allows for delay-join channels (+D) where users don't appear to join until they speak.
[delaymsg](/2/modules/delaymsg)                 | Provides channelmode +d &lt;int&gt;, to deny messages to a channel until &lt;int&gt; seconds.
[denychans](/2/modules/denychans)               | Implements config tags which allow blocking of joins to channels.
[devoice](/2/modules/devoice)                   | Provides voiced users with the ability to devoice themselves.
[dnsbl](/2/modules/dnsbl)                       | Provides handling of DNS blacklists.
[exemptchanops](/2/modules/exemptchanops)       | Provides the ability to allow channel operators to be exempt from certain modes.
[filter](/2/modules/filter)                     | Text (spam) filtering.
[gecosban](/2/modules/gecosban)                 | Extban 'r' - realname (gecos) ban.
[globalload](/2/modules/globalload)             | Allows global loading of a module.
[globops](/2/modules/globops)                   | Provides support for GLOBOPS and snomask +g.
[halfop](/2/modules/halfop)                     | Channel half-operator mode provider.
[helpop](/2/modules/helpop)                     | Provides the /HELPOP command for useful information.
[hidechans](/2/modules/hidechans)               | Provides support for hiding channels with user mode +I.
[hideoper](/2/modules/hideoper)                 | Provides support for hiding oper status with user mode +H.
[hostchange](/2/modules/hostchange)             | Provides masking of user hostnames in a different way to m_cloaking.
[httpd](/2/modules/httpd)                       | Provides HTTP serving facilities to modules.
[httpd_acl](/2/modules/httpd_acl)               | Provides access control lists (passwording of resources, ip restrictions etc) to m_httpd.so dependent modules.
[httpd_config](/2/modules/httpd_config)         | Allows for the server configuration to be viewed over HTTP via m_httpd.so.
[httpd_stats](/2/modules/httpd_stats)           | Provides statistics over HTTP via m_httpd.so.
[ident](/2/modules/ident)                       | Provides support for RFC1413 ident lookups.
[inviteexception](/2/modules/inviteexception)   | Provides support for the +I channel mode.
[ircv3](/2/modules/ircv3)                       | Provides support for extended-join, away-notify and account-notify CAP capabilities.
[joinflood](/2/modules/joinflood)               | Provides channel mode +j (join flood protection).
[jumpserver](/2/modules/jumpserver)             | Provides support for the RPL_REDIR numeric and the /JUMPSERVER command.
[kicknorejoin](/2/modules/kicknorejoin)         | Channel mode to delay rejoin after kick.
[knock](/2/modules/knock)                       | Provides support for /KNOCK and channel mode +K.
[lockserv](/2/modules/lockserv)                 | Allows locking of the server to stop all incoming connections until unlocked again.
[maphide](/2/modules/maphide)                   | Hide /MAP and /LINKS in the same form as ircu.
[md5](/2/modules/md5)                           | Implements MD5 hashing.
[messageflood](/2/modules/messageflood)         | Provides channel mode +f (message flood protection).
[mlock](/2/modules/mlock)                       | Implements the ability to have server-side MLOCK enforcement.
[muteban](/2/modules/muteban)                   | Implements extban +b m: - mute bans.
[namedmodes](/2/modules/namedmodes)             | Provides the ability to manipulate modes via long names.
[namesx](/2/modules/namesx)                     | Provides the NAMESX (CAP multi-prefix) capability.
[nationalchars](/2/modules/nationalchars)       | Provides an ability to have non-RFC1459 nicks & support for national CASEMAPPING.
[nickflood](/2/modules/nickflood)               | Channel mode F - nick flood protection.
[nicklock](/2/modules/nicklock)                 | Provides the NICKLOCK command, allows an oper to change a users nick and lock them to it until they quit.
[noctcp](/2/modules/noctcp)                     | Provides channel mode +C to block CTCPs.
[nokicks](/2/modules/nokicks)                   | Provides channel mode +Q to prevent kicks on the channel.
[nonicks](/2/modules/nonicks)                   | Provides support for channel mode +N & extban +b N: which prevents nick changes on channel.
[nonotice](/2/modules/nonotice)                 | Provides channel mode +T to block notices to the channel.
[nopartmsg](/2/modules/nopartmsg)               | Implements extban +b p: - part message bans.
[ojoin](/2/modules/ojoin)                       | Network Business Join.
[operchans](/2/modules/operchans)               | Provides support for oper-only chans via the +O channel mode and 'O' extban.
[operjoin](/2/modules/operjoin)                 | Forces opers to join the specified channel(s) on oper-up.
[operlevels](/2/modules/operlevels)             | Gives each oper type a 'level', cannot kill opers 'above' your level.
[operlog](/2/modules/operlog)                   | A module which logs all oper commands to the ircd log at default loglevel.
[opermodes](/2/modules/opermodes)               | Sets (and unsets) modes on opers when they oper up.
[opermotd](/2/modules/opermotd)                 | Shows a message to opers after oper-up, adds /opermotd.
[operprefix](/2/modules/operprefix)             | Gives opers cmode +y which provides a staff prefix.
[override](/2/modules/override)                 | Provides support for allowing opers to override certain things.
[passforward](/2/modules/passforward)           | Sends server password to NickServ.
[password_hash](/2/modules/password_hash)       | Allows for hashed oper passwords.
[permchannels](/2/modules/permchannels)         | Provides support for channel mode +P to provide permanent channels.
[randquote](/2/modules/randquote)               | Provides random quotes on connect.
[redirect](/2/modules/redirect)                 | Provides channel mode +L (limit redirection) and user mode +L (no forced redirection).
[regex_glob](/2/modules/regex_glob)             | Regex module using plain wildcard matching.
[regonlycreate](/2/modules/regonlycreate)       | Prevents users whose nicks are not registered from creating new channels.
[remove](/2/modules/remove)                     | Provides a /remove command, this is mostly an alternative to /kick, except makes users appear to have parted the channel.
[restrictchans](/2/modules/restrictchans)       | Only opers may create new channels if this module is loaded.
[restrictmsg](/2/modules/restrictmsg)           | Forbids users from messaging each other. Users may still message opers and opers may message other opers.
[ripemd160](/2/modules/ripemd160)               | Provides RIPEMD-160 hashing.
[rline](/2/modules/rline)                       | RLINE: Regexp user banning.
[sajoin](/2/modules/sajoin)                     | Provides command SAJOIN to allow opers to force-join users to channels.
[sakick](/2/modules/sakick)                     | Provides a SAKICK command.
[samode](/2/modules/samode)                     | Provides command SAMODE to allow opers to change modes on channels and users.
[sanick](/2/modules/sanick)                     | Provides support for SANICK command.
[sapart](/2/modules/sapart)                     | Provides command SAPART to force-part users from a channel.
[saquit](/2/modules/saquit)                     | Provides support for an SAQUIT command, exits user with a reason.
[sasl](/2/modules/sasl)                         | Provides support for IRC Authentication Layer (aka: SASL) via AUTHENTICATE.
[satopic](/2/modules/satopic)                   | Provides a SATOPIC command.
[securelist](/2/modules/securelist)             | Disallows /LIST for recently connected clients to hinder spam bots.
[seenicks](/2/modules/seenicks)                 | Provides support for seeing local and remote nickchanges via snomasks.
[serverban](/2/modules/serverban)               | Extban 's' - server ban.
[services_account](/2/modules/services_account) | Provides support for ircu-style services accounts, including chmode +R, etc.
[servprotect](/2/modules/servprotect)           | Provides user mode +k to protect services from kicks, kills, and channel prefix mode changes.
[sethost](/2/modules/sethost)                   | Provides support for the SETHOST command.
[setident](/2/modules/setident)                 | Provides support for the SETIDENT command.
[setidle](/2/modules/setidle)                   | Allows opers to set their idle time.
[setname](/2/modules/setname)                   | Provides support for the SETNAME command.
[sha256](/2/modules/sha256)                     | Implements SHA-256 hashing.
[showwhois](/2/modules/showwhois)               | Allows opers to set +W to see when a user uses WHOIS on them.
[shun](/2/modules/shun)                         | Provides the /SHUN command, which stops a user from executing all except configured commands.
[silence](/2/modules/silence)                   | Provides support for the /SILENCE command.
[spanningtree](/2/modules/spanningtree)         | Allows servers to be linked.
[sqlauth](/2/modules/sqlauth)                   | Allow/Deny connections based upon an arbitrary SQL table.
[sqloper](/2/modules/sqloper)                   | Allows storage of oper credentials in an SQL table.
[sslinfo](/2/modules/sslinfo)                   | Provides user TLS (SSL) information and certificate utilities.
[sslmodes](/2/modules/sslmodes)                 | Provides channel mode +z to allow for Secure/SSL only channels.
[stripcolor](/2/modules/stripcolor)             | Provides channel +S mode (strip ansi color).
[svshold](/2/modules/svshold)                   | Implements SVSHOLD. Like Q:Lines, but can only be added/removed by Services.
[swhois](/2/modules/swhois)                     | Provides the SWHOIS command which allows setting of arbitrary WHOIS lines.
[testnet](/2/modules/testnet)                   | Provides a module for testing the server while linked in a network.
[timedbans](/2/modules/timedbans)               | Adds timed bans.
[tline](/2/modules/tline)                       | Provides /tline command used to test who a mask matches.
[topiclock](/2/modules/topiclock)               | Implements server-side topic locks and the server-to-server command SVSTOPIC.
[uhnames](/2/modules/uhnames)                   | Provides the UHNAMES facility.
[uninvite](/2/modules/uninvite)                 | Provides the UNINVITE command which lets users un-invite other users from channels.
[userip](/2/modules/userip)                     | Provides support for USERIP command.
[vhost](/2/modules/vhost)                       | Provides masking of user hostnames via traditional /VHOST command.
[watch](/2/modules/watch)                       | Provides support for the /WATCH command.
[xline_db](/2/modules/xline_db)                 | Keeps a dynamic log of all X-lines created, and stores them in a separate conf file (xline.db).

### Extra Modules

These modules require third-party dependencies to be installed and have to be enabled at compile time. See the specific module page for details on how to enable these.

Name                                    | Description
--------------------------------------- | -----------
[geoip](/2/modules/geoip)               | Provides a way to assign users to connect classes by country using GeoIP lookup.
[ldapauth](/2/modules/ldapauth)         | Allow/Deny connections based upon answer from LDAP server.
[ldapoper](/2/modules/ldapoper)         | Adds the ability to authenticate opers via LDAP.
[mysql](/2/modules/mysql)               | MySQL support.
[pgsql](/2/modules/pgsql)               | PostgreSQL Service Provider module for all other m_sql* modules, uses v2 of the SQL API.
[regex_pcre](/2/modules/regex_pcre)     | Regex Provider Module for PCRE.
[regex_posix](/2/modules/regex_posix)   | Regex Provider Module for POSIX Regular Expressions.
[regex_stdlib](/2/modules/regex_stdlib) | Regex Provider Module for std::regex.
[regex_tre](/2/modules/regex_tre)       | Regex Provider Module for TRE Regular Expressions.
[sqlite3](/2/modules/sqlite3)           | sqlite3 provider.
[ssl_gnutls](/2/modules/ssl_gnutls)     | Provides TLS (SSL) support for clients.
[ssl_openssl](/2/modules/ssl_openssl)   | Provides TLS (SSL) support for clients.
