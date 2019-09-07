---
title: Module Details (banredirect)
---

{! 2/_support.md !}

## The "banredirect" Module

### Description

This module allows specifying a channel to redirect a banned user to in the ban mask.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_banredirect.so">
```

This module requires no other configuration.

### Channel Modes

This module does not add any new channel modes but instead extends channel mode `b` (ban) to allow ban masks to be suffixed with the name of a channel to redirect users who match the ban to.

#### Example Usage

Redirects users matching `*!*@example.com` to #banned-channel.

```plaintext
/MODE #channel +b *!*@example.com#banned-channel
```

### Special Notes

When setting a ban redirect the target channel should exist and the user setting the ban should have channel operator status in it.

When the banredirect module is unloaded all ban redirects will be converted to normal bans.
