---
title: Module Details: blockamsg (v2)
---

{! 2/_support.md !}

## The "blockamsg" Module

### Description

This module blocks mass messages sent using the `/AME` and `/AMSG` commands that exist in clients such as mIRC and HexChat.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_blockamsg.so">
```

#### `<blockamsg>`

The `<blockamsg>` tag defines settings about how the blockamsg module should behave. This tag can only be defined once.

Name   | Type   | Default Value | Description
------ | ------ | ------------- | -----------
delay  | Number | -1            | The number of seconds gap between identical messages to consider them a mass message or -1 to allow any gap.
action | Text   | killopers     | The action to take when the module has detected a user sending a mass message.

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
<blockamsg delay="5"
           action="killopers">
```
