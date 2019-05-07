---
title: Module Details (opermotd)
---

## The "opermotd" Module

### Description

This module adds the `/OPERMOTD` command which adds a special message of the day for server operators.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_opermotd.so">
```

#### `<files>` &amp; `<execfiles>`

This module extends the core `<files>` and `<execfiles>` tags with the following fields:

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
opermotd | Text | *None*        | The file to read or command to execute to obtain the opermotd text.

##### Example Usage

Obtains the server operator message of the day by reading conf/opermotd.txt:

```xml
<files ...
       opermotd="conf/opermotd.txt">
```

Obtains the server operator message of the day by executing `curl https://www.example.com/opermotd.txt`:

```xml
<execfiles ...
           opermotd="curl https://www.example.com/opermotd.txt">
```

#### `<opermotd>`

The `<opermotd>` tag defines settings about how the opermotd module should behave. This tag can only be defined once.

Name          | Type    | Default Value | Description
------------- | ------- | ------------- | -----------
file          | Text    | opermotd      | The name of the field in &lt;files&gt; / &lt;execfiles&gt; to use when reading the server operator message of the day.
onoper        | Boolean | Yes           | Whether to send the server operator message of the day to server operators when they log into their server operator account.
processcolors | Boolean | No            | Whether to process IRC formatting escapes within the server operator message of the day.

##### Example Usage

```xml
<opermotd file="opermotd"
          onoper="yes"
          processcolors="yes">
```

### Commands

Name     | Parameter Count | Syntax       | Description
-------- | --------------- | ------------ | -----------
OPERMOTD | 0-1             | `[<server>]` | Requests the server operator message of the day for &lt;server&gt;.

#### Example Usage

Requests the server operator message of the day for the local server:

```plaintext
/OPERMOTD
```

Requests the server operator message of the day for irc.example.com:

```plaintext
/OPERMOTD irc.example.com
```
