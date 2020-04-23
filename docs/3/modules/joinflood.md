---
title: "Module Details: joinflood (v3)"
---

## The "joinflood" Module

### Description

This module adds channel mode `j` (joinflood) which helps protect against spammers which mass-join channels.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="joinflood">
```

#### `<joinflood>`

The `<joinflood>` tag defines settings about how the joinflood module should behave. This tag can only be defined once.

Name     | Type     | Default Value | Description
-------- | -------- | ------------- | -----------
duration | Duration | 1m            | The time period that a channel should be locked for once a join flood has been detected.

##### Example Usage

```xml
<joinflood duration="60s">
```

### Channel Modes

Name      | Character | Type      | Parameter Syntax    | Usable By         | Description
--------- | --------- | --------- | ------------------- | ----------------- | -----------
joinflood | j         | Parameter | `<joins>:<seconds>` | Channel operators | Prevents more than &lt;joins&gt; joins in the last &lt;seconds&gt; seconds.

#### Example Usage

Prevents more than two joins in the last five seconds:

```plaintext
/MODE #channel +j 2:5
```
