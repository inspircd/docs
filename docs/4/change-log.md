---
title: v4 Change Log
---

{! 4/_support.md !}

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 4.0.0a1

**This pre-release version of InspIRCd was released on 2021-06-01.**

**IMPORTANT** &mdash; Various breaking changes have also been made. See [the breaking changes page](/4/breaking-changes) for details.

- Added support for case insensitive regular expressions.

- Added support for fake honeypot channels to the securelist module.

- Added support for multi-line command syntax messages.

- Added support for named (i.e. `foo:n!u@h`) and inverted (i.e. `!f:n!u@h`) extbans.

- Added support for network-synchronised metadata on channel memberships.

- Added support for reloading TLS certificates as part of a normal rehash.

- Added support for sending 005 diffs when the server module state changes

- Added support for the sha224, sha384, and sha512 hash algorithms.

- Added the `servers/ignore-securelist` privilege to allow server operators to ignore the securelist module.

- Changed modules to use native platform file extensions (i.e. `.dylib` on macOS and `.dll` on Windows).

- Enabled the regex_stdlib module by default on all systems.

- Fixed losing the set time and setter of list modes when linking servers.
