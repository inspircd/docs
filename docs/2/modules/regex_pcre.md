---
title: Module Details (regex_pcre)
---

{! 2/_support.md !}

## The "regex_pcre" Module

<div class="alert alert-info" role="alert" markdown="1">

This module depends on a third-party library ([PCRE](https://www.pcre.org)) and must be manually enabled at compile time.

Once you have installed the dependency you can enable this module using the following command:

```sh
./configure --enable-extras=m_regex_pcre.cpp
```

</div>

### Description

This module provides a regular expression engine which uses the [PCRE](https://www.pcre.org) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_regex_pcre.so">
```

This module requires no other configuration.
