---
title: Module Details: hidelist (v3)
---

## The "hidelist" Module

### Description

This module allows list mode lists to be hidden from users without a prefix mode ranked equal to or higher than a defined level.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="hidelist">
```

#### `<hidelist>`

The `<hidelist>` tag defines settings about how the hidelist module should behave. This tag can be defined as many times as required.

Name | Type   | Default Value | Description
---- | ------ | ------------- | -----------
mode | Text   | *None*        | The name of the mode this rule applies to.
rank | Number | 0             | The rank to restrict viewing this list mode list to.

##### Example Usage

Hides channel mode `g` (filter) from non-channel operators:

```xml
<hidelist mode="filter"
          rank="30000">
```

Hides channel mode `I` (invex) from non-channel members:

```xml
<hidelist mode="invex"
          rank="0">
```

### Special Notes

The ranks of the built-in channel prefix modes are:

- op (+o) &mdash; 30000

- voice (+v) &mdash; 10000
