---
title: Module Details: override (v3)
---

## The "override" Module

### Description

This module allows server operators to be given privileges that allow them to ignore various channel-level restrictions.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="override">
```

#### `<oper>` &amp; `<type>`

This module extends the core `<oper>` and `<type>` tags with the following fields:

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
override | Text | *None*        | A space-delimited list of channel-level restrictions that a server operator can ignore.

The override field should be set to one or more of the following values:

Value   | Description
------- | -----------
BANWALK | Allows the server operator to ignore any bans which match them.
INVITE  | Allows the server operator to ignore channel mode `i` (inviteonly).
KEY     | Allows the server operator to ignore channel mode `k` (key).
KICK    | Allows the server operator to ignore channel privileges when kicking users.
LIMIT   | Allows the server operator to ignore channel mode `l` (limit).
MODE    | Allows the server operator to ignore channel privileges when changing channel modes.
TOPIC   | Allows the server operator to ignore channel privileges when changing channel topics.

##### Example Usage

Allows Sadie to ignore any restrictions that might prevent them from joining a channel:

```xml
<oper name="Sadie"
      ...
      override="BANWALK INVITE KEY LIMIT">
```

Allows server operators of type NetAdmin to ignore any restrictions that might prevent them from joining a channel:

```xml
<type name="NetAdmin"
      ...
      override="BANWALK INVITE KEY LIMIT">
```

#### `<override>`

The `<override>` tag defines settings about how the override module should behave. This tag can only be defined once.

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
enableumode | Boolean | No            | Whether user mode `O` (override) needs to be enabled to override a restriction.
noisy       | Boolean | No            | Whether to inform the channel when a server operator overrides a restriction.
requirekey  | Boolean | No            | Whether overriding server operators should have to specify a channel key of `override` when joining a channel.

##### Example Usage

```xml
<override enableumode="yes"
          noisy="no"
          requirekey="no">
```

### User Modes

Name     | Character | Type   | Parameter Syntax | Usable By        | Description
-------- | --------- | ------ | ---------------- | ---------------- | -----------
override | O         | Switch | *None*           | Server operators | Allows server operators to opt-in to overriding restrictions.

### Server Notice Masks

Character | Description
--------- | -----------
v         | Notifications about server operators overriding channel-level restrictions on the local server.
V         | Notifications about server operators overriding channel-level restrictions on a remote server.
