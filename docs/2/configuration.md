---
disable_toc: true
title: Configuration
---

## InspIRCd Configuration

This page only lists core configuration. For details on the configuration of a specific module please refer to [the appropriate page for that module](/2/modules).

### `<admin>`

The `<admin>` tag defines contact details for the server administrator. This tag can only be defined once.

Name  | Type | Default Value    | Description
----- | ---- | ---------------- | -----------
name  | Text | *None*           | If defined then the real name of the server operator.
nick  | Text | admin            | The nickname of the server operator.
email | Text | null@example.com | The email address of the server operator.

#### Example Usage

```xml
<admin name="John Doe"
       nick="JDoe123"
       email="jdoe123@example.com">
```

### `<banlist>`

The `<banlist>` tag defines the number of bans which can be created in a channel. This tag can be defined as many times as required.

Name  | Type   | Default Value | Description
----- | ------ | ------------- | -----------
chan  | Text   | *None*        | **Required!** A glob pattern for channels that this limit applies to.
limit | Number | *None*        | **Required!** The number of bans which can be created in these channels.

#### Example Usage

```xml
<banlist chan="#largechan"
         limit="500">

<banlist chan="*"
         limit="100">
```

### `<bind>`

The `<bind>` tag defines an endpoint to listen for connections on. This tag can only be defined once.

Name    | Type   | Default Value | Description
------- | ------ | ------------- | -----------
address | Text   | *None*        | If defined then the IP address to bind to instead of listening on all available interfaces.
port    | Number | *None*        | **Required!** The TCP port to listen for connections on.
type    | Text   | clients       | The type of connection to be allowed on this endpoint.

The type field should be set to one of the following values:

Value   | Module                                  | Description
------- | --------------------------------------- | -----------
clients | *None*                                  | Listens for IRC client connections.
httpd   | [httpd](/2/modules/httpd)               | Listens for HTTP connnections.
servers | [spanningtree](/2/modules/spanningtree) | Listens for IRC server connections.

#### Example Usage

Listens for IRC client connections on 192.0.2.1:6667:

```xml
<bind address="192.0.2.1"
      port="6667"
      type="clients">
```

Listens for IRC server connections on *:6667:

```xml
<bind port="6667"
      type="clients">
```

### `<channels>`

The `<channels>` tag defines the maximum number of channels that a user can be in. This tag can only be defined once.

Name  | Type   | Default Value | Description
----- | ------ | ------------- | -----------
opers | Number | 60            | The maximum number of channels that a server operator can join.
users | Number | 20            | The maximum number of channels that a normal user can join.

#### Example Usage

```xml
<channels opers="60"
          users="20">
```

### `<cidr>`

The `<cidr>` tag defines the number of bits of an IP address that should be looked at when locating clones. This tag can only be defined once.

Name      | Type   | Default Value | Description
--------- | ------ | ------------- | -----------
ipv4clone | Number | 32            | The number of bits (0-32) of an IPv4 address that should be looked at when locating clones.
ipv6clone | Number | 128           | The number of bits (0-128) of an IPv6 address that should be looked at when locating clones.

#### Example Usage

```xml
<cidr ipv4clone="32"
      ipv6clone="128">
```

### `<class>`

The `<class>` tag defines a set of server operator privileges. This tag can be defined as many times as required.

Name      | Type | Default Value | Description
--------- | ---- | ------------- | -----------
name      | Text | *None*        | A name that uniquely identifies this server operator class.
commands  | Text | *None*        | A space-delimited list of server operator-only commands that server operators with this class can execute.
privs     | Text | *None*        | A space-delimited list of server operator privileges that server operators with this class has.
chanmodes | Text | *None*        | The server operator-only channel modes that server operators with this class can change.
usermodes | Text | *None*        | The server operator-only user modes that server operators with this class can change.

#### Example Usage

```
<class name="OperChat"
       commands="WALLOPS GLOBOPS"
       privs="users/mass-message"
       chanmodes="*"
       usermodes="*">
```

### `<connect>`

The `<connect>` tag defines a class that users can be filtered into when they connect to the server. This tag can be defined as many times as required.

