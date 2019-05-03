---
title: Module Details (regex_posix)
---

## The "regex_posix" Module

<div class="alert alert-info" role="alert" markdown="1">

This module depends on a UNIX-specific system library and must be manually enabled at compile time.

If you are running on a compatible UNIX system you can enable this module using the following command:

```sh
./configure --enable-extras=m_regex_posix.cpp
```

</div>

<div class="alert alert-danger" role="alert" markdown="1">

This module has been deprecated and will be removed in the next major version of InspIRCd.

You should use [the regex_stdlib module](/3/modules/regex_stdlib) in bre (basic) or ere (extended) mode instead.

</div>

### Description

This module provides a regular expression engine which uses the [POSIX.2](https://www.gnu.org/software/libc/manual/html_node/POSIX-Regexp-Compilation.html#POSIX-Regexp-Compilation) regular expression matching system.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="regex_posix">
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
