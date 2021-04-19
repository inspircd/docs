---
title: "Module Details: muteban (v3)"
---

## The "muteban" Module

### Description

This module adds extended ban `m:` which bans specific masks from speaking in a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="muteban">
```

#### `<muteban>`

The `<muteban>` tag defines settings about how the muteban module should behave. This tag can only be defined once.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
notifyuser | Boolean | Yes           | Whether to notify users who try to message a channel whilst mutebanned.

##### Example Usage

```xml
<muteban notifyuser="yes">
```

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
m         | Acting | `m:<mask>` | Bans &lt;mask&gt; from speaking in the channel.
