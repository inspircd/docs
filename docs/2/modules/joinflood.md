---
title: "Module Details: joinflood (v2)"
---

{! 2/_support.md !}

## The "joinflood" Module

### Description

This module adds channel mode `j` (joinflood) which helps protect against spammers which mass-join channels.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_joinflood.so">
```

This module requires no other configuration.

### Channel Modes

Name      | Character | Type      | Parameter Syntax    | Description
--------- | --------- | --------- | ------------------- | -----------
joinflood | j         | Parameter | `<joins>:<seconds>` | Prevents more than &lt;joins&gt; joins in the last &lt;seconds&gt; seconds.

#### Example Usage

Prevents more than two joins in the last five seconds:

```plaintext
/MODE #channel +j 2:5
```
