---
title: Module Details: sethost (v2)
---

{! 2/_support.md !}

## The "sethost" Module

### Description

This module adds the `/SETHOST` command which allows server operators to change their displayed hostname.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_sethost.so">
```

#### `<hostname>`

The `<hostname>` tag defines settings about how the sethost module should behave. This tag can only be defined once.

Name    | Type | Default Value                                                      | Description
------- | ---- | ------------------------------------------------------------------ | -----------
charmap | Text | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.-_/0123456789 | The characters which are allowed in a hostname.

##### Example Usage

Allows hostnames to contain letters, numbers, `/`, `-`, `.', and `__`.

```xml
<hostname charmap="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.-_/0123456789">
```

### Commands

Name    | Parameter Count | Syntax       | Description
------- | --------------- | ------------ | -----------
SETHOST | 1               | `<hostname>` | Changes the displayed hostname of the user to &lt;hostname&gt;.

#### Example Usage

Changes the hostname of the user to wibble.wobble:

```plaintext
/SETHOST wibble.wobble
```

### Special Notes

This command only changes the displayed hostname of the user. Their real hostname will remain intact and still will match against bans.
