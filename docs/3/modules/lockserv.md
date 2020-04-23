---
title: "Module Details: lockserv (v3)"
---

## The "lockserv" Module

### Description

This module adds the `/LOCKSERV` and `/UNLOCKSERV` commands which allows server operators to control whether users can connect to the local server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="lockserv">
```

This module requires no other configuration.

### Commands

Name       | Parameter Count | Syntax        | Description
---------- | --------------- | ------------- | -----------
LOCKSERV   | 0-1             | `[<message>]` | Disables access to the local server with an optional message.
UNLOCKSERV | 0               | *None*        | Enables access to the local server.

#### Example Usage

Stops the local server from accepting new connections with the message "Server is under maintenance. Come back later.":

```plaintext
/LOCKSERV :Server is under maintenance. Come back later.
```

Opens up the local server so it accepts new connections:

```plaintext
/UNLOCKSERV
```

## Special Notes

If you accidentally disconnect whilst a server is locked you can disable the lock by rehashing the server.
