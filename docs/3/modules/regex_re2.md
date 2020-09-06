---
title: "Module Details: regex_re2 (v3)"
---

## The "regex_re2" Module

!!! note ""
    This module depends on a third-party library ([RE2](https://github.com/google/re2)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras regex_re2</code></pre>

### Description

This module provides a regular expression engine which uses the [RE2](https://github.com/google/re2) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="regex_re2">
```

This module requires no other configuration.
