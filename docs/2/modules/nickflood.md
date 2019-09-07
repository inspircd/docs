---
title: Module Details (nickflood)
---

{! 2/_support.md !}

## The "nickflood" Module

### Description

This module adds channel mode `F` (nickflood) which helps protect against spammers which mass-change nicknames.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_nickflood.so">
```

This module requires no other configuration.

### Channel Modes

Name      | Character | Type      | Parameter Syntax      | Description
--------- | --------- | --------- | --------------------- | -----------
nickflood | F         | Parameter | `<changes>:<seconds>` | Prevents more than &lt;changes&gt; nickname changes in the last &lt;seconds&gt; seconds.

#### Example Usage

Prevents more than three nickname changes in the last five seconds:

```plaintext
/MODE #channel +F 3:5
```

### Exemptions

Name  | Description
----- | -----------
flood | Allows exempted users to change nicknames at a higher rate than channel mode `F` (nickflood) allows.
