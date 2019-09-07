---
title: Module Details (operlog)
---

{! 2/_support.md !}

## The "operlog" Module

### Description

This module allows the server administrator to make the server log when a server operator-only command is executed.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_operlog.so">
```

#### `<operlog>`

The `<operlog>` tag defines settings about how the operlog module should behave. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
tosnomask | Boolean | No            | Whether to log to snomask `r` (local) and snomask `R` (remote) as well as writing to the server log.

##### Example Usage

```xml
<operlog tosnomask="yes">
```

### Server Notice Masks

Character | Description
--------- | -----------
r         | Notifications about server operator-only commands being executed on the local server.
R         | Notifications about server operator-only commands being executed on a remote server.
