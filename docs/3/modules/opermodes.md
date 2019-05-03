---
title: Module Details (opermodes)
---

## The "opermodes" Module

### Description

This module allows the server administrator to set user modes on server operators when they log into their server operator account.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="opermodes">
```

#### `<oper>` &amp; `<type>`

This module extends the core `<oper>` and `<type>` tags with the following fields:

Name  | Type | Default Value | Description
----- | ---- | ------------- | -----------
modes | Text | *None*        | The user modes to set on server operators when they log into their server operator account.

##### Example Usage

Forces Sadie to to have user modes `sw` (snomask, wallops) when logging into their server operator account:

```xml
<oper name="Sadie"
      ...
      modes="+sw *">
```

Forces server operators of type NetAdmin to to have user modes `sw` (snomask, wallops) when logging into their server operator account:

```xml
<type name="NetAdmin"
      ...
      modes="+sw *">
```
