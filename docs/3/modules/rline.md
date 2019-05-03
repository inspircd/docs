---
title: Module Details (rline)
---

## The "rline" Module

### Description

This module adds the `/RLINE` command which allows server operators to prevent users matching a nickname!username@hostname+realname regular expression from connecting to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="rline">
```

#### `<rline>`

The `<rline>` tag defines settings about how the rline module should behave. This tag can only be defined once.

Name              | Type    | Default Value | Description
----------------- | ------- | ------------- | -----------
engine            | Text    | *None*        | The regular expression engine to use for checking matches.
matchonnickchange | Boolean | No            | Whether to attempt to match users when they change their nickname.
zlineonmatch      | Boolean | No            | Whether to add a Z-line on the IP address of users that match a R-line.

The engine field should be set to the name of a regular expression engine.

{! 3/modules/_regex_table.md !}

#### Example Usage

```xml
<rline engine="pcre"
       matchonnickchange="no"
       zlineonmatch="no">
```

### Commands

Name  | Parameter Count | Syntax                            | Description
----- | --------------- | --------------------------------- | -----------
RLINE | 1-3             | `<regex> [<duration> [<reason>]]` | Allows server operators to add and remove regular expression bans on nickname!username@hostname+realname masks.

#### Example Usage

<div class="alert alert-info" role="alert" markdown="1">
The following examples assume that the "pcre" regex module is being used. See the `<rline>` documentation above for more information.
</div>

Bans users connecting from example.com for one week:

```plaintext
/RLINE ^[^!]+![^@]+@example.com\+.+$ 7d :Trolling is forbidden
```

Bans users that have "BotBot" in their real name forever:

```plaintext
/RLINE ^[^!]+![^@]+@[^\+]+\+.*BotBot.*$ 0 :No bots allowed
```

Unbans users connecting from example.com:

```plaintext
/RLINE ^[^!]+![^@]+@example.com\+.+$
```

### Statistics

Character | Description
--------- | -----------
R         | Lists all regular expression lines.

### Special Notes

R-lines are expired lazily when a lookup happens for performance reasons. This means that expiry messages may display later than expected.
