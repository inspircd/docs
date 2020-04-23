---
title: Module Details: monitor (v3)
---

## The "monitor" Module

### Description

This module adds the `/MONITOR` command which allows users to find out when their friends are connected to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="monitor">
```

#### `<monitor>`

The `<monitor>` tag defines settings about how the monitor module should behave. This tag can only be defined once.

Name       | Type   | Default Value | Description
---------- | ------ | ------------- | -----------
maxentries | Number | 30            | The maximum number of entries on a user's monitor list.

##### Example Usage

```xml
<monitor maxentries="32">
```

### Commands

Name    | Parameter Count | Syntax                                        | Description
------- | --------------- | --------------------------------------------- | -----------
MONITOR | 1, 2            | `(+|-) <nick>,[<nick>]+`<br>`C`<br>`L`<br>`S` | Manipulates the contents of the executing user's monitor list.

#### Example Usage

Adds Sadie to the monitor list:

```plaintext
/MONITOR + Sadie
```

Removes Sadie from the monitor list:

```plaintext
/MONITOR - Sadie
```

Removes all users from the monitor list:

```plaintext
/MONITOR C
```

Lists all users on the monitor list:

```plaintext
/MONITOR L
```

Shows the status of all monitored users:

```plaintext
/MONITOR S
```
