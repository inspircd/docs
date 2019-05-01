---
disable_toc: true
title: Commands
---

## InspIRCd Commands

This page only lists core commands. For details on the commands of a specific module please refer to [the appropriate page for that module](/2/modules).

### `/ADMIN [<server>]`

Retrieves the contact details for the administrator of the specified server.

If `<server>` is not specified then it defaults to the local server.

#### Example Usage

Retrieves the contact details for the local server administrator:

```plaintext
/ADMIN
```

Retrieves the contact details for the server administrator of irc.example.com:

```plaintext
/ADMIN irc.example.com
```

### `/AWAY [<message>]`

If `<message>` is specified marks yourself as being away with the specified message.

Otherwise, marks yourself as being no longer away.

#### Example Usage

Marks yourself away with the message "Washing my hair":

```plaintext
/AWAY :Washing my hair
```

Marks yourself as no longer being away:

```plaintext
/AWAY
```

### `/CLEARCACHE`

Clears the internal DNS cache for the local server.

### `/COMMANDS`

Lists all commands that exist on the server.

### `/DIE <password>`

Shuts down the server using the password specified in the server configuration.

#### Example Usage

Shuts down the server using the password "hunter2":

```plaintext
/DIE hunter2
```

### `/ELINE <ident@host> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then exempts an ident@host mask from being affected by other (G, K, Z, etc) X-lines. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the E-line will be permanent.

Otherwise, if just `<ident@host>` is specified, removes an exemption on an ident@host mask.

#### Example Usage

E-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/ELINE sadie@example.com 1d :Testing
```

E-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/ELINE sadie@example.com 86400 :Testing
```

Removes an E-line on sadie@example.com:

```plaintext
/ELINE sadie@example.com
```

### `/GLINE <ident@host> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then bans an ident@host mask from connecting to the network. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the G-line will be permanent.

Otherwise, if just `<ident@host>` is specified, removes a G-line on an ident@host mask.

#### Example Usage

G-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/GLINE sadie@example.com 1d :Testing
```

G-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/GLINE sadie@example.com 86400 :Testing
```

Removes an G-line on sadie@example.com:

```plaintext
/GLINE sadie@example.com
```

### `/INFO`

Retrieves information on the developers and supporters who made the creation and continued development of this IRC server possible.

### `/INVITE [[<nick> <channel>] <duration>]`

If no parameters are specified then lists the invites which you have been sent that haven't been acted on yet.

If `<nick>` and `<channel>` are specified then sends an invite to `<nick>` inviting them to join `<channel>`. If `<duration>` is specified then the invite will expire after the specified duration passes. This duration can be given as a number of seconds or as a duration in the format 1y2w3d4h5m6s.

#### Example Usage

Lists all pending invites that you have been sent:

```plaintext
/INVITE
```

Invites Sadie to #example:

```plaintext
/INVITE Sadie #example
```

Invites Sadie to #example with a five minute invite expiry:

```plaintext
/INVITE Sadie #example 5m
```

Invites Sadie to #example with a five minute invite expiry:

```plaintext
/INVITE Sadie #example 300
```

### `/ISON <nick> [<nick>]+`

Determines whether the specified nicknames are currently connected to the server.

#### Example Usage

Checks whether Adam, Attila, and Sadie are currently connected to the server:

```plaintext
/ISON Adam Attila Sadie
```

### `/JOIN <channel>[,<channel>]+ [<key>][,[<key>]+]`

Joins one or more channels using the specified channel keys if required.

#### Example Usage

Joins #channel:

```plaintext
/JOIN #channel
```

Joins #channel with the key hunter2:

```plaintext
/JOIN #channel hunter2
```

Joins #channel-one with no key and #channel-two with the key hunter2:

```plaintext
/JOIN #channel-one,#channel-two ,hunter2
```

### `/KICK <channel> <nick>[,<nick>]+ [<reason>]`

Kicks one or more users from the specified channel. You must at least a channel half-operator (or channel operator if that channel mode is not enabled) and must be an equal or higher rank to the user you are kicking.

#### Example Usage

Kicks Soni from #channel with no reason:

```plaintext
/KICK #channel Soni
```

Kicks Soni from #channel:

```plaintext
/KICK #channel Soni :Disruptive behaviour is not allowed
```

Kicks opal and Soni from #channel:

```plaintext
/KICK #channel opal,Soni :Disruptive behaviour is not allowed
```

### `/KILL <nick> <reason>`

