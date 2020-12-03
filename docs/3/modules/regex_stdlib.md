---
title: "Module Details: regex_stdlib (v3)"
---

## The "regex_stdlib" Module

!!! note ""
    This module depends on C++11-specific features and must be manually enabled at compile time.

    If you are building with a C++11-compatible compiler you can enable this module using the following command:

    <pre><code>./configure --enable-extras regex_stdlib</code></pre>

### Description

This module provides a regular expression engine which uses the [C++11 std::regex](https://en.cppreference.com/w/cpp/regex/syntax_option_type#Constants) regular expression matching system.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="regex_stdlib">
```

#### `<stdregex>`

The `<stdregex>` tag defines settings about how the regex_stdlib module should behave. This tag can only be defined once.

Name | Type | Default Value | Description
---- | ---- | ------------- | -----------
type | Text | ecmascript    | The regular expression grammar to use when matching.

The type field should be set to one of the following values:

Value      | Description
---------- | -----------
awk        | Use the regular expression grammar used by the awk utility in POSIX.
bre        | Use the basic POSIX regular expression grammar.
ecmascript | Use the [modified ECMAScript regular expression grammar](https://en.cppreference.com/w/cpp/regex/ecmascript).
egrep      | Use the regular expression grammar used by the grep utility, with the -E option, in POSIX.
ere        | Use the extended POSIX regular expression grammar.
grep       | Use the regular expression grammar used by the grep utility in POSIX.

##### Example Usage

```xml
<stdregex ecmascript="yes">
```
