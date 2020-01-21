---
title: Module Details (jumpserver)
---

{! 2/_support.md !}

## The "jumpserver" Module

!!! warning ""
   This module has been moved to [inspircd-contrib](/2/module-manager) in the next major version of InspIRCd.

### Description

This module allows server operators to redirect users to a different server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_jumpserver.so">
```

This module requires no other configuration.

### Commands

Name       | Parameter Count | Syntax                                 | Description
---------- | --------------- | -------------------------------------- | -----------
JUMPSERVER | 0, 3-4          | `[<server> <port> <flags> [<reason>]]` | Toggles redirecting users to a new server.

The flags in the third parameter should be set to one of the following values:

Flag | Description
---- | -----------
`+`  | Any flags after the current one should be added.
`-`  | Any flags after the current one should be removed.
`a`  | Redirect all currently connected clients to the specified server.
`n`  | Redirect all newly connected clients to the specified server.

#### Example Usage

Disables redirecting clients to a new server:

```plaintext
/JUMPSERVER
```

Redirect all currently connected users to irc.example.com:+6697:

```plaintext
/JUMPSERVER irc.example.com +6697 +a :This server is being taken offline for updates.
```

Redirect all newly connected users to irc.example.com:+6697:

```plaintext
/JUMPSERVER irc.example.com +6697 +n :This server is offline for updates.
```

### Special Notes

Many clients do not support the `010` (RPL_REDIR) numeric used by this module. Users of these clients will be disconnected and will have to reconnect to the new server manually.

If you accidentally disconnect whilst a server is configured to redirect new clients you can disable the redirection by rehashing the server.
