---
title: "Module Details: securelist (v3)"
---

## The "securelist" Module

### Description

This module prevents users from using the `/LIST` command until a predefined period has passed.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="securelist">
```

#### `<securehost>`

The `<securehost>` tag defines an exception to the `/LIST` waiting period. This tag can be defined as many times as required.

Name      | Type | Default Value | Description
--------- | ---- | ------------- | -----------
exception | Text | *None*        | **Required!** A glob pattern to match against the hostnames of users that run the `/LIST` command.

##### Example Usage

Adds an exception for the [irc.netsplit.de](http://irc.netsplit.de) crawler:

```xml
<securehost exception="*@*.netsplit.de">
```

#### `<securelist>`

The `<securelist>` tag defines settings about how the securelist module should behave. This tag can only be defined once.

Name             | Type     | Default Value | Description
---------------- | -------- | ------------- | -----------
exemptregistered | Boolean  | No            | Whether registered users are exempt from waiting.
showmsg          | Boolan   | No            | Whether to tell the user that they need to wait before using the `/LIST` comand.
waittime         | Duration | 1m            | The time period that must pass before a user can use the `/LIST` command.

#### Example Usage

```xml
<securelist exemptregistered="yes"
            showmsg="yes"
            waittime="60s">
```
