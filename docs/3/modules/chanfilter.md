---
title: "Module Details: chanfilter (v3)"
---

## The "chanfilter" Module

### Description

This module adds channel mode `g` (filter) which allows channel operators to define glob patterns for inappropriate phrases that are not allowed to be used in the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="chanfilter">
```

#### `<chanfilter>`

The `<chanfilter>` tag defines settings about how the chanfilter module should behave. This tag can only be defined once.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
hidemask   | Boolean | No            | Whether users can see the inappropriate phrase that their message matched.
notifyuser | Boolean | Yes           | Whether to notify users when they have matched a filter.
maxlen     | Number  | 35            | The maximum length of a parameter for channel mode `g` (filter).

##### Example Usage

```xml
<chanfilter hidemask="no"
            notifyuser="yes"
            maxlen="50">
```

### Channel Modes

Name   | Character | Type | Parameter Syntax | Usable By         | Description
------ | --------- | ---- | ---------------- | ----------------- | -----------
filter | g         | List | `<glob>`         | Channel operators | Prevents users from sending messages that match &lt;glob&gt;.

#### Example Usage

Prevents users from saying the phrase "fluffy capybara":

```plaintext
/MODE #channel +g *fluffy?capybara*
```

### Exemptions

Name   | Description
------ | -----------
filter | Allows exempted users to send messages that contain censored phrases.

### Special Notes

Due to limitations of the IRC protocol filters containing spaces can not be added.
