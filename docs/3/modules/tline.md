---
title: "Module Details: tline (v3)"
---

## The "tline" Module

### Description

This module adds the `/TLINE` command which allows server operators to determine how many users would be affected by an X-line on a specified pattern.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="tline">
```

This module requires no other configuration.

### Commands

Name  | Parameter Count | Syntax      | Description
----- | --------------- | ----------- | -----------
TLINE | 1               | `<pattern>` | Determines how many users would be affected by an X-line on &lt;pattern&gt;.

#### Example Usage

Determines how many users would be affected by an X-line on `*!*@example.com`:

```plaintext
/TLINE *!*@example.com
```
