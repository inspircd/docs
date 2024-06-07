---
title: v4 Overview
---

!!! note ""
    This page is a work in progress. If you would like to suggest additions to this page [please comment on issue #187](https://github.com/inspircd/inspircd-docs/issues/187).

## v4 Overview

This page contains an overview of the biggest changes in InspIRCd v4.

### Cloaking

The `cloaking` and `hostchange` modules have been combined and modularised to form one consistent cloaking system. Users of the `cloaking` module will not need to do anything to upgrade but users of the `hostchange` module will need to update their configuration.

Core cloaking functionality like user mode `x` (cloak), the `/CLOAK` command, the `<cloak>` configuration tag, and the `cloaks` metadata is now provided by the [`cloak`](/4/modules/cloak) module.

The [`cloak_md5`](/4/modules/cloak_md5) module has been added to provide the v3 `full` and `half` cloaking methods which were previously part of the `cloaking` module. These methods are now deprecated because they use salted MD5 which is no longer considered secure. As with v3 they can be used as a secondary cloak system to prevent breaking bans.

The [`cloak_sha256`](/4/modules/cloak_sha256) module has been added to provide the modern `hmac-sha256` and `hmac-sha256-addr` cloaking systems which cloaks user IP addresses, hostnames, and UNIX socket paths using the standard HMAC-SHA256 algorithm.

The [`cloak_user`](/4/modules/cloak_user) module has been added to provide the ability to cloak users with their userdata. This userdata can be their account name, their account identifier, their nickname, their TLS fingerprint, or their real username. This replaces the `addnick` and `addaccount` action from the v3 `hostchange` module.

The [`cloak_static`](/4/modules/cloak_static) module has been added to provide the ability to cloak users with a static value. This replaces the `set` action from the v3 hostchange module.

### Extended Bans

Extended bans are now a first class feature and have support for match inversion (`!m:R:CoolPerson`) and can be added using their full names instead of a character (e.g. `mute` instead of `m`).

To help migrate over to named extbans you can set `<options:extbanformat>` to `name` to rewrite entries to the new format.

### Logging

Logging has been rewritten in InspIRCd v4 and now has support for support for time-based log rotation, more sensible log levels, and support for logging to:

- JSON (requires [the log_json module](/4/modules/log_json))
- SQL (requires [the log_sql module](/4/modules/log_sql))
- Standard error &amp; output streams ([core](/4/configuration#log))
- syslog (requires [the log_syslog module](/4/modules/log_sql))

The `--debug` option no longer enables raw I/O logging. To enable raw I/O logging the new `--protocoldebug` option must be used.

### Operators

Autologin support is now provided by the core and can match on more fields than just the user's TLS client fingerprint. It now also supports only authenticating a user if their nick matches an account name.

Operator accounts can now opt-out of having a password to push security onto other fields such as a services account name (requires the [account](/4/modules/account) module) or a TLS client fingerprint (requires the [sslinfo](/4/modules/sslinfo) module).

Operator accounts and types can now specify fields directly instead of inheriting them from an operator type or class.

Operator MOTDs can now be customised depending on the type of the operator.

Operator privileges are now synchronised over the network so remote servers can check them.

Services can now grant services privileges to users remotely (requires the [services](/4/modules/services) module).

### TLS

InspIRCd now has stricter requirements regarding TLS. At least one TLS module must now be enabled at build time and servers which link over the public internet must now be linked via TLS.

Using multiple hash algorithms for client fingerprints is now supported. This allows migrating away from old, insecure algorithms like md5. You can also use Subject Public Key Info (SPKI) fingerprint insteads
