---
title: "Module Details: anticaps (v3)"
---

## The "anticaps" Module

### Description

This module adds channel mode `B` (anticaps) which allows channels to block messages which are excessively capitalised.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="anticaps">
```

#### `<anticaps>`

The `<anticaps>` tag defines settings about how the anticaps module should behave. This tag can only be defined once.

Name      | Type   | Default Value              | Description
--------- | ------ | -------------------------- | -----------
lowercase | Text   | abcdefghijklmnopqrstuvwxyz | A list of characters to treat as lower case letters.
uppercase | Text   | ABCDEFGHIJKLMNOPQRSTUVWXYZ | A list of characters to treat as upper case letters.

#### Example Usage

```xml
<anticaps lowercase="abcdefghijklmnopqrstuvwxyz"
          uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ">
```

### Channel Modes

Name     | Character | Type      | Parameter Syntax                                   | Usable By         | Description
-------- | --------- | --------- | -------------------------------------------------- | ----------------- | -----------
anticaps | B         | Parameter | `<ban|block|mute|kick|kickban>:<minlen>:<percent>` | Channel operators | Enables blocking excessively capitalised messages.

#### Example Usage

Kicks users who send a message which is longer than five characters and is more than 75% capital letters:

```plaintext
/MODE #channel +B kick:5:75
```

### Exemptions

Name      | Description
--------- | -----------
anticaps  | Allows exempted users to send overly capitalised messages.
