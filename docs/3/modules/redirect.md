---
title: "Module Details: redirect (v3)"
---

## The "redirect" Module

### Description

This module allows users to be redirected to another channel when the user limit is reached.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="redirect">
```

### Channel Modes

Name     | Character | Type      | Parameter Syntax | Usable By         | Description
-------- | --------- | --------- | ---------------- | ----------------- | -----------
redirect | L         | Parameter | `<channel>`      | Channel operators | Redirects all new users to &lt;channel&gt; when the user limit is reached.

#### Example Usage

Redirects new users from #channel to #channel-full when the user limit is reached.

```plaintext
/MODE #channel +L #channel-full
```

### User Modes

Name         | Character | Type   | Parameter Syntax | Usable By | Description
------------ | --------- | ------ | ---------------- | --------- | -----------
antiredirect | L         | Switch | *None*           | Anyone    | Prevents users from being redirected by channel mode `L` (redirect).

### Special Notes

When setting a redirect the target channel should exist and the user setting the redirect should have channel operator status in it.
