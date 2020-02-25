---
title: v3 Breaking Changes
---

## Breaking changes since InspIRCd 2

NOTE: This document only lists breaking changes between InspIRCd 2 and InspIRCd 3. There are many backwards compatible changes that have been made which are not listed in this document.

## Changes

- The ldapauth module no longer needs to be enabled at build time but now depends on the new ldap module which does need to be enabled at build time.

- The ldapoper module no longer needs to be enabled at build time but now depends on the new ldap module which does need to be enabled at build time.

- The gnutls module no longer automatically generates DH parameters at runtime. Generally all you will need to do in order to upgrade is to regenerate your self-signed certificates with `inspircd-genssl` or run `certtool --generate-dh-params --sec-param normal --outfile dhparams.pem`.

- The default for `<config:format>` has changed from `compat` to `xml`. If you have not set this value then you will need to set it to `compat` or switch all C-style `\` escapes to XML-style `&entity;` escapes.

- The `channels/ignore-noctcp` oper privilege is now required in order to send a CTCP to a +C channel.

- The `channels/restricted-create` oper privilege is now required in order to create channels if the restrictchans module is loaded.

- The `users/ignore-commonchans` oper privilege is now required in order to send a message to a +c user without sharing common channels.

- The `users/ignore-noctcp` oper privilege is now required in order to send a CTCP to a +T user.

- The `users/ignore-privdeaf` oper privilege is now required in order to message users with +D set.

- The `users/samode-usermodes` oper privilege is now required in order to change the user modes of other users with `/SAMODE`.

- The `users/sajoin-others` oper privilege is now required in order to `/SAJOIN` users other than themselves.

- `<cloak:key>` must now be at least 30 characters long. If your cloaking key is shorter than this you should define a stronger one in your `<cloak>` tag. You can define a second `<cloak>` tag with your old key to be used as a backup to avoid breaking any existing bans.

- `<disabled>` has been moved from the core to the new disable module. All you will need to do in order to upgrade is to load this module. The oper privileges `servers/use-disabled-commands` and `servers/use-disabled-modes` are now required in order for opers to bypass the disable module settings.

- `<gnutls:cafile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<gnutls:certfile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<gnutls:crlfile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<gnutls:keyfile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<include:file>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<log:target>` is now relative to the log directory. Generally all you will need to do in order to upgrade is remove `logs/` from the path.

- `<openssl:cafile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<openssl:certfile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<openssl:crlfile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<openssl:dhfile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<openssl:keyfile>` is now relative to the config directory. Generally all you will need to do in order to upgrade is remove `conf/` from the path.

- `<options:defaultmodes>` must now include any default prefix modes. To keep v2 behaviour add "o" to the default modes.

- `<permchanneldb:filename>` is now relative to the config directory. Generally all you will need to do in order to upgrade is move `permchannels.conf` to `conf/` and remove `data/` from the path.

- `<sasl:target>` is now required. The module cannot be loaded unless a target is supplied.

- `<type:name>` can now contain spaces. Any underscores in the type name will no longer be replaced with spaces. To keep v2 behaviour replace any underscores with spaces.

- `<xlinedb:filename>` is now relative to the data directory. Generally all you will need to do in order to upgrade is remove `data/` from the path.

## Moves

- The `/MODENOTICE` command has been moved to the new modenotice module. See the documentation in modules.conf.example for more details.

- The close module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_close` to install it.

- The geoip module has been replaced with the geo_maxmind and geoclass modules. In order to upgrade load these modules and replace comma-delimited `<connect:geoip>` entries with space-delimited `<connect:country>` entries.

- The jumpserver module has been moved to inspircd-contrib. In order to upgrade either remove this module from your configuration or run `./modulemanager install m_jumpserver` to install it.

- Server configuration for the ldapauth module has been moved to `<database>`. See the documentation in modules.conf.example for more details.

- Server configuration for the ldapoper module has been moved to `<database>`. See the documentation in modules.conf.example for more details.

- `<banlist>` has been moved to `<maxlist>` and now applies to all mode types unless a mode constraint is added.

- `<performance:nouserdns>` has been moved to `<connect:resolvehostnames>`.

- The `aliases` directory which previously contained services aliases has been renamed to `services` and now also contains services pseudoclient nickname reservations and filter exemptions. Generally all you will need to do to upgrade is to amend any `<include>` tags to point to the new directory.

- The `helpop-full.conf.example` config file has been merged with `helpop.conf.example`. Generally all you will need to do to upgrade is to amend any `<include>` tags to point to the new file.

- DNSBL-related server notices have been moved to the 'd' (dnsbl) snomask character.  You will need to update any oper blocks.

- Filter-related server notices have been moved to the 'f' (filter) snomask character.  You will need to update any oper blocks.

