---
title: InspIRCd Spanning Tree Protocol &mdash; Example Connection
---

## Example Connection

This example represents an example connection between two servers.

- Lines beginning with ◀️ are outgoing messages.
- Lines beginning with ▶️ are incoming messages.

Servers start by negotiating a protocol version. The lowest version supported by both servers is used. If there is no common supported version then the server should send [`ERROR`](/server/messages/error) and disconnect.

```plaintext
◀️ CAPAB START 1205
▶️ CAPAB START 1205
```

Once a protocol version has been negotiated servers can send their rest of their capabilities. It is the responsibility of the remote server to check that the local server has the same modes and modules as it. If a server does not wish to check for module or mode synchronisations then it should not send the associated messages. If any capabilities are mismatched then then the server should send [`ERROR`](/server/messages/error) and disconnect.

```plaintext
◀️ CAPAB MODULES :m_required1.so=data m_required2.so
◀️ CAPAB MODSUPPORT :m_optional1.so m_optional2.so=data
◀️ CAPAB CHANMODES :list:ban=b param-set:limit=l param:key=k prefix:10000:voice=+v prefix:30000:op=@o simple:inviteonly=i simple:moderated=m simple:noextmsg=n simple:private=p simple:secret=s simple:topiclock=t
◀️ CAPAB USERMODES :param-set:snomask=s simple:invisible=i simple:oper=o simple:wallops=w
◀️ CAPAB CAPABILITIES :NICKMAX=30 CHANMAX=64 MAXMODES=20 IDENTMAX=10 MAXQUIT=255 MAXTOPIC=307 MAXKICK=255 MAXREAL=128 MAXAWAY=200 MAXHOST=64 MAXLINE=512 CASEMAPPING=ascii GLOBOPS=0
◀️ CAPAB END

▶️ CAPAB MODULES :m_required1.so=data m_required2.so
▶️ CAPAB MODSUPPORT :m_optional1.so m_optional2.so=data
▶️ CAPAB CHANMODES :list:ban=b param-set:limit=l param:key=k prefix:10000:voice=+v prefix:30000:op=@o simple:inviteonly=i simple:moderated=m simple:noextmsg=n simple:private=p simple:secret=s simple:topiclock=t
▶️ CAPAB USERMODES :param-set:snomask=s simple:invisible=i simple:oper=o simple:wallops=w
▶️ CAPAB CAPABILITIES :NICKMAX=30 CHANMAX=64 MAXMODES=20 IDENTMAX=10 MAXQUIT=255 MAXTOPIC=307 MAXKICK=255 MAXREAL=128 MAXAWAY=200 MAXHOST=64 MAXLINE=512 CASEMAPPING=ascii GLOBOPS=0
▶️ CAPAB END
```

Once capability negotiation is complete servers can send their server information. This is used for authenticating the remote server against the local server's link config. If the remote server hostname and password do not match or there is already a server using the same hostname or SID then the local server should send [`ERROR`](/server/messages/error) and disconnect.

```plaintext
▶️ SERVER irc2.example.com wobble 0 079 :Second Server
◀️ SERVER irc1.example.com wibble 0 702 :First Server
```

Once servers are fully connected they can send their network state. This includes all server information, users, channels, servers, and metadata.

```plaintext
▶️ :079 BURST 1665473585
◀️ :702 BURST 1665473585
◀️ :702 SINFO version :InspIRCd-3. irc1.example.com :
◀️ :702 SINFO fullversion :InspIRCd-3.2.1. irc1.example.com :[702]
◀️ :702 SINFO rawversion :InspIRCd-3.2.1
◀️ :702 UID 702AAAAAB 1665473547 ServerOneClient 127.0.0.1 127.0.0.1 serverone 127.0.0.1 1665473527 + :Client on Server Two
◀️ :702 FJOIN #test 1665473560 +nt :o,702AAAAAB:2
◀️ :702 METADATA #test 1665473560 maxlist :b 100
◀️ :702 FJOIN #test1 1665473560 +nt :o,702AAAAAB:1
◀️ :702 METADATA #test1 1665473560 maxlist :b 100
◀️ :702 ENDBURST

▶️ :079 SINFO version :InspIRCd-3. irc2.example.com :
▶️ :079 SINFO fullversion :InspIRCd-3.2.1. irc2.example.com :[079]
▶️ :079 SINFO rawversion :InspIRCd-3.2.1
▶️ :079 UID 079AAAAAA 1665473551 ServerTwoClient 127.0.0.1 127.0.0.1 servertwo 127.0.0.1 1665473536 + :Client on Server Two
▶️ :079 FJOIN #test 1665473554 +nt :o,079AAAAAA:1
▶️ :079 METADATA #test 1665473554 maxlist :b 100
▶️ :079 FJOIN #test2 1665473554 +nt :o,079AAAAAA:0
▶️ :079 METADATA #test2 1665473554 maxlist :b 100
▶️ :079 ENDBURST
```

The two servers are now synchronised and can send messages normally.
