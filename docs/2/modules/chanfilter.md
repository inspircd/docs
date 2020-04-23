---
title: Module Details: chanfilter (v2)
---

{! 2/_support.md !}

## The "chanfilter" Module

### Description

This module adds channel mode `g` (filter) which allows channel operators to define glob patterns for inappropriate phrases that are not allowed to be used in the channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_chanfilter.so">
```

#### `<chanfilter>`

The `<chanfilter>` tag defines settings about how the chanfilter module should behave. This tag can only be defined once.

Name     | Type    | Default Value | Description
-------- | ------- | ------------- | -----------
hidemask | Boolean | No            | Whether users can see the inappropriate phrase that their message matched.

##### Example Usage

```xml
<chanfilter hidemask="no">
```

### Channel Modes

Name   | Character | Type | Parameter Syntax | Description
------ | --------- | ---- | ---------------- | -----------
filter | g         | List | `<glob>`         | Prevents users from sending messages that match &lt;glob&gt;.

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

The chanfilter module does not allow filters longer than 35 bytes to be added. This limit will be raised and made customisable in the next release.

Due to limitations of the IRC protocol filters containing spaces can not be added.
