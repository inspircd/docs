---
title: "Module Details: operjoin (v2)"
---

{! 2/_support.md !}

## The "operjoin" Module

### Description

This module allows the server administrator to force server operators to join one or more channels when logging into their server operator account.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_operjoin.so">
```

#### `<oper>` &amp; `<type>`

This module extends the core `<oper>` and `<type>` tags with the following fields:

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
autojoin | Text | *None*        | A comma-delimited list of channels for server operators to be joined to when logging into their server operator account.

##### Example Usage

Forces Sadie to join #example1 and #example2 when logging into their server operator account:

```xml
<oper name="Sadie"
      ...
      autojoin="#example1,#example2">
```

Forces server operators of type NetAdmin to join #example1 and #example2 when logging into their server operator account:

```xml
<type name="NetAdmin"
      ...
      autojoin="#example1,#example2">
```

#### `<operjoin>`

The `<operjoin>` tag defines settings about how the operjoin module should behave. This tag can only be defined once.

Name     | Type    | Default Value | Description
-------- | ------- | ------------- | -----------
channel  | Text    | *None*        | A comma-delimited list of channels for server operators to be joined to when logging into their server operator account.
override | Boolean | No            | Whether to force server operators into the channel regardless of any channel modes that might normally prevent them from joining.

##### Example Usage

Forces all server operators to join #example when logging into their server operator account:

```xml
<operjoin channel="#example"
          override="yes">
```