Forcibly disconnects the specified user from the server.

#### Example Usage

```plaintext
/KILL opal :Disruptive behaviour is not allowed
```

### `/KLINE <ident@host> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then bans an ident@host mask from connecting to the local server. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the K-line will be permanent.

Otherwise, if just `<ident@host>` is specified, removes a K-line on an ident@host mask.

#### Example Usage

K-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/KLINE sadie@example.com 1d :Testing
```

K-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/KLINE sadie@example.com 86400 :Testing
```

Removes an K-line on sadie@example.com:

```plaintext
/KLINE sadie@example.com
```

### `/LIST [(>|<)<count>|<pattern>]`

Lists all channels visibile to the requesting user.

If `(>|<)<count>` is specified then only shows channels which contain more or less users than `<count>`.

If `<pattern>` is specified then only shows channels with a name or a topic matching `<pattern>`.

### `/LOADMODULE <module>`

Loads the specified module on the local server.

#### Example Usage

Loads the botmode module:

```plaintext
/LOADMODULE m_botmode.so
```

### `/LUSERS`

Shows information about the current and total number of servers, server operators, and users.

### `/MODE <target> <modes> [<parameters>]+`

Changes the modes which are set on a target.

For a list of modes see [the modes page](/2/modes).

#### Example Usage

Sets:

1. Channel mode `n` (noextmsg).
2. Channel parameter-set mode `k` (key) with the value "s3cr3t".
3. Channel parameter mode `l` (limit) with the value "100".
4. Channel prefix mode `o` (op) with the user "Sadie".

```plaintext
/MODE #channel +nklo s3cr3t 100 Sadie
```

Unsets:

1. Channel mode `n` (noextmsg).
2. Channel parameter-set mode `k` (key) with the value "s3cr3t".
3. Channel parameter mode `l` (limit).
4. Channel prefix mode `o` (op) with the user "Sadie".

```plaintext
/MODE #channel -nklo s3cr3t Sadie
```

Sets:

1. User mode `w` (wallops).
2. User parameter mode `s` (snomask) with the value "*".

```plaintext
/MODE Sadie +ws *
```

Unsets:

1. User mode `w` (wallops).
2. User parameter mode `s` (snomask).

```plaintext
/MODE Sadie -ws
```

### `/MODENOTICE <modes> <message>`

Sends a message to all users with the specified user modes set.

#### Example Usage

Sends a message to every user with user mode `i` (invisible) set:

```plaintext
/MODENOTICE i :Hello invisible people!
```

### `/MODULES`

Lists all modules which are loaded on the server.

### `/MOTD [<server>]`

If `<server>` is specified then views the message of the day for the specified server.

Otherwise, views the message of the day for the local server.

#### Example Usage

Retrieves the MOTD for the local server:

```plaintext
/MOTD
```

Retrieves the MOTD for irc2.example.com:

```plaintext
/MOTD irc2.example.com
```

### `/NAMES [<channel>[,<channel>]+]`

Retrieves a list of users who are in the specified channels.

#### Example Usage

Retrieves the users on channels #one and #two:

```plaintext
/NAMES #one,#two
```

### `/NICK <nick>`

Changes your nickname to `<nick>`.

You may also change your nick to your UUID by specifying a nickname of "0".

#### Example Usage

Changes your nick to Sadie:

```plaintext
/NICK Sadie
```

Changes your nick to your UUID:

```plaintext
/NICK 0
```

### `/NOTICE <target> <message>`

Sends a notice to the target specified in `<target>`. This target can be a channel, a user, or a server mask (requires the users/mass-message server operator privilege).

#### Example Usage

Sends a notice to #channel saying "Hello!":

```plaintext
/NOTICE #channel :Hello!
```

Sends a notice to Sadie saying "Hello!":

```plaintext
/NOTICE Sadie :Hello!
```

Sends a notice to all users on servers matching the glob pattern `*.example.com` saying "Hello!":

```plaintext
/NOTICE $*.example.com :Hello!
```

### `/OPER <name> <password>`

Logs into a server operator account with the specified name and password. 

#### Example Usage

Logs into the server operator account "AzureDiamond" with the password "hunter2":

```plaintext
/OPER AzureDiamond hunter2
```

### `/PART <channel> [<reason>]`

Leaves the specified channel. If `<message>` is specified then it will be used as the message shown when parting.

#### Example Usage

Leaves \#channel with no reason:

```plaintext
/PART #channel
```

Leaves \#channel with the reason "Going to bed":

