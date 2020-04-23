---
title: Module Details: httpd_stats (v2)
---

{! 2/_support.md !}

## The "httpd_stats" Module

### Description

This module provides XML-serialised statistics about the server, channels, and users over HTTP via the /stats path.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_httpd_stats.so">
```

This module requires no other configuration.

### Special Notes

Leaking your server statistics over the internet is a privacy and security risk. You should avoid doing this by either configuring [the httpd module](/2/modules/httpd) to only listen for local connections or by using [the httpd_acl module](/2/modules/httpd_acl) to restrict who can view your server configuration.
