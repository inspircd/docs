---
title: Module Details: inviteexception (v3)
---

## The "inviteexception" Module

### Description

This module adds channel mode `I` (invex) which allows channel operators to exempt user masks from the `i` (inviteonly) channel mode.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="inviteexception">
```

#### `<inviteexception>`

The `<inviteexception>` tag defines settings about how the inviteexception module should behave. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
bypasskey | Boolean | Yes           | Whether channel mode `I` (invex) allows joining users to bypass the `k` (key) channel mode.

##### Example Usage

```xml
<inviteexception bypasskey="yes">
```

### Channel Modes

Name  | Character | Type | Parameter Syntax | Usable By         | Description
----- | --------- | ---- | ---------------- | ----------------- | -----------
invex | I         | List | `<mask>`         | Channel operators | Exempts users matching &lt;mask&gt; from the `i` (inviteonly) channel mode.

#### Example Usage

Exempts users matching `*!*@example.com` from the `i` (inviteonly) channel mode:

```plaintext
/MODE #channel +I *!*@example.com
```

Exempts users logged into the services account named Sadie from the `i` (inviteonly) channel mode (requires [the services_account module](/3/modules/services_account)):

```plaintext
/MODE #channel +I R:Sadie
```
