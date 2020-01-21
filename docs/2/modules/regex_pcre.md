---
title: Module Details (regex_pcre)
---

{! 2/_support.md !}

## The "regex_pcre" Module

!!! note ""
    This module depends on a third-party library ([PCRE](https://www.pcre.org)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_regex_pcre.cpp</code></pre>

### Description

This module provides a regular expression engine which uses the [PCRE](https://www.pcre.org) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_regex_pcre.so">
```

This module requires no other configuration.
