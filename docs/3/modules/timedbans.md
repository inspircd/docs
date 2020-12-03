---
title: "Module Details: timedbans (v3)"
---

## The "timedbans" Module

### Description

This module adds the `/TBAN` command which allows channel operators to add bans which will be expired after the specified period.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="timedbans">
```

#### `<timedbans>`

The `<timedbans>` tag defines settings about how the timedbans module should behave. This tag can only be defined once.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
sendnotice | Boolean | Yes           | [**New in v3.7.0!**](/3/change-log/#inspircd-370) Whether to send a notice to channel operators when a timed ban is added or expired.

##### Example Usage

```xml
<timedbans sendnotice="yes">
```

### Commands

Name | Parameter Count | Syntax                           | Description
---- | --------------- | -------------------------------- | -----------
TBAN | 3               | `<channel> <duration> <banmask>` | Bans &lt;banmask&lt; from &lt;channel&gt; for &lt;duration&gt;.

#### Example Usage

Bans `*!*@example.com` from #channel for one hour:

```plaintext
/TBAN #channel 1h *!*@example.com
```
