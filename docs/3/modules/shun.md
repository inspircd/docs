---
title: "Module Details: shun (v3)"
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

Name            | Type    | Default Value                                                            | Description
--------------- | ------- | ------------------------------------------------------------------------ | -----------
affectopers     | Boolean | No                                                                       | Whether server operators are affected by shuns.
allowconnect    | Boolean | No                                                                       | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Whether to only apply shuns to users who have fully connected to the server.
allowtags       | Boolean | No                                                                       | [**New in v3.8.0!**](/3/change-log/#inspircd-380) Whether shunned users can send message tags on allowed commands.
cleanedcommands | Text    | AWAY PART QUIT                                                           | [**New in v3.8.0!**](/3/change-log/#inspircd-380) The commands to remove any messages from if allowed.
enabledcommands | Text    | ADMIN OPER PING PONG QUIT *(since 3.6)*<br>PING PONG QUIT *(3.0 to 3.5)* | A space-delimited list of commands that a shunned user is allowed to run.
notifyuser      | Boolean | Yes                                                                      | Whether to notify shunned users that they are blocked from executing commands.

#### Example Usage

```xml
<shun affectopers="no"
      allowconnect="yes"
      allowtags="no"
      cleanedcommands="AWAY PART QUIT"
      enabledcommands="ADMIN PING PONG QUIT"
      notifyuser="yes">
```

#### `<class>`

This module extends the core `<class:privs>` key with the following values:

Name                 | Description
-------------------- | -----------
servers/ignore-shuns | [**New in v3.6.0!**](/3/change-log/#inspircd-360) Allows server operators to ignore shuns.

#### Example Usage

Allows server operators with the class named BasicOper to ignore shuns.

```xml
<class name="BasicOper"
       ...
       privs="... servers/ignore-shun ...">
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
