---
title: "Module Details: cban (v3)"
---

## The "cban" Module

### Description

This module adds the `/CBAN` command which allows server operators to prevent channels matching a glob from being created.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="cban">
```

#### `<cban>`

The `<cban>` tag defines settings about how the cban module should behave. This tag can only be defined once.

Name | Type    | Default Value | Description
---- | ------- | ------------- | -----------
glob | Boolean | No            | [**New in v3.8.0!**](/3/change-log/#inspircd-380) Whether to use glob matching instead of case-insensitive string matching.

##### Example Usage

```xml
<cban glob="yes">
```

### Commands

Name | Parameter Count | Syntax                              | Description
---- | --------------- | ----------------------------------- | -----------
CBAN | 1-3             | `<channel> [<duration> [<reason>]]` | Allows server operators to add and remove channel bans.

#### Example Usage

Bans the #example channel for one week:

```plaintext
/CBAN #example 7d :This channel is banned for a week
```

Bans channels that match the glob #example* forever:

```plaintext
/CBAN #example* 0 :This channel is banned forever
```

Unbans the #example channel:

```plaintext
/CBAN #example
```

### Statistics

Character | Description
--------- | -----------
C         | Lists all channel bans.

### Special Notes

CBANs are expired lazily when a lookup happens for performance reasons. This means that expiry messages may display later than expected.
