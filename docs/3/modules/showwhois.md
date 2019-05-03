---
title: Module Details (showwhois)
---

## The "showwhois" Module

### Description

This module adds user mode `W` (showwhois) which allows users to be informed when someone does a `/WHOIS` query on their nick.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="showwhois">
```

#### `<showwhois>`

The `<showwhois>` tag defines settings about how the showwhois module should behave. This tag can only be defined once.

Name          | Type    | Default Value  | Description
------------- | ------- | -------------- | -----------
opersonly     | Boolean | Yes            | Whether user mode `W` (showwhois) can only be used by server operators.
showfromopers | Boolean | Yes            | Whether to inform users of an oper doing a `/WHOIS` query on their nick.

##### Example Usage

```xml
<showwhois opersonly="no"
           showfromopers="no">
```

### User Modes

Name      | Character | Type   | Parameter Syntax | Description
--------- | --------- | ------ | ---------------- | -----------
showwhois | W         | Switch | *None*           | Informs the user when someone does a `/WHOIS` query on their nick.