Name        | Type    | Default Value           | Description
----------- | ------- | ----------------------- | -----------
name        | Text    | *None*                  | If defined then the name of this connect class.
allow       | Text    | *None*                  | A glob pattern or CIDR range for an IP address which is allowed to connect to the server. If this is defined then `deny` (below) MUST NOT be defined.
deny        | Text    | *None*                  | A glob pattern or CIDR range for an IP address which is banned from connecting to the server. If this is defined then `allow` (below) MUST NOT be defined.
commandrate | Number  | *None*                  | The number of millicommands per second that a user can execute.
fakelag     | Boolean | Yes                     | Whether users should have their input/output delayed when they reach a soft limit rather than being killed.
globalmax   | Number  | *None*                  | The maximum number of users who can exist on the entire network from the range specified in the allow field.
hardsendq   | Number  | 1048576                 | The maximum amount of data allowed in a user's send queue before it is killed.
limit       | Number  | *None*                  | The maximum number of users who can be in this connect class.
localmax    | Number  | *None*                  | The maximum number of users who can exist on the local server from the range specified in the allow field.
maxchans    | Number  | *None*                  | If defined then the maximum number of channels that a user in this class can be in.
maxconnwarn | Boolean | No                      | Whether to send a server notice when a connect class limit is reached.
parent      | Text    | *None*                  | If defined then the name of the class to inherit most *core* settings from.
password    | Text    | *None*                  | *Not inherited from the parent block!*  The password that the user must send to be put into this connect class.
pingfreq    | Number  | 120                     | The number of seconds this client can be idle for before sending it a `PING` message.
port        | Number  | *None*                  | *Not inherited from the parent block!* The port on which a client must be connecting to be put into this connect class.
reason      | Number  | Unauthorised connection | *Not inherited from the parent block!* If `<connect:deny>` is set then the reason to give when disconnecting a user.
recvq       | Number  | 4096                    | The maximum amount of data allowed in a user's receive queue before it is killed.
registered  | Boolean | *None*                  | *Not inherited from the parent block!* If defined then whether this connect class matches a user in registration or a client that has completed registration.
softsendq   | Number  | 4096                    | The maximum number of bytes of data that can be in a user's send queue before the server stops processing their input to allow the send queue to drain.
threshold   | Number  | 10                      | The maximum amount of penalty that a user can have before being fakelagged or killed if fakelag is turned off.
timeout     | Number  | 90                      | The number of seconds after which an unregistered user is timed out.

#### Example Usage

Denies connections to clients connecting from 3ffe::0/32:

```xml
<connect name="6bone"
         deny="3ffe::0/32"
         reason="The 6bone address space is deprecated">
```

Defines a general connect class and then a SSL-only connect class that inherits from it:

```xml
<connect name="Secure"
         parent="Main"
         port="6697">

<connect name="Main"
         allow="*"
         commandrate="1000"
         fakelag="on"
         globalmax="3"
         hardsendq="1M"
         limit="5000"
         localmax="3"
         maxchans="30"
         maxconnwarn="no"
         pingfreq="120"
         recvq="8K"
         softsendq="8192"
         threshold="10"
         timeout="10">
```

### `<disabled>`

The `<disabled>` tag defines commands and modes which normal users can not change. This tag can only be defined once.

Name            | Type    | Default Value | Description
--------------- | ------- | ------------- | -----------
fakenonexistant | Boolean | No            | Whether to pretend that a disabled command/mode does not exist.
commands        | Text    | *None*        | A space-delimited list of commands to disable.
chanmodes       | Text    | *None*        | A list of channel modes to disable.
usermodes       | Text    | *None*        | A list of user modes to disable.

#### Example Usage

```xml
<disabled fakenonexistant="no"
          commands="MODE TOPIC"
          chanmodes="kp"
          usermodes="iw">
```

### `<dns>`

The `<dns>` tag defines the DNS server to use when looking up hostnames. This tag can only be defined once.

Name    | Type   | Default Value | Description
------- | ------ | ------------- | -----------
server  | Text   | *None*        | If defined then the DNS server to look up hostnames with.
timeout | Number | 5             | The number of seconds before timing out DNS lookups.

#### Example Usage

```xml
<dns server="8.8.8.8"
     timeout="5">
```

### `<insane>`

The `<insane>` tag defines limits to protect against overly wide X-lines being created. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
hostmasks | Boolean | No            | Whether to apply the limit to E-lines, G-lines, and K-lines.
ipmasks   | Boolean | No            | Whether to apply the limit to Z-lines.
nickmasks | Boolean | No            | Whether to apply the limit to Q-lines.
trigger   | Decimal | 95.5          | The percentage of connected users who must match the X-line for it to be rejected as overly wide.

