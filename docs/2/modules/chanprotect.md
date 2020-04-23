---
title: Module Details: chanprotect (v2)
---

{! 2/_support.md !}

## The "chanprotect" Module

!!! warning ""
    This module has been deprecated and will be removed in the next major version of InspIRCd.

    You should use [the customprefix module](/2/modules/customprefix) instead.

### Description

This module adds channel prefix modes `a` (admin) and `q` (founder).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_chanprotect.so">
```

#### `<chanprotect>`

The `<chanprotect>` tag defines settings about how the chanprotect module should behave. This tag can only be defined once.

Name            | Type    | Default Value | Description
--------------- | ------- | ------------- | -----------
aprefix         | Text    | *None*        | The prefix character for the +a mode.
qprefix         | Text    | *None*        | The prefix character for the +q mode.
deprotectself   | Boolean | Yes           | Whether users with +a or +q can remove the mode from themself.
deprotectothers | Boolean | Yes           | Whether users with +a or +q can remove the mode from other users.
noservices      | Boolean | No            | Whether to grant +q to the first user who joins the channel.

##### Example Usage

```xml
<chanprotect aprefix="&amp;"
             qprefix="~"
             deprotectself="yes"
             deprotectothers="yes"
             noservices="no">
```

### Channel Modes

Name    | Character | Type      | Parameter Syntax | Description
------- | --------- | --------- | ---------------- | -----------
admin   | a (~)     | Prefix    | `<nick>`         | Grants channel admin status to &lt;nick&gt;.
founder | q (&amp;) | Prefix    | `<nick>`         | Grants channel founder status to &lt;nick&gt;.

#### Example Usage

Grants channel admin status to Sadie:

```plaintext
/MODE #channel +a Sadie
```

Grants channel founder status to Adam:

```plaintext
/MODE #channel +q Adam
```
