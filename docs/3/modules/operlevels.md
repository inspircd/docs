---
title: Module Details (operlevels)
---

## The "operlevels" Module

### Description

This module allows the server administrator to define ranks for server operators which prevent lower ranked server operators from using `/KILL` on higher ranked server operators.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="operlevels">
```

#### `<oper>` &amp; `<type>`

This module extends the core `<oper>` and `<type>` tags with the following fields:

Name  | Type   | Default Value | Description
----- | ------ | ------------- | -----------
level | Number | 0             | The rank to give to the server operators.

##### Example Usage

Creates two server operators, Sadie and Adam, where the former will be able to `/KILL` the latter but the latter will not be able to kill the former:

```xml
<oper name="Sadie"
      ...
      level="100">

<oper name="Adam"
      ...
      level="50">
```

Creates two server operator types, NetAdmin and Helper, where the former will be able to `/KILL` the latter but the latter will not be able to kill the former:

```xml
<type name="NetAdmin"
      ...
      level="100">

<type name="Helper"
      ...
      level="50">
```
