---
title: Module Details (auditorium)
---

## The "auditorium" Module

### Description

This module adds channel mode `u` (auditorium) which hides unprivileged users in a channel from each other. This is done by suppressing joins, parts, quits, kicks, `/NAMES` responses, and `/WHO` responses for unprivileged users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="auditorium">
```

#### `<auditorium>`

The `<auditorium>` tag defines settings about how the auditorium module should behave. This tag can only be defined once.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
opcansee   | Boolean | No            | Whether channel operators can see other channel members.
opvisible  | Boolean | No            | Whether channel operators can be seen by other channel members.
opercansee | Boolean | Yes           | Whether server operators with the channels/auspex privilege can see other channel members.

##### Example Usage

```xml
<auditorium opcansee="no"
            opvisible="no"
            opercansee="yes">
```

### Channel Modes

Name       | Character | Type   | Parameter Syntax | Description
---------- | --------- | ------ | ---------------- | -----------
auditorium | u         | Switch | *None*           | Enables auditorium mode.

### Exemptions

Name           | Description
-------------- | -----------
auditorium-see | Allows exempted users to see other channel members.
auditorium-vis | Allows exempted users to be seen by other channel members.
