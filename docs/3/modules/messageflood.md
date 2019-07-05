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

#### `<messageflood>`

The `<messageflood>` tag defines settings about how the messageflood module should behave. This tag can only be defined once.

Name    | Type    | Default Value | Description
------- | ------- | ------------- | -----------
notice  | Decimal | 1.0           | [**New in v3.2.0!**](/3/change-log/#inspircd-320) The number of lines that a single `NOTICE` message is equivalent to.
privmsg | Decimal | 1.0           | [**New in v3.2.0!**](/3/change-log/#inspircd-320) The number of lines that a single `PRIVMSG` message is equivalent to.
tagmsg  | Decimal | 0.2           | [**New in v3.2.0!**](/3/change-log/#inspircd-320) The number of lines that a single `NOTICE` message is equivalent to. This should be lower than the other commands to avoid users being kicked by automated client features such as typing notifications.

##### Example Usage

```xml
<messageflood notice="1.0"
              privmsg="1.0"
              tagmsg="0.2">
```
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
