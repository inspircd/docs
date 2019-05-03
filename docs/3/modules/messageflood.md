---
title: Module Details (messageflood)
---

## The "messageflood" Module

### Description

This module adds channel mode `f` (flood) which helps protect against spammers which mass-message channels.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="messageflood">
```

This module requires no other configuration.

### Channel Modes

Name  | Character | Type      | Parameter Syntax       | Description
----- | --------- | --------- | ---------------------- | -----------
flood | f         | Parameter | `(*)<lines>:<seconds>` | Kicks users who send more than &lt;lines&gt; messages in the last &lt;seconds&gt; seconds. If prefixed with * then offending users are also banned.

#### Example Usage

Prevents more than four messages in the last two seconds:

```plaintext
/MODE #channel +f 4:2
```

### Exemptions

Name  | Description
----- | -----------
flood | Allows exempted users to send messages at a higher rate than channel mode `f` (flood) allows.
