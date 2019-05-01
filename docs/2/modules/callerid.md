---
title: Module Details (callerid)
---

## The "callerid" Module

### Description

This module provides user mode `g` (bot) which allows users to require that other users are on their whitelist before messaging them.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_callerid.so">
```

#### `<callerid>`

The `<callerid>` tag defines settings about how the callerid module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
cooldown     | Number  | 10            | The number of seconds between notifying users of other users that want to message them.
maxaccepts   | Number  | 16            | The maximum number of users who can be on a user's callerid whitelist.
operoverride | Boolean | No            | Whether server operators can message users without being on an callerid whitelist.
tracknick    | Boolean | No            | Whether to track nickname changes for users on a callerid whitelist.

##### Example Usage

```xml
<callerid cooldown="10"
          maxaccepts="16"
          operoverride="no"
          tracknick="no">
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

Name     | Character | Type   | Parameter Syntax | Description
-------- | --------- | ------ | ---------------- | -----------
callerid | g         | Switch | *None*           | Enables whitelisting of who can message the user.
