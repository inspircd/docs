---
title: Module Details (hidemode)
---

## The "hidemode" Module

### Description

This module allows mode changes to be hidden from users without a prefix mode ranked equal to or higher than a defined level.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="hidemode">
```

#### `<hidemode>`

The `<hidemode>` tag defines settings about how the hidemode module should behave. This tag can only be defined once.

Name | Type   | Default Value | Description
---- | ------ | ------------- | -----------
mode | Text   | *None*        | The name of the mode this rule applies to.
rank | Number | 0             | The rank to restrict viewing this mode change to.

##### Example Usage

Hides channel mode `b` (ban) changes from non-voiced users:

```xml
<hidemode mode="ban"
          rank="10000">
```

### Special Notes

The ranks of the built-in channel prefix modes are:

- op (+o) &mdash; 30000

- voice (+v) &mdash; 10000
