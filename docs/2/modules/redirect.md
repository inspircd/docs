---
title: Module Details (redirect)
---

{! 2/_support.md !}

## The "redirect" Module

### Description

This module allows users to be redirected to another channel when the user limit is reached.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_redirect.so">
```

#### `<redirect>`

The `<redirect>` tag defines settings about how the redirect module should behave. This tag can only be defined once.

Name         | Type    | Default Value | Description
------------ | ------- | ------------- | -----------
antiredirect | Boolean | No            | Whether user mode `L` (antiredirect) is enabled.

##### Example Usage

```xml
<redirect antiredirect="yes">
```

### Channel Modes

Name     | Character | Type      | Parameter Syntax | Description
-------- | --------- | --------- | ---------------- | -----------
redirect | L         | Parameter | `<channel>`      | Redirects all new users to &lt;channel&gt; when the user limit is reached.

#### Example Usage

Redirects new users from #channel to #channel-full when the user limit is reached.

```plaintext
/MODE #channel +L #channel-full
```

### User Modes

Name         | Character | Type   | Parameter Syntax | Description
------------ | --------- | ------ | ---------------- | -----------
antiredirect | L         | Switch | *None*           | Prevents users from being redirected by channel mode `L` (redirect).

### Special Notes

When setting a redirect the target channel should exist and the user setting the redirect should have channel operator status in it.
