---
title: Module Details (muteban)
---

{! 2/_support.md !}

## The "muteban" Module

### Description

This module adds extended ban `m` which bans specific masks from speaking in a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_muteban.so">
```

This module requires no other configuration.

### Extended Bans

Character | Type   | Ban Syntax | Description
--------- | ------ | ---------- | -----------
m         | Acting | `m:<mask>` | Bans &lt;mask&gt; from speaking in the channel.
