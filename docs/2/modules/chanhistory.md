---
title: Module Details: chanhistory (v2)
---

{! 2/_support.md !}

## The "chanhistory" Module

### Description

This module adds channel mode `H` (history) which allows message history to be viewed on joining the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_chanhistory.so">
```

#### `<chanhistory>`

The `<chanhistory>` tag defines settings about how the chanhistory module should behave. This tag can only be defined once.

Name     | Type    | Default Value | Description
-------- | ------- | ------------- | -----------
bots     | Boolean | Yes           | Whether users with the bot user mode (+B) will receive history.
notice   | Boolean | Yes           | Whether to send a notice before sending history.
maxlines | Number  | 50            | The maximum number of lines of history that a channel can keep.

##### Example Usage

```xml
<chanhistory bots="yes"
             notice="yes"
             maxlines="50">
```

### Channel Modes

Name    | Character | Type      | Parameter Syntax   | Description
------- | --------- | --------- | ------------------ | -----------
history | H         | Parameter | `<count>:<period>` | Sends up to &lt;count&gt; messages from the last &lt;period&gt; on join.

#### Example Usage

Replays up to 10 messages from the last 30 minutes:

```plaintext
/MODE #channel +H 10:1800
```

Replays up to 25 messages from the last two hours:

```plaintext
/MODE #channel +H 25:2h
```
