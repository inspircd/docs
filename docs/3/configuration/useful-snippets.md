---
title: v3 Configuration
---

## Useful Configuration Snippets

### Enabling support for connections via hosted clients

As of v3.4.0 InspIRCd ships with preconfigured files for enabling support for popular hosted clients on your server.

To add support for KiwiIRC.com add the following include tag to your configuration:

```xml
<include file="examples/providers/kiwiirc-com.conf.example">
```

To add support for IRCCloud add the following include tag to your configuration:

```xml
<include file="examples/providers/irccloud.conf.example">
```

If you run a popular hosted client or a shared bouncer service that supports modern IRC features we would be happy to include configs for your client. Please reach out to us via \#inspircd.dev on irc.inspircd.org and we'll try to work something out.

### Requiring connections to use SASL

To do this you create an allow connect class which only applies pre-connection and then a deny class which only applies post-connection which has `<connect:requireaccount>` set to yes (requires [the sasl module](/3/modules/sasl) and the [the services_account module](/3/modules/services_account)).

You can also combine this with other `<connect>` fields such as adding `port="6660-6669"` to only apply to plain text connections or `webirc="*"` to only apply to connections via WebIRC gateways (requires [the cgiirc module](/3/modules/cgiirc)).

```xml
<connect allow="*"
         registered="no"
         name="before-reg">

<connect allow="*"
         requireaccount="yes"
         registered="yes"
         name="authed">

<connect deny="*"
         registered="yes"
         requireaccount="no"
         reason="You must authenticate using SASL to connect to this server."
         name="no-auth">
```
