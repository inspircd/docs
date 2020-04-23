---
title: Module Details: nickflood (v3)
---

## The "nickflood" Module

### Description

This module adds channel mode `F` (nickflood) which helps protect against spammers which mass-change nicknames.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="nickflood">
```

#### `<nickflood>`

The `<nickflood>` tag defines settings about how the nickflood module should behave. This tag can only be defined once.

Name     | Type     | Default Value | Description
-------- | -------- | ------------- | -----------
duration | Duration | 1m            | The time period that nick changes should be locked for once a nick flood has been detected.

##### Example Usage

```xml
<nickflood duration="60s">
```

### Channel Modes

Name      | Character | Type      | Parameter Syntax      | Usable By         | Description
--------- | --------- | --------- | --------------------- | ----------------- | -----------
nickflood | F         | Parameter | `<changes>:<seconds>` | Channel operators | Prevents more than &lt;changes&gt; nickname changes in the last &lt;seconds&gt; seconds.

#### Example Usage

Prevents more than three nickname changes in the last five seconds:

```plaintext
/MODE #channel +F 3:5
```

### Exemptions

Name  | Description
----- | -----------
flood | Allows exempted users to change nicknames at a higher rate than channel mode `F` (nickflood) allows.
