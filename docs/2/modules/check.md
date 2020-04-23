---
title: Module Details: check (v2)
---

{! 2/_support.md !}

## The "check" Module

### Description

This module adds the `/CHECK` command which allows server operators to look up details about a channel, user, IP address, or hostname.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_check.so">
```

This module requires no other configuration.

### Commands

Name  | Parameter Count | Syntax                                                                                            | Description
----- | --------------- | ------------------------------------------------------------------------------------------------- | -----------
CHECK | 1-2             | `<channel> [<server>]`<br>`<nickname> [<server>]`<br>`<ip> [<server>]`<br>`<hostname> [<server>]` | Looks up information about the specified channel, user, IP address, or hostname.

#### Example Usage

Looks up details relating to #channel:

```plaintext
/CHECK #example
```

Looks up details relating to Sadie on irc2.example.com:

```plaintext
/CHECK Sadie irc2.example.com
```
