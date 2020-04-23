---
title: Module Details: blockcaps (v2)
---

{! 2/_support.md !}

## The "blockcaps" Module

### Description

This module adds channel mode `B` (blockcaps) which allows channels to block messages which are excessively capitalised.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_blockcaps.so">
```

#### `<blockcaps>`

The `<blockcaps>` tag defines settings about how the blockcaps module should behave. This tag can only be defined once.

Name    | Type   | Default Value              | Description
------- | ------ | -------------------------- | -----------
capsmap | Text   | ABCDEFGHIJKLMNOPQRSTUVWXYZ | A list of characters to treat as capital letters.
minlen  | Number | 1                          | The minimum length of a message to block excessive capitalisation.
percent | Number | 100                        | The percentage of a message which can be capitalised before it is blocked.

#### Example Usage

```xml
<blockcaps capsmap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
           minlen="1"
           percent="100">
```

### Channel Modes

Name      | Character | Type   | Parameter Syntax | Description
--------- | --------- | ------ | ---------------- | -----------
blockcaps | B         | Switch | *None*           | Enables blocking excessively capitalised messages.

### Exemptions

Name      | Description
--------- | -----------
blockcaps | Allows exempted users to send overly capitalised messages.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
B         | Acting | `B:<mask>` | Bans &lt;mask&gt; from sending messages with excessive capitalisation.

##### Example Usage

Bans users matching `*!*@example.com` from sending messages with excessive capitalisation:

```plaintext
/MODE #channel +b B:*!*@example.com
```
