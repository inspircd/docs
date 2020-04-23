---
title: Module Details: passforward (v2)
---

{! 2/_support.md !}

## The "passforward" Module

### Description

This module allows the `/PASS` password to be forwarded to a services pseudoclient such as NickServ.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_passforward.so">
```

#### `<passforward>`

The `<passforward>` tag defines settings about how the passforward module should behave. This tag can only be defined once.

Name       | Type | Default Value                                      | Description
---------- | ---- | -------------------------------------------------- | -----------
cmd        | Text | PRIVMSG $nickrequired :IDENTIFY $pass              | The command to use when forwarding the `/PASS` password.
forwardmsg | Text | NOTICE $nick :*** Forwarding PASS to $nickrequired | The command to use when informing the connecting user that their `/PASS` password is being forwarded.
nick       | Text | NickServ                                           | The nickname of the user that must be online for a `/PASS` password to be forwarded.

The cmd and forwardmsg fields can contain any of the following template variables:

Variable      | Description
------------- | -----------
$nick         | The nickname of the connecting user.
$nickrequired | The nickname of the user that must be online for a `/PASS` password to be forwarded.
$pass         | The password sent by the connecting user using the `/PASS` command.
$user         | The username (ident) of the connecting user.

##### Example Usage

```xml
<passforward cmd="PRIVMSG $nickrequired :IDENTIFY $pass"
             forwardmsg="NOTICE $nick :*** Forwarding PASS to $nickrequired"
             nick="NickServ">
```
