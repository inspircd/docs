---
title: Module Details (testnet)
---

## The "testnet" Module

<div class="alert alert-danger" role="alert" markdown="1">

This module has been deprecated and will be removed in the next major version of InspIRCd.

</div>

### Description

This module provides facilities for developer testing of InspIRCd modules.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_testnet.so">
```
This module requires no other configuration.

### Commands

Name   | Parameter Count | Syntax                                               | Description
------ | --------------- | ---------------------------------------------------- | -----------
TEST   | 2               | `check`<br>`flood [<lines>]`<br>`freeze [<penalty>]` | Runs the test specified by the user.

#### Example Usage

Checks that all modules are hooked to their event handlers correctly:

```plaintext
/TEST check
```

Floods the requesting user with 400 lines of text:

```plaintext
/TEST flood 400
```

Adds 2000 millicommands of penalty to the requesting user:

```plaintext
/TEST freeze 2000
```

### Special Notes

To ensure that this testing module is not accidentally loaded on a production server your server hostname must contain ".test" to load this module.
