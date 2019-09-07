---
title: Module Details (blockcaps)
---

## The "blockcaps" Module

<div class="alert alert-danger" role="alert" markdown="1">

This module has been deprecated and will be removed in the next major version of InspIRCd.

You should use [the anticaps module](/3/modules/anticaps) instead.

</div>

### Description

This module adds channel mode `B` (blockcaps) which allows channels to block messages which are excessively capitalised.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="blockcaps">
```

#### `<blockcaps>`

The `<blockcaps>` tag defines settings about how the blockcaps module should behave. This tag can only be defined once.

Name      | Type   | Default Value              | Description
--------- | ------ | -------------------------- | -----------
lowercase | Text   | abcdefghijklmnopqrstuvwxyz | A list of characters to treat as lower case letters.
minlen    | Number | 1                          | The minimum length of a message to block excessive capitalisation.
percent   | Number | 100                        | The percentage of a message which can be capitalised before it is blocked.
uppercase | Text   | ABCDEFGHIJKLMNOPQRSTUVWXYZ | A list of characters to treat as upper case letters.

#### Example Usage

```xml
<blockcaps lowercase="abcdefghijklmnopqrstuvwxyz"
           minlen="1"
           percent="100"
           uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ">
```

### Channel Modes

Name      | Character | Type   | Parameter Syntax | Usable By         | Description
--------- | --------- | ------ | ---------------- | ----------------- | -----------
blockcaps | B         | Switch | *None*           | Channel operators | Enables blocking excessively capitalised messages.

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
