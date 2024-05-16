---
title: InspIRCd Spanning Tree Protocol &mdash; Change Log
---

##  Change Log

{! server/_dev.md !}

## 1206 (v4)

!!! danger "InspIRCd v4 is still early in development!"
    If you implement the 1206 protocol you may experience unannounced breaking changes.

    You probably want to use [the 1205 (v3) protocol](#1205-v3) instead which v4 also supports.

- Channel and user mode `r` (c_registered, u_registered) have been made optional and may no longer exist.

```diff
- CABAB CHANMODES :simple:c_registered=r
- CABAB USERMODES :simple:u_registered=r
```

- Membership metadata can now be synchronised between servers using the `METADATA` message.

```diff
+ :36D METADATA @ 36DAAAAAA #channel 1234567890 2345678901 wibble :wobblw
```

- Module link data in `CAPAB MODULES` and `CAPAB MODSUPPORT` is now sent as a series of key-value pairs with the same syntax as an URI query string (i.e. `key=1value1&key2;key3=value3;key4`).

```diff
- CAPAB MODULES :m_foo.so m_bar.so=wibble
+ CAPAB MODULES :foo bar=key1=value1&key2;key3=value%203
```

- Module names in `CAPAB MODULES` and `CAPAB MODSUPPORT` no longer include the `m_` prefix or `.so` file extension.

```diff
- CAPAB MODULES :m_foo.so m_bar.so m_baz.so
+ CAPAB MODULES :foo bar baz
```

- Modules which were split, merged, or renamed in v4 will be reported in `CAPAB MODULES` using their new names.

    - `m_cloaking.so` => `cloak`
    - `m_gecosban.so` => `realnameban`
    - `m_services_account.so` => `account` and `services`.
    - `m_svshold.so` => `services`.
    - `m_topiclock.so` => `services`.

```diff
- CAPAB MODULES :m_cloaking.so m_gecosban.so m_services_account.so
+ CAPAB MODULES :account cloak realnameban services
```

- Server queries (`SQUERY`) are now sent as unicast messages to their target user instead of being encapsulated in a `PRIVMSG`.

```diff
- :36DAAAAAA PRIVMSG NickServ :IDENTIFY hunter2
+ :36DAAAAAA SQUERY NickServ :IDENTIFY hunter2
```

- The `accountnicks` metadata key may now be sent to inform the server of valid nicknames for a user's account. This replaces channel mode `r` (u_registered).

```diff
- :36C MODE 36DAAAAAA +r
+ :36C METADATA 36DAAAAAA accountnicks :Sadie Eidas
```

- The `CHANMAX`, `IDENTMAX`, and `NICKMAX` keys in `CAPAB CAPABILITIES` have been renamed to `MAXCHANNEL`, `MAXUSER`, and `MAXNICK` respectively for consistency.

```diff
- CAPAB CAPABILITIES :CHANMAX=60 IDENTMAX=10 NICKMAX=30
+ CAPAB CAPABILITIES :MAXCHANNEL=60 MAXUSER=60 MAXNICK=30
```

- The `EXTBANS` key in `CAPAB CAPABILITIES` has been replaced with the `CAPAB EXTBANS` message.

```diff
- CAPAB CAPABILITIES :EXTBANS=ABCdef
+ CAPAB EXTBANS :acting:mute=m matching:unauthed=U matching:account=R
```

- The `FHOST` message now takes a second parameter which, if not a `*`, signifies a change of the real hostname of a user .

```diff
- :36DAAAAAA FHOST fake.host.name
+ :36DAAAAAA FHOST fake.host.name real.host.name
+ :36DAAAAAA FHOST * real.host.name
+ :36DAAAAAA FHOST fake.host.name *
```

- The `FIDENT` message now takes a second parameter which, if not a `*`, signifies a change of the real username of a user .

```diff
- :36DAAAAAA FHOST fake.user.name
+ :36DAAAAAA FHOST fake.user.name real.user.name
+ :36DAAAAAA FHOST * real.user.name
+ :36DAAAAAA FHOST fake.user.name *
```

- The `GLOBOPS` key in `CAPAB CAPABILITIES` has been removed. Instead, the globops module can be detected by its presence in `CAPAB MODSUPPORT`.

```diff
- CAPAB CAPABILITIES :GLOBOPS=0
+ CAPAB MODSUPPORT :globops
```

- The `UID` message now has an extra field for the real username of the user which is being introduced.

```diff
- :36D UID 36DAAAAAA 1234567890 Sadie localhost sadie.moe sadie 127.0.0.1 1234567890 +i :Sadie
+ :36D UID 36DAAAAAA 1234567890 Sadie localhost sadie.moe sp91 sadie 127.0.0.1 1234567890 +i :Sadie
```

- The `LMODE` message was added to synchronise the contents of a mode list including the setter and set time.

```diff
- :36D FMODE #CHANNEL 1234567890 +bb *!*@example.com *!*@example.org
+ :36D LMODE #channel 1234567890 b *!*@example.com 1234567890 Sadie *!*@example.org 2345678901 Adam
```

- The `version` and `fullversion` keys in `SINFO` were deprecated and replaced with `customversion` and `rawbranch`. If sent the deprecated keys will be parsed to attempt to extract the latter values from them.

```diff
- :36D SINFO fullversion :InspIRCd-4.0.0-a10. sadie.testnet.inspircd.org :[597] Test
- :36D SINFO version :InspIRCd-4. testnet.inspircd.org :Test
+ :36D SINFO customversion :Test
+ :36D SINFO rawbranch :InspIRCd-4
```

- The `~context=<chan>` tag can now be sent to make a user-targeted `PRIVMSG`, `NOTICE`, or `TAGMSG` appear to be sent to a channel.

```diff
- :36DAAAAAA NOTICE 36EAAAAAA :[#channel] Welcome to #channel. Make sure to introduce yourself.
+ @~context=#channel :36DAAAAAA NOTICE 36EAAAAAA :Welcome to #channel. Make sure to introduce yourself.
```

## 1205 (v3)

- IRCv3 message tags are now supported.

```diff
- :36D FOO bar baz
+ @foo=bar;baz :36D FOO bar baz
```

- The `BURST` message is no longer sent for indirectly-linked servers.

```diff
- :36D BURST 3133641600
```

- The `CAPAB CHANMODES` and `CAPAB USERMODES` messages have been extended to include the type of mode and mode rank (if applicable). The new format is `<type>[:<rank>]:<name>=[<prefix>]<letter>`.

```diff
- CAPAB CHANMODES :ban=b key=k limit=l op=@o moderated=m
+ CABAB CHANMODES :list:ban=b param:key=k param-set:limit=l prefix:30000:op=@o simple:moderated=n
```

- The `CHANMODES` token in the `CAPAB CAPABILITIES` message was removed.  This is now provided in `CAPAB CHANMODES` instead.

```diff
- CAPAB CAPABILITIES :FOO=123 CHANMODES=b,k,l,imnpstr BAR=456
+ CAPAB CAPABILITIES :FOO=123 BAR=456
```

- The `ELINE`, `GLINE`, `KLINE`, `QLINE`, and `ZLINE` messages have been removed. You should use `ADDLINE` and `DELLINE` instead.

```diff
- :36D ELINE *@example.com 60 :Example
- :36D ELINE *@example.com
+ :36D ADDLINE E *@example.com Sadie 420 60 :Example
+ :36D DELLINE E *@example.com
```

- The `FJOIN` message now includes unique membership identifiers for members.

```diff
- :36D FJOIN #chan 3133641600 +l 69 :o,36DAAAAAA v,36DAAAAAA
+ :36D FJOIN #chan 3133641600 +l 69 :o,36DAAAAAA:420 o,36DAAAAAB:69
```

- The `FMODE` message no longer supports changing user modes. You should use `MODE` instead.

```diff
- :36DAAAAAA FMODE 36DAAAAAA 69 +os Aa
+ :36DAAAAAA MODE 36DAAAAAA +os Aa
```

- The `FTOPIC` message now has the channel creation time as the second parameter.

```diff
- :36D FTOPIC #chan 69 Sadie :Welcome to the cool zone!
+ :36D FTOPIC #chan 420 69 Sadie :Welcome to the cool zone!
```

- The `IJOIN` message has been added for joins to an existing channel.

```diff
- :36D FJOIN #chan 69 + :o,36DAAAAAA
+ :36DAAAAAA IJOIN #chan 420 69 o
```

- The `INVITE` message now has the channel creation time as the third parameter.

```diff
- :20D INVITE 36DAAAAAA #chan
+ :20D INVITE 36DAAAAAA #chan 69
```

- The `JOIN` message has been removed. You should send `FJOIN` instead.

```diff
- :36DAAAAAA JOIN #chan
+ :36D FJOIN #chan 69 + :,36DAAAAAA
```

- The `KICK` message now has a membership identifier as the third parameter.

```diff
- :36DAAAAAA KICK #chan 36DAAAAAB :Begone vile troll!
+ :36DAAAAAA KICK #chan 36DAAAAAB 69 :Begone vile troll!
```

- The `MAXGECOS` token in the `CAPAB CAPABILITIES` message was renamed to `MAXREAL`.

```diff
- CAPAB CAPABILITIES :FOO=123 MAXGECOS=100 BAR=456
+ CAPAB CAPABILITIES :FOO=123 MAXREAL=100 BAR=456
```

- The `METADATA` message when sent with a channel target now has the channel creation time as the second parameter.

```diff
- :36D METADATA #channel wibble :wobble
+ :36D METADATA #channel 69 wibble :wobble
```

- The `MODENOTICE` message was moved to a module. You should send it with `ENCAP` to avoid causing a netsplit.

```diff
- :36DAAAAAA MODENOTICE o :Greetings fellow opers!
+ :36DAAAAAA ENCAP * MODENOTICE o :Greetings fellow opers!
```

- The `OPERQUIT` message has been replaced with the `operquit` user metadata.

```diff
- :36DAAAAAA OPERQUIT :Spammer
+ :36D METADATA 36DAAAAAA operquit :Spammer
```

- The `OPERTYPE` message can now handle sending a server operator type that contains spaces.

```diff
- :36DAAAAAA OPERTYPE Network_Administrator
+ :36DAAAAAA OPERTYPE :Network Administrator
```

- The `PING` message no longer has the source server identifier as the first parameter.

```diff
- :36D PING 36D 36E
+ :36D PING 36E
```

- The `PING` message now requires that the target is a server identifier instead of a server name.

```diff
- :36D PING irc2.example.com
+ :36D PING 36E
```

- The `PREFIX` token in the `CAPAB CAPABILITIES` message was removed.  This is now provided in `CAPAB CHANMODES` instead.

```diff
- CAPAB CAPABILITIES :FOO=123 PREFIX=(ov)@+ BAR=456
+ CAPAB CAPABILITIES :FOO=123 BAR=456
```

- The `PROTOCOL` token in the `CAPAB CAPABILITIES` message was removed. This is now provided as as a parameter to `CAPAB START` instead.

```diff
- CAPAB CAPABILITIES :FOO=123 PROTOCOL=1202 BAR=456
+ CAPAB START 1205
```

- The `PUSH` message has been removed. You should use `NUM` for sending numerics instead.

```diff
- :36D PUSH 36EAAAAAA ::irc2.example.com 375 Sadie :irc2.example.com message of the day
+ :36D NUM 36D 36EAAAAAA 375 :irc2.example.com message of the day
```

- The `RESYNC` message has been added to resynchronise the state of a channel if an `IJOIN` is sent for an unknown channel.

```diff
+ :36D RESYNC #chan
```

- The `RULES` message has been removed with no replacement.

```diff
- :36DAAAAAA RULES *.example.com
```

- The `SERVER` message for indirectly-linked servers can now contain data about the server and no longer includes a dummy password and hop count.

```diff
- 36D SERVER irc2.example.com 36E * 0 :Server no. 2
+ 36D SERVER irc2.example.com 36E burst=69 hidden=yes :Server no. 2
```

- The `SINFO fullversion` message was added to allow opers to see the full version in `/VERSION`.

```diff
+ :36D SINFO fullversion :InspIRCd-3.2.1. irc2.example.com :[36D]
```

- The `SINFO rawversion` message was added to allow opers to see the full version in `/MAP`.

```diff
+ :36D SINFO rawversion :InspIRCd-3.2.1
```

- The `SVSMODE` message was renamed to `MODE`.

```diff
- :36DAAAAAA SVSMODE 36EAAAAAA +o
+ :36DAAAAAA MODE 36EAAAAAA +o
```

- The `SVSSILENCE` message has been replaced with the `silence-list` user metadata.

```diff
- :36D SVSSILENCE 36EAAAAAA +foo@bar@baz cnpt
+ :36D METADATA 36EAAAAAA silence-list :foo!bar@baz NnPp
```

- The `SVSWATCH` message has been removed with no replacement.

```diff
- :36DAAAAAA SVSWATCH 36EAAAAAA +Sadie
```

- The `TOPIC` message has been removed. You should use `FTOPIC` instead.

```diff
- :36D TOPIC #chan Sadie :Welcome to the cool zone!
+ :36D FTOPIC #chan 420 69 Sadie :Welcome to the cool zone!
```

- The `USERMODES` token in the `CAPAB CAPABILITIES` message was removed.  This is now provided in `CAPAB USERMODES` instead.

```diff
- CAPAB CAPABILITIES :FOO=123 USERMODES=,,s,iow BAR=456
+ CAPAB CAPABILITIES :FOO=123 BAR=456
```

- The `VERSION` message has been removed. You should send `SINFO version` instead.

```diff
- :36D VERSION :InspIRCd-3.2. irc2.example.com :
+ :36D SINFO version :InspIRCd-3.2. irc2.example.com :
```

- The length of messages post-authentication is no longer limited.

```diff
- :36D FJOIN #chan 3133641600 +l 69 :o,36DAAAAAA:420
- :36D FJOIN #chan 3133641600 +l 69 :o,36DAAAAAB:69
+ :36D FJOIN #chan 3133641600 +l 69 :o,36DAAAAAA:420 o,36DAAAAAB:69
```
