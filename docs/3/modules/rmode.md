---
title: "Module Details: rmode (v3)"
---

## The "rmode" Module

### Description

This module allows removal of channel list modes using glob patterns.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="rmode">
```

This module requires no other configuration.

### Commands

Name  | Parameter Count | Syntax                         | Description
----- | --------------- | ------------------------------ | -----------
RMODE | 2-3             | `<channel> <mode> [<pattern>]` | Removes all &lt;mode&gt; list modes matching &lt;pattern&gt;, or all if no pattern is specified.

#### Example Usage

Removes all bans on #example:

```plaintext
/RMODE #example b
```

Removes all bans on #example matching \*foo\*:

```plaintext
/RMODE #example b *foo*
```
