---
title: Module Details: chghost (v3)
---

## The "chghost" Module

### Description

This module adds the `/CHGHOST` command which allows server operators to change the displayed hostname of a user.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="chghost">
```

#### `<hostname>`

The `<hostname>` tag defines settings about how the chghost module should behave. This tag can only be defined once.

Name    | Type | Default Value                                                      | Description
------- | ---- | ------------------------------------------------------------------ | -----------
charmap | Text | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.-_/0123456789 | The characters which are allowed in a hostname.

##### Example Usage

Allows hostnames to contain letters, numbers, `/`, `-`, `.', and `__`.

```xml
<hostname charmap="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.-_/0123456789">
```

### Commands

Name    | Parameter Count | Syntax                  | Description
------- | --------------- | ----------------------- | -----------
CHGHOST | 2               | `<nickname> <hostname>` | Changes the displayed hostname of &lt;nickname&gt; to &lt;hostname&gt;.

#### Example Usage

Changes the hostname of Sadie to wibble.wobble:

```plaintext
/CHGHOST Sadie wibble.wobble
```

### Special Notes

This command only changes the displayed hostname of a user. Their real hostname will remain intact and still will match against bans.
