---
title: "Module Details: repeat (v3)"
---

## The "repeat" Module

### Description

This module adds channel mode `E` (repeat) which helps protect against spammers which spam the same message repeatedly.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="repeat">
```

#### `<repeat>`

The `<repeat>` tag defines settings about how the repeat module should behave. This tag can only be defined once.

Name        | Type     | Default Value | Description
----------- | -------- | ------------- | -----------
maxbacklog  | Number   | 20            | The maximum size that can be specified for backlog. Set to 0 to disable multiline matching.
maxdistance | Number   | 50            | The maximum percentage of difference between two lines we'll allow to match. Set to 0 to disable edit-distance matching.
maxlines    | Number   | 20            | The maximum lines of backlog to match against.
maxtime     | Duration | 0             | The maximum period of time a user can set. Set to 0 to allow any period.
size        | Number   | 512           | The maximum number of characters to check for, can be used to truncate messages before they are checked, resulting in less CPU usage.

##### Example Usage

```xml
<repeat maxbacklog="20"
        maxdistance="50"
        maxlines="20"
        maxtime="1h"
        size="512">
```

### Channel Modes

Name   | Character | Type      | Parameter Syntax                                | Usable By         | Description
------ | --------- | --------- | ----------------------------------------------- | ----------------- | -----------
repeat | E         | Parameter | `[~|*]<lines>:<sec>[:<difference>][:<backlog>]` | Channel operators | Configures the messages that should be considered a repeat. If prefixed with ~ the messages are blocked. If prefixed with * then offending users are banned. If not prefixed then offending users are kicked.

#### Example Usage

Blocks more than two repeated messages in five seconds:

```plaintext
/MODE #channel +E 2:5
```

### Exemptions

Name   | Description
------ | -----------
repeat | Allows exempted users to send repetitive messages at a higher rate than channel mode `E` (repeat) allows.
