---
title: Module Details (channames)
---

## The "channames" Module

### Description

This module allows the server administrator to define what characters are allowed in channel names.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="channames">
```

#### `<channames>`

The `<channames>` tag defines settings about how the channames module should behave. This tag can only be defined once.

Name       | Type      | Default Value | Description
---------- | --------- | ------------- | -----------
allowrange | No. Range | *None*        | The character ranges to allow in a channel name. This overrides denyrange if they overlap.
denyrange  | No. Range | *None*        | The character ranges to disallow in a channel name.

##### Example Usage

Bans characters other than letters, numbers, `#`, `-`, and `.`.

```xml
<channames allowrange="35,45-46"
           denyrange="1-47,58-64,91-96,123-255">
```

### Special Notes

The following characters have special meaning in the IRC protocol and will never be allowed in a channel name:

- 0x07 (bell)	
- 0x20 (space)
- 0x2C (comma)
