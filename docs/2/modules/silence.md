---
title: "Module Details: silence (v2)"
---

{! 2/_support.md !}

## The "silence" Module

### Description

This module adds the `/SILENCE` command which allows users to ignore other users on server-side.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_silence.so">
```

#### `<silence>`

The `<silence>` tag defines settings about how the silence module should behave. This tag can only be defined once.

Name       | Type   | Default Value  | Description
---------- | ------ | -------------- | -----------
maxentries | Number | 32             | The maximum number of entries that can be on a `/SILENCE` list.

#### Example Usage

```xml
<silence maxentries="32">
```

### Commands

Name    | Parameter Count | Syntax                    | Description
------- | --------------- | ------------------------- | -----------
SILENCE | 1-2             | `[(+|-)<mask> [<flags>]]` | Allows users to add users to their `/SILENCE` list, remove users from their `/SILENCE` list, and list users on their `/SILENCE` list.

The flags in the second parameter should be set to one of the following values:

Flag | Description
---- | -----------
`*`  | Enables the `cinpt` flags.
`a`  | Enables the `cinpt` flags.
`c`  | Applies to channel `PRIVMSG` messages.
`i`  | Applies to invites.
`n`  | Applies to private `NOTICE` messages
`p`  | Applies to private `PRIVMSG` messages.
`t`  | Applies to channel `NOTICE` messages.
`x`  | The entry is an exception.

#### Example Usage

Adds a `/SILENCE` entry which blocks all possible messages from users matching `*!*@example.com`:

```plaintext
/SILENCE *!*@example.com *
```

Removes a `/SILENCE` entry which blocked private `NOTICE` and `PRIVMSG` messages from users matching `*!*@example.com`:

```plaintext
/SILENCE *!*@example.com
```

View all entries on the `/SILENCE` list:

```plaintext
/SILENCE
```
