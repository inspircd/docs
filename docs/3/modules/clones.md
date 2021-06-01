---
title: "Module Details: clones (v3)"
---

## The "clones" Module

!!! warning ""
    This module has been moved to [inspircd-contrib](/3/module-manager) in the next major version of InspIRCd.

### Description

This module adds the `/CLONES` command which allows server operators to view IP addresses from which there are more than a specified number of connections.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="clones">
```

This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax    | Description
------ | --------------- | --------- | -----------
CLONES | 1               | `<limit>` | Lists all IP addresses from which there are more than &lt;limit&gt; connections.

#### Example Usage

Lists IP addresses from which there are more than five connections:

```plaintext
/CLONES 5
```