```plaintext
/PART #channel :Going to bed
```

### `/PASS <password>`

Specifies the password used to connect to the server.

#### Example Usage

Specifies "hunter2" as the server password.

```plaintext
/PASS hunter2
```

### `/PING <server1> [<server2>]`

Pings `<server2>` from `<server1>`.

If `<server2>` is not specified it defaults to the local server.

#### Example Usage

Pings irc.eu.example com from the local server:

```plaintext
/PING irc.eu.example.com
```

Pings irc.eu.example com from irc.us.example.com:

```plaintext
/PING irc.eu.example.com irc.us.example.com
```

### `/PONG <text>`

Responds to a ping to let the server know you are still connected.

#### Example Usage

Replies to a ping from irc.example.com:

```plaintext
/PONG :irc.example.com
```

### `/PRIVMSG <target>[,<target>] <message>`

Sends a message to the target specified in `<target>`. This target can be a channel, a user, or a server mask (requires the users/mass-message server operator privilege).

#### Example Usage

Sends a message to #channel saying "Hello!":

```plaintext
/PRIVMSG #channel :Hello!
```

Sends a message to Sadie saying "Hello!":

```plaintext
/PRIVMSG Sadie :Hello!
```

Sends a message to all users on servers matching the glob pattern `*.example.com` saying "Hello!":

```plaintext
/PRIVMSG $*.example.com :Hello!
```

### `/QLINE <nick> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then prevents a nickname from being used. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the Q-line will be permanent.

Otherwise, if just `<nick>` is specified, removes an Q-line on a nickname.

#### Example Usage

Q-lines Adam for one day with the reason "Testing":

```plaintext
/QLINE Adam 1d :Testing
```

Q-lines Sadie for one day with the reason "Testing":

```plaintext
/QLINE Sadie 86400 :Testing
```

Removes an Q-line on Adam:

```plaintext
/QLINE Adam
```

### `/QUIT [<message>]`

Disconnects from the server. If `<message>` is specified then it will be used as the message shown when quitting. Otherwise, "Client exited" will be used.

#### Example Usage

Quits with "Client exited" as the quit message:

```plaintext
/QUIT
```

Quits with "Time for bed" as the reason:

```plaintext
/QUIT :Time for bed
```

### `/REHASH <server>|-<type>`

Reloads the server configuration.

If `<server>` is specified then the specified server's configuration is reloaded instead of the local server.

If `<type>` is specified then then a specific module is rehashed instead of the full configuration.

#### Example Usage

Reloads the local server configuration:

```plaintext
/REHASH
```

Reloads the server configuration for remote.example.com:

```plaintext
/REHASH remote.example.com
```

Reloads the SSL certificates:

```plaintext
/REHASH -ssl
```

### `/RELOADMODULE <module>`

Reloads the specified module.

#### Example Usage

Reloads the alias module:

```plaintext
/RELOADMODULE m_alias.so
```

### `/RESTART <password>`

Restarts the local server using the password specified in the server configuration.

#### Example Usage

Restarts the server using the password "hunter2":

```plaintext
/RESTART hunter2
```

### `/RULES <server>`

If `<server>` is specified then views the rules for the specified server.

Otherwise, views the rules for the local server.

#### Example Usage

Retrieves the rules for the local server:

```plaintext
/RULES
```

Retrieves the rules for irc2.example.com:

```plaintext
/RULES irc2.example.com
```

### `/STATS <character> [<server>]`

Views the specified server statistics.

If `<server>` is specified then views the server statistics for the specified server.

Otherwise, views the server statistics for the local server.

#### Example Usage

Views `p` (ports) statistics for the local server:

