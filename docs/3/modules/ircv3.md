---
title: Module Details (ircv3)
---

## The "ircv3" Module

### Description

This module provides the IRCv3 `account-notify`, `away-notify`, and `extended-join` client capabilities.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3">
```

#### `<ircv3>`

The `<ircv3>` tag defines settings about how the ircv3 module should behave. This tag can only be defined once.

Name          | Type    | Default Value | Description
------------- | ------- | ------------- | -----------
accountnotify | Boolean | Yes           | Whether the `account-notify` client capability is enabled.
awaynotify    | Boolean | Yes           | Whether the `away-notify` client capability is enabled.
extendedjoin  | Boolean | Yes           | Whether the `extended-join` client capability is enabled.

```xml
<ircv3 accountnotify="yes"
       awaynotify="yes"
       extendedjoin="yes">
```

### Client Capabilities

Name                                                                         | Description
---------------------------------------------------------------------------- | -----------
[account-notify](https://ircv3.net/specs/extensions/account-notify-3.1.html) | Allows the client to be notified when a user's account name changes.
[away-notify](https://ircv3.net/specs/extensions/away-notify-3.1.html)       | Allows the client to be notified when a user's away status changes.
[extended-join](https://ircv3.net/specs/extensions/extended-join-3.1.html)   | Extends the server-to-client JOIN message to include the joining user's account name and real name.