#### Example Usage

```xml
<insane hostmasks="yes"
        ipmasks="yes"
        nickmasks="yes"
        trigger="95.5">
```

### `<limits>`

The `<limits>` tag defines the maximum length of user-configurable fields. This tag can only be defined once.

Name     | Type   | Default Value | Description
-------- | ------ | ------------- | -----------
maxaway  | Number | 200           | The maximum length of an away message.
maxchan  | Number | 64            | The maximum length of a channel name.
maxgecos | Number | 128           | The maximum length of a real name (gecos).
maxident | Number | 11            | The maximum length of a username (ident).
maxkick  | Number | 255           | The maximum length of a kick message.
maxmodes | Number | 20            | The maximum number of non-flag modes that can be changed in a single `MODE` message.
maxnick  | Number | 32            | The maximum length of a nickname.
maxquit  | Number | 255           | The maximum length of a quit message.
maxtopic | Number | 307           | The maximum length of a channel topic.

#### Example Usage

```xml
<limits maxaway="200"
        maxchan="64"
        maxgecos="128"
        maxident="11"
        maxkick="255"
        maxmodes="20"
        maxnick="32"
        maxquit="255"
        maxtopic="307"
```

### `<log>`

The `<log>` tag defines a location to log to. This tag can be defined as many times as required.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
method | Text | file          | The method to use for storing logs.
type   | Text | *None*        | **Required!** A space-delimited token list of types of message to log.
level  | Text | default       | The level of messages to log.
target | Text | *None*        | The location to write the log to.

The method field should be set to one of the following values:

Value | Description
----- | -----------
file  | The specified log types should be written to a file.

The type field should be set to one or more of the following values:

Value            | Description
---------------- | -----------
BANCACHE         | Messages relating to the X-line result cache.
CHANNELS         | Messages relating to channels.
COMMAND          | Messages relating to command execution.
CONFIG           | Messages relating to the configuration.
CONNECTCLASS     | Messages relating to connect classes.
CULLLIST         | Messages relating to object cull lists.
FILTER           | Messages relating to [the filter module](/2/modules/filter).
INVITATION       | Messages relating to channel invites.
INVITEBASE       | Messages relating to channel invites.
KILL             | Messages relating to users being killed by server operators.
map              | Messages relating to the `/MAP` command.
MODE             | Messages relating to channel and user modes.
MODULE           | Messages relating to modules.
OPER             | Messages relating to server operators.
REGEX            | Messages relating to [the regex_pcre module](/2/modules/regex_pcre).
remoterehash     | Messages relating to the server being rehashed remotely.
RESOLVER         | Messages relating to DNS lookups.
SETGROUPS        | Messages relating to the `<security:runasgroup>` option.
SETGUID          | Messages relating to the `<security:runasuser>` option.
snomask          | Messages relating to server notices.
SOCKET           | Messages relating to network sockets.
STARTUP          | Messages relating to the startup process.
USERINPUT        | Messages relating to user input.
USEROUTPUT       | Messages relating to user output.
USERS            | Messages relating to users.
WHOWAS           | Messages relating to the `/WHOWAS` command.
m_banredirect.so | Messages relating to [the banredirect module](/2/modules/banredirect).
m_callerid       | Messages relating to [the callerid module](/2/modules/callerid).
m_chanlog        | Messages relating to [the chanlog module](/2/modules/chanlog).
m_connectban     | Messages relating to [the connectban module](/2/modules/connectban).
m_dnsbl          | Messages relating to [the dnsbl module](/2/modules/dnsbl).
m_filter         | Messages relating to [the filter module](/2/modules/filter).
m_httpd          | Messages relating to [the httpd module](/2/modules/httpd)
m_httpd_acl      | Messages relating to [the httpd_acl module](/2/modules/httpd_acl).
m_http_stats     | Messages relating to [the httpd_stats module](/2/modules/httpd_stats).
m_ident          | Messages relating to [the ident module](/2/modules/ident).
m_ldapauth       | Messages relating to [the ldapauth module](/2/modules/ldapauth).
m_nationalchars  | Messages relating to [the nationalchars module](/2/modules/nationalchars).
m_operlog        | Messages relating to [the operlog module](/2/modules/operlog).
m_permchannels   | Messages relating to [the permchannels module](/2/modules/permchannels).
m_pgsql          | Messages relating to [the pgsql module](/2/modules/pgsql).
m_redirect       | Messages relating to [the redirect module](/2/modules/redirect).
m_ripemd160      | Messages relating to [the ripemd160 module](/2/modules/ripemd160).
m_ripemd160.so   | Messages relating to [the ripemd160 module](/2/modules/ripemd160).
m_sasl           | Messages relating to [the sasl module](/2/modules/sasl).
m_spanningtree   | Messages relating to [the spanningtree module](/2/modules/spanningtree).
m_sqlite3        | Messages relating to [the sqlite3 module](/2/modules/sqlite3).
m_sqloper        | Messages relating to [the sqloper module](/2/modules/sqloper).
m_ssl_gnutls     | Messages relating to [the ssl_gnutls module](/2/modules/ssl_gnutls).
m_ssl_openssl    | Messages relating to [the ssl_openssl module](/2/modules/ssl_openssl).
m_topiclock      | Messages relating to [the topiclock module](/2/modules/topiclock).
m_xline_db       | Messages relating to [the xline_db module](/2/modules/xline_db).

