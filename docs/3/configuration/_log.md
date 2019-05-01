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

Value                | Description
-------------------- | -----------
BANCACHE             | Messages relating to the X-line result cache.
CHANNELS             | Messages relating to channels.
COMMAND              | Messages relating to command execution.
CONFIG               | Messages relating to the configuration.
CONNECTCLASS         | Messages relating to connect classes.
CULLLIST             | Messages relating to object cull lists.
MODULE               | Messages relating to modules.
SOCKET               | Messages relating to network sockets.
STARTUP              | Messages relating to the startup process.
USERINPUT            | Messages relating to user input.
USEROUTPUT           | Messages relating to user output.
USERS                | Messages relating to users.
WHOWAS               | Messages relating to the `/WHOWAS` command.
core_channel         | Messages relating to channels.
core_dns             | Messages relating to DNS lookups.
core_hostname_lookup | Messages relating to user hostname lookups.
core_oper            | Messages relating to server operators.
core_reloadmodule    | Messages relating to the RELOADMODULE command.
core_whowas          | Messages relating to the WHOWAS command.
m_callerid           | Messages relating to [the callerid module](/3/modules/callerid).
m_cap                | Messages relating to [the cap module](/3/modules/cap).
m_cgiirc             | Messages relating to [the cgiirc module](/3/modules/cgiirc).
m_chanlog            | Messages relating to [the chanlog module](/3/modules/chanlog).
m_connectban         | Messages relating to [the connectban module](/3/modules/connectban).
m_customprefix       | Messages relating to [the customprefix module](/3/modules/customprefix).
m_disable            | Messages relating to [the disable module](/3/modules/disable).
m_dnsbl              | Messages relating to [the dnsbl module](/3/modules/dnsbl).
m_filter             | Messages relating to [the filter module](/3/modules/filter).
m_geo_maxmind        | Messages relating to [the geo_maxmind module](/3/modules/geo_maxmind).
m_hidemode           | Messages relating to [the hidemode module](/3/modules/hidemode).
m_httpd_acl          | Messages relating to [the httpd_acl module](/3/modules/httpd_acl).
m_httpd_config       | Messages relating to [the httpd_config module](/3/modules/httpd_config).
m_httpd_stats        | Messages relating to [the httpd_stats module](/3/modules/httpd_stats).
m_ident              | Messages relating to [the ident module](/3/modules/ident).
m_ircv3_sts          | Messages relating to [the ircv3_sts module](/3/modules/ircv3_sts).
m_ldapauth           | Messages relating to [the ldapauth module](/3/modules/ldapauth).
m_mysql              | Messages relating to [the mysql module](/3/modules/mysql).
m_nationalchars      | Messages relating to [the nationalchars module](/3/modules/nationalchars).
m_operlog            | Messages relating to [the operlog module](/3/modules/operlog).
m_password_hash      | Messages relating to [the password_hash module](/3/modules/password_hash).
m_permchannels       | Messages relating to [the permchannels module](/3/modules/permchannels).
m_pgsql              | Messages relating to [the pgsql module](/3/modules/pgsql).
m_regex_pcre         | Messages relating to [the regex_pcre module](/3/modules/regex_pcre).
m_sasl               | Messages relating to [the sasl module](/3/modules/sasl).
m_showfile           | Messages relating to [the showfile module](/3/modules/showfile).
m_spanningtree       | Messages relating to [the spanningtree module](/3/modules/spanningtree).
m_sqlite3            | Messages relating to [the sqlite3 module](/3/modules/sqlite3).
m_sqloper            | Messages relating to [the sqloper module](/3/modules/sqloper).
m_ssl_gnutls         | Messages relating to [the ssl_gnutls module](/3/modules/ssl_gnutls).
m_ssl_mbedtls        | Messages relating to [the ssl_mbedtls module](/3/modules/ssl_mbedtls).
m_ssl_openssl        | Messages relating to [the ssl_openssl module](/3/modules/ssl_openssl).
m_sslinfo            | Messages relating to [the sslinfo module](/3/modules/sslinfo).
m_sslrehashsignal    | Messages relating to [the sslrehashsignal module](/3/modules/sslrehashsignal).
m_topiclock          | Messages relating to [the topiclock module](/3/modules/topiclock).
m_xline_db           | Messages relating to [the xline_db module](/3/modules/xline_db).

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