```plaintext
/STATS p
````

Views `p` (ports) statistics for the remote server irc.eu.example.com:

```plaintext
/STATS p irc.eu.example.com
```

### `/TIME [<server>]`

Retrieves the current time on the specified server.

If `<server>` is specified then views the time on the specified server.

Otherwise, views the on the local server.

#### Example Usage

Views the time on the local server:

```plaintext
/TIME
```

Views the time on remote server irc.eu.example.com:

```plaintext
/STATS p irc.eu.example.com
```

### `/TOPIC <channel> [<newtopic>]`

If `<newtopic>` is specified then changes the topic for `<channel>` to the specified value.

Otherwise, retrieves the topic for the specified channel.

#### Example Usage

Changes the topic for #trains to "choo choo"

```plaintext
/TOPIC #trains :choo choo
```

Retrieves the topic for #trains:

```plaintext
/TOPIC #trains
```

### `/UNLOADMODULE <module>`

Unload the specified module on the local server.

#### Example Usage

Unloads the botmode module:

```plaintext
/UNLOADMODULE m_botmode.so
```

### `/USER <username> <unused> <unused> <realname>`

Specifies the username (ident) and real name (gecos) when connecting to the server.

#### Example Usage

Specifies the username (ident) "jsmith" and the real name "John Smith <jsmith@example.com>":

```plaintext
/USER jsmith * * :John Smith <jsmith@example.com>
```

### `/USERHOST <nick> [<nick>]`

Retrieves the hostname of the specified users.

#### Example Usage

Retrieves the hostname of Adam:

```plaintext
/USERHOST Adam
```

Retrieves the hostname of Adam and Sadie:

```plaintext
/USERHOST Adam
```

### `/VERSION [<server>]`

If `<server>` is specified then retrieves the version of the specified server.

Otherwise, retrieves the version of the local server.

#### Example Usage

Retrieves the version of the local server:

```plaintext
/VERSION
```

Retrieves the version of the remote server irc.eu.example.com:

```plaintext
/VERSION irc.eu.example.com
```

### `/WALLOPS <message>`

Sends a message to all users with the `w` (wallops) user mode enabled:

#### Example Usage

Sends "Rebooting for updates at 20:00 UTC" to all users with the `w` (wallops) user mode enabled.

```plaintext
/WALLOPS :Rebooting for updates at 20:00 UTC
```

### `/WHO <server>|<nick>|<channel>|<host>|<pattern>|<realname>|0 [afhilMmoprt]`

Looks up information about users who match the specified condition. One or more of the following flags may be used.

Character | Description
--------- | -----------
a         | Show users who have an away message matching `<pattern>`.
f         | Only show users on remote (far) servers.
h         | Show real hostnames rather than display hostnames (server operators only).
i         | Show users who have an ident (username) matching `<pattern>`.
l         | Only show users on the local server.
M         | Show users who have metadata attached to them with a key name matching `<pattern>` (server operators only).
m         | Show users who have the modes listed in `<pattern>`. The pattern should be in the same format as a mode change e.g. +ow-i (server operators only).
o         | Only show server operators.
p         | Show users who are connected to a port in the `<pattern>` range (server operators only).
r         | Show users who have a real name matching `<pattern>`.
t         | Show users who have connected in the last `<pattern>` seconds.

#### Example Usage

Retrieve all users who have an away message matching `*brb`:

```plaintext
/WHO *brb* a
```

View all server operators on irc.eu.example.com:

```plaintext
/WHO irc.eu.example.com o
```

### `/WHOIS <nick1>[,<nick1>]  <nick2>[,<nick2>]`

Looks up information about users who are currently connected with the specified nicks:

If the `<nick2>` parameter is specified for a user then remotes information will be fetched about the user if they are not on the local server.

#### Example Usage

Looks up locally available information about the user who is using the nick Adam:

```plaintext
/WHOIS Adam
```

Looks up remotely available information about the user who is using the nick Adam:

```plaintext
/WHOIS Adam Adam
```

Looks up locally available information about users who are using the nicks Adam and Sadie:

```plaintext
/WHOWAS Adam,Sadie
```

Looks up remotely available information about users who are using the nicks Adam and Sadie:

```plaintext
/WHOWAS Adam,Sadie Adam,Sadie
```

### `/WHOWAS <nick>[,<nick>]`

Looks up information about users who were previously connected with the specified nicks.

#### Example Usage

Looks up information about the user who previously used the nick Adam:

```plaintext
/WHOWAS Adam
```

Looks up information about users who previously used the nicks Adam and Sadie:

```plaintext
/WHOWAS Adam,Sadie
```

### `/ZLINE <ipaddr> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then bans an IP address or CIDR range from connecting to the network. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the Z-line will be permanent.

Otherwise, if just `<ipaddr>` is specified, removes a Z-line on an IP address.

#### Example Usage

Z-lines 192.0.2.1 for one day with the reason "Testing":

```plaintext
/ZLINE 192.0.2.0 1d :Testing
```

Z-lines 192.0.2.0/24 for one day with the reason "Testing":

```plaintext
/ZLINE 192.0.2.0/24 86400 :Testing
```

Removes an Z-line on 192.0.2.1:

```plaintext
/ZLINE 192.0.2.1
```
