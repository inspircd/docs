---
title: Module Details (regex_re2)
---

## The "regex_re2" Module

<div class="alert alert-info" role="alert" markdown="1">

This module depends on a third-party library ([RE2](https://github.com/google/re2)) and must be manually enabled at compile time.

Once you have installed the dependency you can enable this module using the following command:

```sh
./configure --enable-extras=m_regex_re2.cpp
```

</div>

### Description

This module provides a regular expression engine which uses the [RE2](https://github.com/google/re2) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="regex_re2">
```

This module requires no other configuration.
