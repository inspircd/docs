---
title: Module Details (globalload)
---

## The "globalload" Module

### Description

This module adds the `/GLOADMODULE`, `/GRELOADMODULE`, and `/GUNLOADMODULE` commands which allows server operators to load, reload, and unload modules on remote servers.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_globalload.so">
```

This module requires no other configuration.

### Commands

Name          | Parameter Count | Syntax                | Description
------------- | --------------- | --------------------- | -----------
GLOADMODULE   | 1-2             | `<module> [<server>]` | Loads &lt;module&gt; on servers matching the  &lt;server&gt; glob pattern. If no pattern is given then it is loaded on all servers.
GRELOADMODULE | 1-2             | `<module> [<server>]` | Reloads &lt;module&gt; on servers matching the &lt;server&gt; glob pattern. If no pattern is given then it is reloaded on all servers.
GUNLOADMODULE | 1-2             | `<module> [<server>]` | Unloads &lt;module&gt; on servers matching the &lt;server&gt; glob pattern. If no pattern is given then it is unloaded on all servers.

#### Example Usage

Loads [the botmode module](/2/modules/botmode) on all servers:

```plaintext
/GLOADMODULE m_botmode.so
```

Loads [the botmode module](/2/modules/botmode) on servers matching \*.eu.example.com:

```plaintext
/GLOADMODULE m_botmode.so *.eu.example.com
```

Unloads [the check module](/2/modules/check) on all servers:

```plaintext
/GUNLOADMODULE m_check.so
```

Unloads [the check module](/2/modules/check) on servers matching \*.na.example.com:

```plaintext
/GUNLOADMODULE m_check.so *.na.example.com
```

Reloads [the gecosban module](/2/modules/gecosban) on all servers:

```plaintext
/GUNLOADMODULE m_gecosban.so
```

Reloads [the gecosban module](/2/modules/gecosban) on servers matching \*.sea.example.com:

```plaintext
/GUNLOADMODULE m_gecosban.so *.sea.example.com
```
