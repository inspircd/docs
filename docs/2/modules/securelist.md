---
title: Module Details: securelist (v2)
---

{! 2/_support.md !}

## The "securelist" Module

### Description

This module prevents users from using the `/LIST` command until a predefined period has passed.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_securelist.so">
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

Name     | Type   | Default Value | Description
-------- | ------ | ------------- | -----------
waittime | Number | 60            | The number of seconds that must pass before a user can use the `/LIST` command.

#### Example Usage

```xml
<securelist waittime="60">
```
