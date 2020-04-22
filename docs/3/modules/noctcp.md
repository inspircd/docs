---
title: "Module Details: noctcp (v3)"
---

## The "noctcp" Module

### Description

This module adds channel mode `C` (noctcp) which allows channels to block messages which contain CTCPs and user mode `T` (u_noctcp) which allows users to block private messages that contain CTCPs.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="noctcp">
```

#### `<noctcp>`

The `<noctcp>` tag defines settings about how the noctcp module should behave. This tag can only be defined once.

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
enableumode | Boolean | No            | Whether user mode `T` (u_noctcp) is enabled.

##### Example Usage

```xml
<noctcp enableumode="yes">
```

### Channel Modes

Name   | Character | Type   | Parameter Syntax | Usable By         | Description
------ | --------- | ------ | ---------------- | ----------------- | -----------
noctcp | C         | Switch | *None*           | Channel operators | Enables blocking channel messages that contain CTCPs.

### User Modes

Name     | Character | Type   | Parameter Syntax | Usable By | Description
-------- | --------- | ------ | ---------------- | --------- | -----------
u_noctcp | T         | Switch | *None*           | Anyone    | Enables blocking private messages that contain CTCPs.

### Exemptions

Name   | Description
------ | -----------
noctcp | Allows exempted users to send messages that contain CTCPs.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
C         | Acting | `C:<mask>` | Bans &lt;mask&gt; from sending messages that contain CTCPs.

#### Example Usage

Bans users matching `*!*@example.com` from sending messages that contain CTCPs:

```plaintext
/MODE #channel +b C:*!*@example.com
```

### Special Notes

Actions (i.e. /ME) use a CTCP internally but are not blocked by this module.
