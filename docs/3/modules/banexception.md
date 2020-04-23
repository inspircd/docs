---
title: Module Details: banexception (v3)
---

## The "banexception" Module

### Description

This module adds channel mode `e` (banexception) which allows channel operators to exempt user masks from the `b` (ban) channel mode.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="banexception">
```

This module requires no other configuration.

### Channel Modes

Name         | Character | Type | Parameter Syntax | Usable By         | Description
------------ | --------- | ---- | ---------------- | ----------------- | -----------
banexception | e         | List | `<mask>`         | Channel operators | Exempts users matching &lt;mask&gt; from the `b` (ban) channel mode.

#### Example Usage

Exempts users matching `*!*@example.com` from the `b` (ban) channel mode:

```plaintext
/MODE #channel +e *!*@example.com
```

Exempts users logged into the services account named Sadie from the `b` (ban) channel mode (requires [the services_account module](/3/modules/services_account)):

```plaintext
/MODE #channel +e R:Sadie
```
