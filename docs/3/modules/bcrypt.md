---
title: "Module Details: bcrypt (v3)"
---

## The "bcrypt" Module

### Description

This module allows other modules to generate [bcrypt](https://en.wikipedia.org/wiki/bcrypt) hashes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="bcrypt">
```

#### `<bcrypt>`

The `<bcrypt>` tag defines settings about how the bcrypt module should behave. This tag can only be defined once.

Name   | Type   | Default Value | Description
------ | ------ | ------------- | -----------
rounds | Number | 10            | The number of rounds of the bcrypt algorithm that should be used.

##### Example Usage

```xml
<bcrypt rounds="10">
```
