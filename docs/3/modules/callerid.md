---
title: "Module Details: callerid (v3)"
---

## The "callerid" Module

### Description

This module provides user mode `g` (bot) which allows users to require that other users are on their whitelist before messaging them.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="callerid">
```

#### `<callerid>`

The `<callerid>` tag defines settings about how the callerid module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
cooldown     | Number  | 10            | The number of seconds between notifying users of other users that want to message them.
maxaccepts   | Number  | 30            | The maximum number of users who can be on a user's callerid whitelist.
tracknick    | Boolean | No            | Whether to track nickname changes for users on a callerid whitelist.

##### Example Usage

```xml
<callerid cooldown="10"
          maxaccepts="30"
          tracknick="no">
```

#### `<class>`

This module extends the core `<class:privs>` key with the following values:

Name                  | Description
--------------------- | -----------
users/ignore-callerid | Allows server operators to message users using callerid without being on their callerid list.

##### Example Usage

Allows server operators with the class named BasicOper to message users using callerid without being on their callerid list.

```xml
<class name="BasicOper"
       ...
       privs="... users/ignore-callerid ...">
```

### Commands

Name    | Parameter Count | Syntax                                      | Description
------- | --------------- | ------------------------------------------- | -----------
ACCEPT  | 1               | `*`<br>`(+|-)<nickname>[,(+|-)<nickname>]+` | Allows users to add, remove, and view the users on their callerid whitelist.

#### Example Usage

Lists all users on your callerid whitelist:

```plaintext
/ACCEPT *
```

Adds Sadie to your callerid whitelist and removes Adam from your callerid whitelist:

```plaintext
/ACCEPT +Sadie,-Adam
```

### User Modes

Name     | Character | Type   | Parameter Syntax | Usable By | Description
-------- | --------- | ------ | ---------------- | --------- | -----------
callerid | g         | Switch | *None*           | Anyone    | Enables whitelisting of who can message the user.