The level field should be set to one of the following values:

Value   | Description
------- | -----------
rawio   | Logs raw I/O traffic.
debug   | Logs debug information.
verbose | Logs verbose information.
default | Logs general information.
sparse  | Log errors and other infrequent information.
none    | Logs nothing.

#### Example Usage

```xml
<log method="file"
     type="* -USERINPUT -USEROUTPUT"
     level="default"
     target="logs/ircd.log">
```

### `<module>`

The `<module>` tag defines a module to load. This tag can be defined as many times as required.

Name | Type | Default Value | Description
---- | ---- | ------------- | -----------
name | Text | *None*        | **Required!** The filename of a module to load.

#### Example Usage

```xml
<module name="m_ssl_gnutls.so">
```

### `<oper>`

The `<oper>` tag defines a server operator account. This tag can be defined as many times as required.

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
class    | Text | *None*        | If defined then a connect class to assign users who log into this server operator account to.
hash     | Text | *None*        | If defined then the hash algorithm that the password field is hashed with.
host     | Text | *None*        | **Required!** A space-delimited list of glob patterns for the username@hostname mask that users must be connecting from to log into this server operator account.
name     | Text | *None*        | **Required!** The username for this server operator account.
password | Text | *None*        | **Required!** The password for this server operator account.
type     | Text | *None*        | **Required!** The type of server operator this account is.
vhost    | Text | *None*        | If defined then a virtual hostname to set on users who log into this server operator account.

{! 2/modules/_hash_table.md !}

#### Example Usage

```xml
<oper name="Sadie"
      password="7H8Tqm+i$jaG48RHAcoLXSB3Guzaf1bQehaNRNbblMoNrHPdguvU"
      hash="hmac-sha256"
      class="ServerOperators"
      host="*@bnc.example.com"
      type="NetAdmin"
      vhost="staff.example.net">
```

### `<options>`

The `<options>` tag defines general configuration options. This tag can only be defined once.

Name               | Type    | Default Value  | Description
------------------ | ------- | -------------- | -----------
cyclehosts         | Boolean | No             | Whether to fake a connect and reconnect for users whose hostnames have changed to allow clients to update their hostname cache.
cyclehostsfromuser | Boolean | No             | Whether to send modes from the user rather than the server when sending a fake rejoin.
defaultbind        | Text    | auto           | The IP version to bind using if an IP address is not specified.
defaultmodes       | Text    | nt             | The default modes to apply to newly created channels.
exemptchanops      | Text    | *None*         | The privileges to exempt ranked channel users from. See the notes for [the exemptchanops module](/2/modules/exemptchanops) for more information.
fixedpart          | Text    | *None*         | If defined then a static value to replace users' part messages with.
fixedquit          | Text    | *None*         | If defined then a static value to replace users' quit messages with.
hostintopic        | Boolean | No             | Whether to show the full user mask of a topic setter rather than just their nickname.
invitebypassmodes  | Boolean | Yes            | Whether being invited to a channel allows the invitee to bypass channel modes which would otherwise prevent them from joining.
ircumsgprefix      | Boolean | No             | *Deprecated!* Whether to prefix `PRIVMSG` and `NOTICE`  messages with the status character when sending a status message.
moronbanner        | Text    | You're banned! | The message to send to users who have been banned from the server.
nosnoticestack     | Boolean | No             | Whether to stop identical server notices from being stacked with "last message repeated X times".
prefixpart         | Text    | *None*         | If defined then the value to prefix users' part messages with.
prefixquit         | Text    | *None*         | If defined then the value to prefix users' quit messages with.
suffixpart         | Text    | *None*         | If defined then the value to suffix users' part messages with.
suffixquit         | Text    | *None*         | If defined then the value to suffix users' quit messages with.
syntaxhints        | Boolean | No             | Whether to send syntax hints to users who send commands with not enough parameters.
welcomenotice      | Boolean | Yes            | *Deprecated!* Whether to send a welcome message to users on connect.

