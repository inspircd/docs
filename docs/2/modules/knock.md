---
title: Module Details (knock)
---

{! 2/_support.md !}

## The "knock" Module

### Description

This module adds the `/KNOCK` command which allows users to request access to an invite-only channel and channel mode `K` (noknock) which allows channels to disable usage of this command.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_knock.so">
```

#### `<knock>`

The `<knock>` tag defines settings about how the knock module should behave. This tag can only be defined once.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
notify | Text | notice        | How to notify channel members that a user would like to join the channel.

The notify field should be set to one of the following values:

Value   | Description
------- | -----------
both    | Send both numeric `710` (RPL_KNOCK) and a `NOTICE` when a user requests access to an invite-only channel.
notice  | Send a `NOTICE` when a user requests access to an invite-only channel.
numeric | Send numeric `710` (RPL_KNOCK) when a user requests access to an invite-only channel.

##### Example Usage

```xml
<knock notify="notice">
```

### Commands

Name  | Parameter Count | Syntax               | Description
----- | --------------- | -------------------- | -----------
KNOCK | 2               | `<channel> <reason>` | Requests permission to join &lt;channel&gt; with the reason specified in &lt;reason&gt;.

#### Example Usage

Knocks on #channel with the reason "Please let me in!":

```plaintext
/KNOCK #channel :Please let me in!
```

### Channel Modes

Name    | Character | Type   | Parameter Syntax | Description
------- | --------- | ------ | ---------------- | -----------
noknock | K         | Switch | *None*           | Disables the usage of the `/KNOCK` command on this channel.
