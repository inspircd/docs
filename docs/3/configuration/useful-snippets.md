---
title: v{{ version }} Configuration
---

{% if '4' == version %}
{! 4/_support.md !}
{% endif %}

## Useful Configuration Snippets

### Enabling support for connections via hosted clients

{% if '3' == version %}As of v3.4.0 {% endif %}InspIRCd ships with preconfigured files for enabling support for popular hosted clients on your server.

To add support for IRCCloud add the following include tag to your configuration:

```xml
<include file="examples/providers/irccloud.conf.example">
```

If you run a popular hosted client or a shared bouncer service that supports modern IRC features we would be happy to include configs for your client. Please reach out to us via \#inspircd.dev on irc.inspircd.org and we'll try to work something out.

### Requiring connections to use SASL

To do this you create an allow connect class which only applies pre-connection and two connect classes that apply post-connection. The first being an allow connect class with `<connect:requireaccount>` set to yes (requires [the sasl module](/{{ version }}/modules/sasl) and the [the services_account module](/{{ version }}/modules/services_account)) and the second being a deny connect class with a reason explaining to the user why they cannot connect.

You can also combine this with other `<connect>` fields such as adding `port="6660-6669"` to only apply to plain text connections or `webirc="*"` to only apply to connections via WebIRC gateways (requires [the cgiirc module](/{{ version }}/modules/cgiirc)).

```xml
<connect name="before-reg"
         allow="*"
         registered="no">

<connect name="authed"
         allow="*"
         registered="yes"
         requireaccount="yes">

<connect name="no-auth"
         deny="*"
         registered="yes"
         requireaccount="no"
         reason="You must authenticate using SASL to connect to this server.">
```
