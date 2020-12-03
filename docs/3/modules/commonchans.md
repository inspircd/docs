---
title: "Module Details: commonchans (v3)"
---

## The "commonchans" Module

### Description

This module adds user mode `c` (deaf_commonchan) which requires users to have a common channel before they can privately message each other.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="commonchans">
```

#### `<class>`

This module extends the core `<class:privs>` key with the following values:

Name                     | Description
------------------------ | -----------
users/ignore-commonchans | Allows server operators to message a user with the `c` (deaf_commonchan) mode set without sharing a common channel.

##### Example Usage

Allows server operators with the class named BasicOper to message a user with the `c` (deaf_commonchan) mode set without sharing a common channel.

```xml
<class name="BasicOper"
       ...
       privs="... users/ignore-commonchans ...">
```

### User Modes

Name            | Character | Type   | Parameter Syntax | Usable By | Description
--------------- | --------- | ------ | ---------------- | --------- | -----------
deaf_commonchan | c         | Switch | *None*           | Anyone    | Requires other users to have a common channel before they can message this user.
