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
