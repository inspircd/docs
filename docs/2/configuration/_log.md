<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

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
