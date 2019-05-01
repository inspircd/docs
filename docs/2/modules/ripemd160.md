---
title: Module Details (ripemd160)
---

## The "ripemd160" Module

<div class="alert alert-danger" role="alert" markdown="1">

This module has been deprecated and will be removed in the next major version of InspIRCd.

You should use [the sha256 module](/2/modules/sha256) instead.

</div>

### Description

This module allows other modules to generate [RIPEMD-160](https://en.wikipedia.org/wiki/RIPEMD) hashes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_ripemd160.so">
```

This module requires no other configuration.
