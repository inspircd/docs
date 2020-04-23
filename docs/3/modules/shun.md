---
title: Module Details: shun (v3)
---

## The "shun" Module

### Description

This module adds the `/SHUN` command which allows server operators to prevent users from executing commands.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="shun">
```

#### `<shun>`

The `<shun>` tag defines settings about how the shun module should behave. This tag can only be defined once.

Name            | Type    | Default Value  | Description
--------------- | ------- | -------------- | -----------
affectsopers    | Boolean | No             | Whether server operators are affected by shuns.
enabledcommands | Text    | PING PONG QUIT | A space-delimited list of commands that a shunned user is allowed to run.
notifyuser      | Boolean | Yes            | Whether to notify shunned users that they are blocked from executing commands.

#### Example Usage

```xml
<shun affectsopers="no"
      enabledcommands="ADMIN PING PONG QUIT"
      notifyuser="yes">
```

### Commands

Name | Parameter Count | Syntax                              | Description
---- | --------------- | ----------------------------------- | -----------
SHUN | 1-3             | `<pattern>[ [<duration>] <reason>]` | Allows server operators to add and remove shuns on nickname!username@hostname glob patterns.

#### Example Usage

Shuns users connecting from example.com for one week:

```plaintext
/SHUN *!*@example.com 7d :Trolling is forbidden
```

Shuns users connecting from example.com forever:

```plaintext
/SHUN *!*@example.com :Trolling is forbidden
```

Removes a shun on users connecting from example.com:

```plaintext
/SHUN *!*@example.com
```

### Statistics

Character | Description
--------- | -----------
H         | Lists all shuns.

### Special Notes

Shuns are expired lazily when a lookup happens for performance reasons. This means that expiry messages may display later than expected.
