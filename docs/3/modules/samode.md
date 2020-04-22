---
title: "Module Details: samode (v3)"
---

## The "samode" Module

### Description

This module adds the `/SAMODE` command which allows server operators to change the modes of a target (channel, user) that they would not otherwise have the privileges to change.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="samode">
```

#### `<class>`

This module extends the core `<class:privs>` key with the following values:

Name                   | Description
---------------------- | -----------
users/samode-usermodes | Allows server operators to change the user modes of any other user using `/SAMODE`.

#### Example Usage

Allows server operators with the class named SACommands to `/SAMODE` the user modes of other users.

```xml
<class name="SACommands"
       ...
       commands="... SAMODE ..."
       privs="... users/samode-usermodes ...">
```

### Commands

Name   | Parameter Count | Syntax                                  | Description
------ | --------------- | --------------------------------------- | -----------
SAMODE | 2+              | `<target> <modes> [<mode-parameters>]+` | Changes the modes of &lt;target&gt; to &lt;modes&gt; [&lt;mode-parameters&gt;]+

#### Example Usage

Removes channel mode `s` (secret) from #channel:

```plaintext
/SAMODE #channel -s
```

Adds user mode `w` (wallops) to Sadie:

```plaintext
/SAMODE Sadie +w
```
