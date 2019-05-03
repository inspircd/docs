---
title: Module Details (userip)
---

## The "userip" Module

### Description

This module adds the `/USERIP` command which allows users to find out the IP address of one or more connected users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="userip">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax             | Description
------ | --------------- | ------------------ | -----------
USERIP | 1+              | `<nick> [<nick>]+` | Retrieves the IP address of the specified users.

#### Example Usage

Looks up the IP address of Sadie:

```plaintext
/USERIP Sadie
```

### Special Notes

The `users/auspex` server operator privilege is required to view the IP address of other users.
