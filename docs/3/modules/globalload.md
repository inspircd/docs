---
title: "Module Details: globalload (v3)"
---

## The "globalload" Module

### Description

This module adds the `/GLOADMODULE`, `/GRELOADMODULE`, and `/GUNLOADMODULE` commands which allows server operators to load, reload, and unload modules on remote servers.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="globalload">
```

This module requires no other configuration.

### Commands

Name          | Parameter Count | Syntax                | Description
------------- | --------------- | --------------------- | -----------
GLOADMODULE   | 1-2             | `<module> [<server>]` | Loads &lt;module&gt; on servers matching the  &lt;server&gt; glob pattern. If no pattern is given then it is loaded on all servers.
GRELOADMODULE | 1-2             | `<module> [<server>]` | Reloads &lt;module&gt; on servers matching the &lt;server&gt; glob pattern. If no pattern is given then it is reloaded on all servers.
GUNLOADMODULE | 1-2             | `<module> [<server>]` | Unloads &lt;module&gt; on servers matching the &lt;server&gt; glob pattern. If no pattern is given then it is unloaded on all servers.

#### Example Usage

Loads [the botmode module](/3/modules/botmode) on all servers:

```plaintext
/GLOADMODULE botmode
```

Loads [the botmode module](/3/modules/botmode) on servers matching \*.eu.example.com:

```plaintext
/GLOADMODULE botmode *.eu.example.com
```

Reloads [the check module](/3/modules/check) on all servers:

```plaintext
/GRELOADMODULE check
```

Reloads [the check module](/3/modules/check) on servers matching \*.na.example.com:

```plaintext
/GRELOADMODULE check *.na.example.com
```

Unloads [the gecosban module](/3/modules/gecosban) on all servers:

```plaintext
/GUNLOADMODULE gecosban
```

Unloads [the gecosban module](/3/modules/gecosban) on servers matching \*.sea.example.com:

```plaintext
/GUNLOADMODULE gecosban *.sea.example.com
```
