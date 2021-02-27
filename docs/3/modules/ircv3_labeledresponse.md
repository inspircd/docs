---
title: "Module Details: ircv3_labeledresponse (v3)"
---

## The "ircv3_labeledresponse" Module

!!! note "New in v3.5.0!"
    If you are using an older version you will need to upgrade to use this module.

### Description

This module provides support for [the IRCv3 Labeled Response specification](https://ircv3.net/specs/extensions/labeled-response.html).

This applies only for **registered** clients who negotiated the `batch` capability in addition to `labeled-response`.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ircv3_labeledresponse">
```

This module requires no other configuration.

### Client Capabilities

Name                                                                          | Description
---------------------------------------------------------------------------- | -----------
[labeled-response](https://ircv3.net/specs/extensions/labeled-response.html) | Enables support for the IRCv3 Labeled Response specification.
