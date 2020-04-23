---
title: Module Details: blockamsg (v3)
---

## The "blockamsg" Module

### Description

This module blocks mass messages sent using the `/AME` and `/AMSG` commands that exist in clients such as mIRC and HexChat.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="blockamsg">
```

#### `<blockamsg>`

The `<blockamsg>` tag defines settings about how the blockamsg module should behave. This tag can only be defined once.

Name   | Type     | Default Value | Description
------ | -------- | ------------- | -----------
delay  | Duration | 3s            | The duration between identical messages to consider them a mass message or 0 to allow any gap.
action | Text     | killopers     | The action to take when the module has detected a user sending a mass message.

The action field should be set to one of the following values:

Value       | Description
----------- | -----------
kill        | Disconnect the sending user from the server.
killopers   | Disconnect the sending user from the server and notify server operators.
notice      | Inform the sending user that their repeated message has been discarded.
noticeopers | Inform the sending user that their repeated message has been discarded and notify server operators.
silent      | Silently discard repeated messages.

##### Example Usage

```xml
<blockamsg delay="5s"
           action="killopers">
```
