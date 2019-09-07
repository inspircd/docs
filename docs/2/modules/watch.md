---
title: Module Details (watch)
---

{! 2/_support.md !}

## The "watch" Module

### Description

This module adds the `/WATCH` command which allows users to find out when their friends are connected to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_watch.so">
```

#### `<watch>`

The `<watch>` tag defines settings about how the watch module should behave. This tag can only be defined once.

Name       | Type   | Default Value | Description
---------- | ------ | ------------- | -----------
maxentries | Number | 32            | The maximum number of entries on a user's watch list.

##### Example Usage

```xml
<watch maxentries="32">
```

### Commands

Name  | Parameter Count | Syntax                               | Description
----- | --------------- | ------------------------------------ | -----------
WATCH | 1               | `[(+|-)<nick>]`<br>`C`<br>`L`<br>`S` | Manipulates the contents of the executing user's watch list.

#### Example Usage

Adds Sadie to the watch list:

```plaintext
/WATCH +Sadie
```

Removes Sadie from the watch list:

```plaintext
/WATCH -Sadie
```

Removes all users from the watch list:

```plaintext
/WATCH C
```

Lists all users on the watch list:

```plaintext
/WATCH C
```

Shows the status of all watched users:

```plaintext
/WATCH S
```