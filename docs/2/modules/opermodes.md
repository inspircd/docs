---
title: Module Details (opermodes)
---

{! 2/_support.md !}

## The "opermodes" Module

### Description

This module allows the server administrator to set user modes on server operators when they log into their server operator account.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_opermodes.so">
```

#### `<oper>` &amp; `<type>`

This module extends the core `<oper>` and `<type>` tags with the following fields:

Name  | Type | Default Value | Description
----- | ---- | ------------- | -----------
modes | Text | *None*        | The user modes to set on server operators when they log into their server operator account.

##### Example Usage

Forces Sadie to have user modes `sw` (snomask, wallops) and all available snomasks when logging into their server operator account:

```xml
<oper name="Sadie"
      ...
      modes="+sw +*">
```

Forces server operators of type NetAdmin to have user modes `sw` (snomask, wallops) and all available snomasks when logging into their server operator account:

```xml
<type name="NetAdmin"
      ...
      modes="+sw +*">
```
