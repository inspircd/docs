---
title: Module Details: regex_posix (v2)
---

{! 2/_support.md !}

## The "regex_posix" Module

!!! note ""
    This module depends on a UNIX-specific system library and must be manually enabled at compile time.

    If you are running on a UNIX system you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_regex_posix.cpp</code></pre>

### Description

This module provides a regular expression engine which uses the [POSIX.2](https://www.gnu.org/software/libc/manual/html_node/POSIX-Regexp-Compilation.html#POSIX-Regexp-Compilation) regular expression matching system.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_regex_posix.so">
```

#### `<posix>`

The `<posix>` tag defines settings about how the regex_posix module should behave. This tag can only be defined once.

Name     | Type    | Default Value | Description
-------- | ------- | ------------- | -----------
extended | Boolean | No            | Whether to enable extended regular expression matching.

##### Example Usage

```xml
<posix extended="yes">
```
