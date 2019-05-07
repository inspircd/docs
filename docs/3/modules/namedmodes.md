---
title: Module Details (namedmodes)
---

## The "namedmodes" Module

### Description

This module provides support for adding and removing modes via their long names.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="namedmodes">
```

This module requires no other configuration.

### Commands

Name | Parameter Count | Syntax                              | Description
---- | --------------- | ----------------------------------- | -----------
PROP | 1+              | `<target> [(+|-)<name> [<value>]]+` | Allows users to add, remove, and view the modes of a specific target.

#### Example Usage

Lists all channel modes set on #channel:

```plaintext
/PROP #channel
```

Sets channel mode `n` (noextmsg) on #channel:

```plaintext
/PROP #channel +noextmsg
```

Sets channel mode `o` (op) on Sadie in #channel:

```plaintext
/PROP #channel +op Sadie
```

Removes channel mode `n` (noextmsg) from #channel:

```plaintext
/PROP #channel -noextmsg
```

Removes channel mode `o` (op) from Sadie in #channel:

```plaintext
/PROP #channel -op Sadie
```

### Channel Modes

Name     | Character | Type | Parameter Syntax   | Description
-------- | --------- | ---- | ------------------ | -----------
namebase | Z         | List | `<name>[=<value>]` | Allows users to add, remove, and view the modes of a specific target.

#### Example Usage

Lists all channel modes set on #channel:

```plaintext
/MODE #channel +Z
```

Sets channel mode `n` (noextmsg) on #channel:

```plaintext
/MODE #channel +Z noextmsg
```

Sets channel mode `o` (op) on Sadie in #channel:

```plaintext
/MODE #channel +Z op=Sadie
```

Removes channel mode `n` (noextmsg) from #channel:

```plaintext
/MODE #channel -Z noextmsg
```

Removes channel mode `o` (op) from Sadie in #channel:

```plaintext
/MODE #channel -Z op=Sadie
```
