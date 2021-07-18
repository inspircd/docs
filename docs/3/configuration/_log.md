<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<log>`

The `<log>` tag defines a location to log to. This tag can be defined as many times as required.

Name   | Type   | Default Value | Description
------ | ------ | ------------- | -----------
method | Text   | *None*        | The method to use for storing logs.
type   | Text   | *None*        | **Required!** A space-delimited token list of types of message to log.
level  | Text   | default       | The level of messages to log.
target | Text   | *None*        | The location to write the log to.
flush  | Number | 20            | After how many lines to flush the log to disk.

The method field should be set to one of the following values:

Value | Description
----- | -----------
file  | The specified log types should be written to a file.

The type field should be set to one or more of the following values:

Value                | Logging Levels Used         | Description
-------------------- | --------------------------- | -----------
BANCACHE             | debug                       | Messages relating to the X-line result cache.
CHANNELS             | debug                       | Messages relating to channels.
COMMAND              | default                     | Messages relating to command execution.
CONFIG               | default<br>debug            | Messages relating to the configuration.
CONNECTCLASS         | default<br>debug            | Messages relating to connect classes.
CULLLIST             | debug                       | Messages relating to object cull lists.
HEADER               | sparse                      | Messages relating to starting logging.
MODE                 | debug                       | Messages relating to modes.
MODULE               | default<br>debug            | Messages relating to modules.
SERIALIZE            | debug                       | Messages relating to object serialisation.
SERVICE              | debug                       | Messages relating to service registration.
SOCKET               | default<br>debug            | Messages relating to network sockets.
STARTUP              | default                     | Messages relating to the startup process.
USERINPUT            | rawio                       | Messages relating to user input.
USEROUTPUT           | rawio                       | Messages relating to user output.
USERS                | default<br>debug            | Messages relating to users.
core_channel         | debug                       | Messages relating to channels.
core_dns             | sparse<br>default<br>debug  | Messages relating to DNS lookups.
core_hostname_lookup | debug                       | Messages relating to user hostname lookups.
core_oper            | sparse<br>default           | Messages relating to server operators.
core_reloadmodule    | debug                       | Messages relating to the RELOADMODULE command.
core_whowas          | default                     | Messages relating to the WHOWAS command.
m_callerid           | default                     | Messages relating to [the callerid module](/3/modules/callerid).
m_cap                | debug                       | Messages relating to [the cap module](/3/modules/cap).
m_cgiirc             | default<br>debug            | Messages relating to [the cgiirc module](/3/modules/cgiirc).
m_chanlog            | default                     | Messages relating to [the chanlog module](/3/modules/chanlog).
m_cloaking           | default                     | Messages relating to [the cloaking module](/3/modules/cloaking).
m_codepage           | debug                       | Messages relating to [the codepage module](/3/modules/codepage).
m_connectban         | debug                       | Messages relating to [the connectban module](/3/modules/connectban).
m_customprefix       | debug                       | Messages relating to [the customprefix module](/3/modules/customprefix).
m_customtitle        | default                     | Messages relating to [the customtitle module](/3/modules/customtitle).
m_dccallow           | debug                       | Messages relating to [the dccallow module](/3/modules/dccallow).
m_disable            | default<br>debug            | Messages relating to [the disable module](/3/modules/disable).
m_dnsbl              | debug                       | Messages relating to [the dnsbl module](/3/modules/dnsbl).
m_filter             | default<br>debug            | Messages relating to [the filter module](/3/modules/filter).
m_geo_maxmind        | debug                       | Messages relating to [the geo_maxmind module](/3/modules/geo_maxmind).
m_hidemode           | debug                       | Messages relating to [the hidemode module](/3/modules/hidemode).
m_httpd              | debug                       | Messages relating to [the httpd module](/3/modules/httpd).
m_httpd_acl          | debug                       | Messages relating to [the httpd_acl module](/3/modules/httpd_acl).
m_httpd_config       | debug                       | Messages relating to [the httpd_config module](/3/modules/httpd_config).
m_httpd_stats        | debug                       | Messages relating to [the httpd_stats module](/3/modules/httpd_stats).
m_ident              | debug                       | Messages relating to [the ident module](/3/modules/ident).
m_ircv3_sts          | debug                       | Messages relating to [the ircv3_sts module](/3/modules/ircv3_sts).
m_ldapauth           | debug                       | Messages relating to [the ldapauth module](/3/modules/ldapauth).
m_mysql              | default<br>debug            | Messages relating to [the mysql module](/3/modules/mysql).
m_nationalchars      | default                     | Messages relating to [the nationalchars module](/3/modules/nationalchars).
m_operlog            | default                     | Messages relating to [the operlog module](/3/modules/operlog).
m_password_hash      | default                     | Messages relating to [the password_hash module](/3/modules/password_hash).
m_permchannels       | default<br>debug            | Messages relating to [the permchannels module](/3/modules/permchannels).
m_pgsql              | default<br>debug            | Messages relating to [the pgsql module](/3/modules/pgsql).
m_regex_pcre         | debug                       | Messages relating to [the regex_pcre module](/3/modules/regex_pcre).
m_sasl               | default<br>verbose<br>debug | Messages relating to [the sasl module](/3/modules/sasl).
m_showfile           | default                     | Messages relating to [the showfile module](/3/modules/showfile).
m_silence            | debug                       | Messages relating to [the silence module](/3/modules/silence).
m_spanningtree       | default<br>debug<br>rawio   | Messages relating to [the spanningtree module](/3/modules/spanningtree).
m_sqlite3            | default<br>debug            | Messages relating to [the sqlite3 module](/3/modules/sqlite3).
m_sqloper            | sparse<br>default           | Messages relating to [the sqloper module](/3/modules/sqloper).
m_ssl_gnutls         | default<br>debug            | Messages relating to [the ssl_gnutls module](/3/modules/ssl_gnutls).
m_ssl_mbedtls        | default<br>debug            | Messages relating to [the ssl_mbedtls module](/3/modules/ssl_mbedtls).
m_ssl_openssl        | default<br>debug            | Messages relating to [the ssl_openssl module](/3/modules/ssl_openssl).
m_sslinfo            | debug                       | Messages relating to [the sslinfo module](/3/modules/sslinfo).
m_sslrehashsignal    | default                     | Messages relating to [the sslrehashsignal module](/3/modules/sslrehashsignal).
m_topiclock          | default                     | Messages relating to [the topiclock module](/3/modules/topiclock).
m_vhost              | default                     | Messages relating to [the vhost module](/3/modules/vhost).
m_xline_db           | debug                       | Messages relating to [the xline_db module](/3/modules/xline_db).

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
     target="ircd.log"
     flush="20">
```