The defaultbind field should be set to one of the following values:

Value | Description
----- | -----------
auto  | Bind to :: if IPv6 support is available. Otherwise, bind to 0.0.0.0.
ipv4  | Bind to 0.0.0.0 by default.
ipv6  | Bind to :: by default.

#### Example Usage

```xml
<options cyclehosts="yes"
         cyclehostsfromuser="no"
         defaultbind="auto"
         defaultmodes="nst"
         exemptchanops=""
         fixedpart=""
         fixedquit=""
         hostintopic="yes"
         invitebypassmodes="yes"
         ircumsgprefix="no"
         moronbanner="You're banned. Email abuse@example.com to appeal this decision."
         nosnoticestack="no"
         prefixpart="&quot;"
         prefixquit="Quit: "
         suffixpart="&quot;"
         suffixquit=""
         syntaxhints="yes"
         welcomenotice="no">
```

### `<path>`

The `<path>` tag defines the location of the modules directory. This tag can only be defined once.

Name      | Type | Default Value | Description
--------- | ---- | ------------- | -----------
moduledir | Text | modules       | The location of the modules directory.

#### Example Usage

```xml
<path moduledir="modules">
```

### `<performance>`

The `<performance>` tag defines configuration options relating to server performance. This tag can only be defined once.

Name           | Type    | Default Value  | Description
-------------- | ------- | -------------- | -----------
limitsomaxconn | Boolean | Yes            | Whether to limit to the somaxconn field to the compile-time `SOMAXCONN` constant.
netbuffersize  | Number  | 10240          | The size of the buffer used to receive data from users.
nouserdns      | Boolean | No             | Whether DNS lookups should be performed to resolve the hostnames of connecting users.
softlimit      | Number  | *Varies*       | The maximum number of connections to allow to the IRC server.
somaxconn      | Number  | *Varies*       | The maximum number of connections that may be waiting in the connection accept queue.

#### Example Usage

```xml
<performance limitsomaxconn="yes"
             netbuffersize="10240"
             nouserdns="no"
             softlimit="15000"
             somaxconn="128">
```

### `<pid>`

The `<pid>` tag defines the location of the pidfile. This tag can only be defined once.

Name | Type | Default Value     | Description
---- | ---- | ----------------- | -----------
file | Text | data/inspircd.pid | The location of the pidfile.

#### Example Usage

```xml
<pid file="data/inspircd.pid">
```

### `<power>`

The `<power>` tag defines the passwords for the `/DIE` and `/RESTART` commands. This tag can only be defined once.

Name        | Type | Default Value | Description
----------- | ---- | ------------- | -----------
hash        | Text | *None*        | If defined then the hash algorithm that the password fields are hashed with. 
diepass     | Text | *None*        | The password for the `/DIE` command. 
restartpass | Text | *None*        | The password for the `/RESTART` command. 

{! 2/modules/_hash_table.md !}

#### Example Usage

```xml
<power hash="hmac-sha256"
       diepass="dsPt0O0a$hzRT2ODLGgQnyaugt74ACaP4YN1BBtff/rU94ZJi29U"
       restartpass="hpMUFNl5$YVcwiAWphiqm1zgzzz8j+lBi7bOtSDNVhdpBmflL5VQ">
```

### `<security>`

The `<security>` tag defines configuration options relating to server security. This tag can only be defined once.

