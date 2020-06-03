---
title: Frequently Asked Questions
---

## Frequently Asked Questions

More FAQs may be found at:

- [Windows FAQs](/faq/windows)

### Can I use InspIRCd on my large network?

Yes! InspIRCd is being used on some networks with more than 100,000 clients.

The number of users you can support per-server is dependent on your chosen modules, server hardware, and network connection but regardless if you have a lot of users you should probably consider spreading them out over multiple geographically distributed servers for redundancy reasons.

### How do I get prefixes like `%`, `~`, and `&`?

These prefixes are provided by the customprefix module. You should load this module and then define the appropriate `<customprefix>` tags to add those prefixes ([v2 docs](/2/modules/customprefix), [v3 docs](/3/modules/customprefix)).

### How do I start InspIRCd when the system boots?

To launch InspIRCd when your system starts you should place the following line into the crontab for your IRCd user (crontab -e):

```sh
# Replace [PATH] with the path to your InspIRCd bin directory.
@reboot [PATH]/inspircd
```

If you are using InspIRCd 3 or newer you may also use our included systemd unit files:

```sh
sudo systemctl enable inspircd.service
```

### I have found a bug where should I report it?

Security bugs should be emailed privately to an InspIRCd core developer. All other bugs should be reported on our [issue tracker](https://github.com/inspircd/inspircd/issues).

Please do not use IRC for reporting bugs as your report may be buried and forgotten about.

### I have a feature request where should I post it?

All feature requests should be posted on our [issue tracker](https://github.com/inspircd/inspircd/issues).

Please do not use IRC for requesting features as your request may be buried and forgotten about.

### What services package should I use?

Common services packages used with InspIRCd are:

- [Anope](https://anope.org)

- [Atheme](https://atheme.github.io/atheme.html)

### Why don't I have channel privileges even though I'm a server operator?

Server operators do not automatically get channel privileges by default. You can change this by:

- Giving server operators a channel status using the operprefix module ([v2 docs](/2/modules/operprefix), [v3 docs](/3/modules/operprefix)).

- Overriding your lack of privileges using the override module ([v2 docs](/2/modules/override), [v3 docs](/3/modules/override)).

- Giving yourself channel operator status using the samode module ([v2 docs](/2/modules/samode), [v3 docs](/3/modules/samode)).

### Why does my server tell me "An unexpected TLS packet was received" or "error:1408F10B:SSL routines:ssl3_get_record:wrong version number:ssl/record/ssl3_record.c" when I try to connect using SSL/TLS?

You are trying to connect using SSL/TLS but your server is not configured to listen for SSL/TLS connections.

Check that you have a TLS (SSL) module loaded and that your bind tag has the name of a TLS (SSL) module (if you're using v2) or the name of a TLS (SSL) profile (if you're using v3) in `<bind:ssl>`.

### Why does my client not show mode changes/opped users on join/etc correctly when using InspIRCd v3?

InspIRCd v3 changed the way that we emit messages in order to allow support for new IRCv3 extensions which require message tags to be implemented. The new way we emit messages is entirely valid according to the the formatting rules in part 2.3.1 of RFC 1459 (note two is of specific relevance here) but unfortunately several clients were found to be incompliant with the rules specified in this section.

This issue is fixed in many clients already. Please make sure you have updated to the latest version and if you are still having an issue then please report it to your client author. Your client author might find it useful to know that [ircdocs provides test vectors](https://github.com/ircdocs/parser-tests) for testing their message parser compliance.

This bug is known to be fixed in:

- AdiIRC 3.6 (released November 2019)
- HexChat 2.14.3 (released December 2019).
- Irssi 1.1.0 (released January 2018).
- WeeChat v2.5 (released June 2019).
- ZNC 1.8 (released May 2020).

If you are using v2 and want to warn users to upgrade their client you can install the clientcheck contrib module via [the Module Manager](/2/module-manager) and use the following config:

```xml
<module name="m_clientcheck.so">

<clientcheck engine="pcre">

<client match="^AdiIRC (?:[0-2]\.|3\.[0-5] )"
        message="[WARNING] You have been detected as using an broken version of AdiIRC. This client will have problems connecting in the future. Please upgrade to v3.6 or newer to fix this issue.">

<client match="^HexChat 2\.(?:[0-9]\.|1[0-3]\.|14\.[0-2] )"
        message="[WARNING] You have been detected as using an broken version of HexChat. This client will have problems connecting in the future. Please upgrade to v2.14.3 or newer to fix this issue.">

<client match="^irssi v(?:0\.|1\.0\.)"
        message="[WARNING] You have been detected as using an broken version of Irssi. This client will have problems connecting in the future. Please upgrade to v1.1.0 or newer to fix this issue.">

<client match="^WeeChat (?:1\.|2\.[0-4][\. ])"
        message="[WARNING] You have been detected as using an broken version of WeeChat. This client will have problems connecting in the future. Please upgrade to v2.5.0 or newer to fix this issue.">

<client match="^ZNC (?:0\.|1\.[0-7][\. ])"
        message="[WARNING] You have been detected as using an broken version of ZNC. This client will have problems connecting in the future. Please upgrade to v1.8.0 or newer to fix this issue.">
```