## Removals

- The `/RANDQUOTE` command has been removed with no replacement.

- The `/RULES` command has been removed. If you wish to keep this command then you should load the new showfile module. See the documentation in modules.conf.example for more details.

- The chanprotect module has been removed. If you wish to keep this behaviour then you should load the customprefix module and uncomment the "founder" and "admin" prefixes. See the documentation in modules.conf.example for more details.

- The devoice module has been removed. If you wish to keep this behaviour then you should load the customprefix module and specify `<customprefix name="voice" change="yes" depriv="yes">` to allow users to devoice themselves.

- The halfop module has been removed. If you wish to keep this behaviour then you should load the customprefix module and uncomment the "halfop" prefix. See the documentation in modules.conf.example for more details.

- The regonlycreate module has been removed. If you wish to keep this behaviour then you should load the restrictchans module and enable the `<restrictchans:allowregistered>` setting.

- The ripemd160 module has been removed. If you wish to keep this behaviour then you should install and load the hash_gnutls module from inspircd-contrib.

- The testnet module has been removed with no replacement.

- The `compat-host` and `compat-ip` options for `<cloak:mode>` have been removed. You should switch to either `full` or `half` instead. See the documentation in modules.conf.example for more details.

- The `identfirst`, `pass`, and `passfirst` options for `<cgihost:type>` has been removed. You should switch to either `ident` or `webirc`instead. See the documentation in modules.conf.example for more details.

- The `suffix` mode of `<hostchange:action>` has been removed. If you wish to keep this behaviour you should change it to `set` and specify the `value` parameter.

- The 'd' (debug) snomask character has been removed and the things using it have been moved to 'a' (announcements) and 'x' (xline) respectively. You will need to update any oper blocks.

- `<banlist>` has been removed. If you wish to keep this behaviour you should rename it to `<maxlist mode="ban">`.

- `<callerid:operoverride>` has been removed. If you wish to keep this behaviour then you should give your server operators the `users/ignore-callerid` privilege.

- `<chanfilter>` has been removed. If you wish to keep this behaviour you should rename it to `<maxlist mode="filter">`.

- `<connect:allowmotdcolors>` has been removed with no replacement (now always enabled).

- `<exemptchanops>` has been removed. If you wish to keep this behaviour you should rename it to `<maxlist mode="exemptchanops">`.

- `<gnutls:advertisedports>` has been removed with no replacement.

- `<gnutls:showports>` has been removed with no replacement (now always disabled).

- `<gnutls:dhbits>` has been removed with no replacement. You must now provide a DH parameter file for the server to use instead.

- `<gnutls:starttls>` has been removed. If you wish to keep this behaviour then you should load the new starttls module. See the documentation in modules.conf.example for more details.

- `<host:prefix>` has been removed. If you wish to keep this behaviour you should move the prefix field to your `<hostchange>` blocks

- `<host:separator>` has been removed. If you wish to keep this behaviour you should append or prepend it to your `<hostchange:prefix>` or `<hostchange:suffix>` tags as appropriate.

- `<host:suffix>` has been removed. If you wish to keep this behaviour you should move the suffix field to your `<hostchange>` blocks

- `<nonicks:operoverride>` has been removed. If you wish to keep this behaviour then you should give your server operators the `channels/ignore-nonicks` privilege.

- `<options:cyclehosts>` has been removed. If you wish to keep this behaviour then you should load the new hostcycle module. See the documentation in modules.conf.example for more details.

- `<options:ircumsgprefix>` has been removed with no replacement (now always disabled).

- `<openssl:advertisedports>` has been removed with no replacement.

- `<openssl:cipherserverpref>` has been removed with no replacement (now always enabled).

- `<openssl:showports>` has been removed with no replacement (now always disabled).

- `<openssl:sslv3>` has been removed with no replacement (now always disabled).

- `<opermotd:processcolors>` has been removed with no replacement (now always enabled).

- `<options:welcomenotice>` has been removed with no replacement (now always disabled).

- `<performance:limitsomaxconn>` has been removed with no replacement (now always disabled).

- `<redirect:antiredirect>` has been removed with no replacement (now always enabled).

- `<restrictmsg:uline>` has been removed with no replacement (now always enabled).

- `<security:hidemodes>` has been removed. If you wish to keep this behaviour then you should load the new hidelist module. See the documentation in modules.conf.example for more details.

- `<security:operspywhois>` has been removed. If you wish to keep this behaviour then you should give your server operators the `users/channel-spy` privilege and enable the `<options:splitwhois>` setting.

- `<sqloper:hash>` has been removed. If you wish to keep this behaviour then you should add a `hash` column to your SQL table and populate it with the hash you have used for your server operators.