Name                | Type     | Default Value | Description
------------------- | -------- | ------------- | -----------
announceinvites     | Text     | none          | Whether to send an announcement when a user is invited to a channel.
customversion       | Text     | Network IRCd  | A custom string to show in the `/VERSION` output.
genericoper         | Boolean  | No            | Whether to show "is an IRC operator" in `/WHOIS` instead of the server operator's type.
hidebans            | Boolean  | No            | Whether to only show X-line messages to server operators.
hidekills           | Text     | *None*        | If defined then the text to show in a kill message instead of the name of the server operator who caused the kill.
hidemodes           | Text     | *None*        | The list modes to hide from users without channel privileges.
hidesplits          | Boolean  | No            | Whether to hide server names in netsplit quits from non-server operators.
hideulinekills      | Boolean  | No            | Whether to hide server notices about kills by users on ulined servers.
hidewhois           | Text     | *None*        | If defined then the text to show in place of a server name in `/WHOIS` output.
maxtargets          | Number   | 20            | The maximum number of targets a user may specify in a command.
operspywhois        | Text     | no            | Whether to show private/secret channels to operators with the users/auspex privilege.
restrictbannedusers | Boolean  | Yes           | Whether to restrict the behaviour of users who are banned in a channel.
runasgroup          | Text     | *None*        | If defined then the group to switch to after starting up (requires starting as root).
runasuser           | Text     | *None*        | If defined then the user to switch to after starting up (requires starting as root).
userstats           | Text     | *None*        | The `/STATS` characters that a non-server operator can view.

The announceinvites field should be set to one of the following values:

Value   | Description
------- | -----------
none    | Don't send any invite announcements.
ops     | Send invite announcements to channel operators and higher ranked users.
dynamic | Send invites to channel half-operators (if available) and higher ranked users.
all     | Send invites to all channel members.

The operspywhois field should be set to one of the following values:

Value    | Description
-------- | -----------
no       | Don't show private/secret channels to operators with the users/auspex privilege.
yes      | Show private/secret channels to operators with the users/auspex privilege.
splitmsg | Show private/secret channels to operators with the users/auspex privilege in a separate message with an explanation.

#### Example Usage

```xml
<security announceinvites="dynamic"
          customversion=""
          genericoper="no"
          hidebans="yes"
          hidekills=""
          hidemodes="be"
          hidesplits="no"
          hideulinekills="yes"
          hidewhois=""
          maxtargets="20"
          operspywhois="yes"
          restrictbannedusers="yes"
          runasgroup=""
          runasuser=""
          userstats="Pu">
```

### `<server>`

The `<server>` tag defines settings about the local server. This tag can only be defined once.

Name        | Type | Default Value | Description
----------- | ---- | ------------- | -----------
name        | Text | *None*        | **Required!** The hostname of the local server.
description | Text | Configure Me  | A description of the local server.
network     | Text | Network       | The name of the IRC network the local server is attached to.
id          | Text | *None*        | If defined then a unique server identifier in the format [0-9][0-9A-Z][0-9A-Z].

#### Example Usage

```xml
<server name="irc.eu.example.com"
        description="ExampleNet's European server"
        network="ExampleNet"
        id="34C">
```

### `<type>`

The `<type>` tag defines a type of server operator. This tag can be defined as many times as required.

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
class    | Text | *None*        | If defined then a connect class to assign users who log into this server operator account to.
classes  | Text | *None*        | If defined then a space-delimited list of `<class>` tags to inherit privileges from.
name     | Text | *None*        | **Required!** The name for this server operator account.
vhost    | Text | *None*        | If defined then a virtual hostname to set on users who log into this server operator account.

#### Example Usage

```xml
<type name="NetAdmin"
      class="ServerOperators"
      classes="BanControl HostCloak OperChat SACommands ServerLink Shutdown"
      vhost="staff.example.net">
```

### `<whowas>`

The `<whowas>` tag defines the configuration of the `/WHOWAS` database. This tag can only be defined once.

Name      | Type     | Default Value | Description
--------- | -------- | ------------- | -----------
groupsize | Number   | 0             | The maximum number of `/WHOWAS` entries for a nickname.
maxgroups | Number   | 0             | The maximum number of `/WHOWAS` nickname groups.
maxkeep   | Duration | 1h            | The period of time to keep `/WHOWAS` records for.

#### Example Usage

```xml
<whowas groupsize="10"
        maxgroups="100000"
        maxkeep="3d">
```
