---
title: How to prevent spam on your IRC network
---

## How to prevent spam on your IRC network

Unfortunately spam is still an issue on IRC. However, with the right server configuration you can keep your network safe from the vast majority of spam.

Before applying any mitigations there is something important to remember: **DO NOT FEED THE TROLLS**. Most IRC spammers are pathetic losers who are trying to waste your time or get a reaction out of you. Do not attempt to follow their spam to complain as they often use false flags to implicate an innocent third party or have traps set up on their own IRC network (e.g. a bot that joins you to channels until your client crashes) to cause further problems. There's nothing you can do to change their behaviour other than block their spam so it's not fun for them anymore.

### Require account registration

Almost all spam happens from unregistered users. Requiring registration to send messages is the most reliable way to stop automated spam on your IRC network because spambots are generally unable to confirm accounts.

Some bots may attempt to register accounts to bypass filters on networks that don't have account confirmation. This can be fixed by ensuring your services package requires confirmation of account registration. In Anope check that that the `registration` option of the ns_register module is not set to `none`. In Atheme check that `serverinfo:auth` is not set to `none`.

In order to enact this on your network you can:

0. Load [the conn_umodes module](/3/modules/conn_umodes) if not already loaded.

0. Load [the services_account module](/3/modules/services_account) if not already loaded.

0. Add [user mode `R` (regdeaf)](/3/modules/services_account/#user-modes) to [`<connect:modes>`](/3/modules/conn_umodes/#connect). This will require that users have to be logged into an account to send a private message to any new users.

0. Add [channel mode `M` (regmoderated)](/3/modules/services_account/#user-modes) to [`<options:defaultmodes>`](/3/configuration/#options). This will require that users have to be logged into an account to send a message to any new channels.

0. Encourage your existing users to add these modes on existing channels. You can also add these modes manually to existing channels and users using [the /SAMODE command](/3/modules/samode).

### Check connections against a DNSBL

Many other IRC networks will be encountering the same bots as you and have may already added them to a DNSBL. You can scan new users against these lists by loading [the dnsbl module](/3/modules/dnsbl) and configuring some DNSBLs to check against.

There are three main DNSBLs which are typically used by InspIRCd networks:

- [DroneBL](https://dronebl.org/)
- [EFnet RBL](https://rbl.efnetrbl.org/)
- [torexit.dan.me.uk](https://www.dan.me.uk/dnsbl)

Preconfigured profiles for these DNSBLs are available in the [on the dnsbl module page](https://docs.inspircd.org/3/modules/dnsbl/#dnsbl).

### Check connections with a proxy scanner

Even if a spammer is using a host which has not previously been blacklisted for spam you can use a scanner like [HOPM](https://github.com/ircd-hybrid/hopm) to scan all new clients for HTTP/SOCKS/WinGate proxies and insecure software that is often exploited by spammers.

Depending on your local laws and server provider terms of service this may not be legal. However, to our knowledge no IRC admin has ever had any legal trouble for port scanning users for the purposes of spam prevention despite IRC networks doing so for decades. The [NMAP book](https://nmap.org/book/legal-issues.html) contains an article about the legality of port scanning which may be of interest to IRC server admins.

### Required users of shared providers authenticate with SASL

If you can't require all users use an account you should consider requiring users of shared hosts to be authenticated to be allowed to connect. Common shared hosts which spam has been seen from are:

- AWS &mdash; `*.amazonaws.com`
- Google Cloud &mdash; `*.googleusercontent.com`
- Linode &mdash; `*.linodeusercontent.com`

A configuration for how to do this can be found on [the useful snippets page](/3/configuration/useful-snippets/#requiring-connections-to-use-sasl).

If you want a softer option you can also use [the muteban module](/3/modules/muteban) and the [the services_account module](/3/modules/services_account) to ban unregistered users from those providers in your channels.

```plaintext
/MODE #channel +b m:U:*!*@*.amazonaws.com
/MODE #channel +b m:U:*!*@*.googleusercontent.com
/MODE #channel +b m:U:*!*@*.linodeusercontent.com
```

### Require TLS (SSL)

Some IRC spambots are very poorly written and do not support TLS (SSL). You can break these bots by requiring TLS (SSL) on your IRC network. This also has the benefit of preventing your users from having their chats snooped on. To do this you can either disable your plaintext listeners entirely or better still use the IRCv3 STS (Strict Transport Security) feature to redirect users of modern clients to your TLS (SSL) port.

```xml
# These can go anywhere in your configuration
<module name="ircv3_sts">

<sts host="*.example.com"
     duration="60d"
     port="6697"
     preload="yes">

# These go above your main connect class
<connect allow="*"
         registered="no"
         port="6667">

<connect deny="*"
         registered="yes"
         port="6667"
         reason="Plain text connections are not allowed on this server. Please reconnect to irc.example.com/+6697 using TLS.">
```

### Filtering messages

If the other methods on this page are not feasible or you are still having issues you can use [the filter module](/3/modules/filter) to block messages that are sent by spammers.

### Useful third-party modules

The `inspircd-contrib` repository contains several third-party modules which may be useful for spam prevention. These modules are checked for obvious issues by the InspIRCd Team before they are merged but may not meet the same levels of stability as the official modules shipped with InspIRCd.

- [blockhighlight](https://github.com/inspircd/inspircd-contrib/blob/master/3/m_blockhighlight.cpp) (`./modulemanager install m_blockhighlight`) &mdash; Adds channel mode `V` (blockhighlight) which kills users who attempt to highlight multiple users.

- [fakelist](https://github.com/inspircd/inspircd-contrib/blob/master/3/m_fakelist.cpp) (`./modulemanager install m_fakelist`) &mdash; An alternative to [the securelist module](/3/modules/securelist) that responds to `/LIST` with a list of spamtrap channels that kill users who join them.

- [kill_idle](https://github.com/inspircd/inspircd-contrib/blob/master/3/m_kill_idle.cpp) (`./modulemanager install m_kill_idle`) &mdash; Allows killing users who are idle. Can be configured to kill users that have been connected for a while but have not joined any channels which is a common tactic used by spambots to evade spamfilters.

- [solvemsg](https://github.com/inspircd/inspircd-contrib/blob/master/3/m_solvemsg.cpp) (`./modulemanager install m_solvemsg`) &mdash; Requires users solve a basic maths problem before they can message others.

- [tgchange](https://github.com/inspircd/inspircd-contrib/blob/master/3/m_tgchange.cpp) (`./modulemanager install m_tgchange`) &mdash; Prevents users from messaging lots of targets at the same time.
