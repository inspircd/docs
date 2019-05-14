---
title: Change Log
---

## Change Log

This page lists changes which have happened between releases.

### InspIRCd 3.1.0

**This version of InspIRCd has not yet been released.**

- Added a configure option, `--disable-auto-extras`, which disables automatically enabling extras for which the dependencies are available.

- Added support for disabling a STS policy for users in specific connect classes. 

- Developer: added support for modules overriding the default access checks for `NOTICE`, `PRIVMSG`, and `TAGMSG`.

- Developer: added the `INSPIRCD_VERSION_BEFORE(MAJOR, MINOR)` and `INSPIRCD_VERSION_SINCE(MAJOR, MINOR)` macros for checking the InspIRCd version at compile time.

- Developer: allowed child classes of SSLIOHook to override `GetCertificate()` and `GetFingerprint()`.

- Fixed configure not failing when invalid options were passed to it.

- Fixed servers not specifying whether they are hidden. If no visibility is specified then servers default to the visibility of their parent server.

### InspIRCd 3.0.1

**This version of InspIRCd was released on 2019-05-10.**

- Documented the anticaps exemption in both the main config and in the example helpop config.

- Documented user mode `O` (override) in the helpop config.

- Fixed building against older versions of glibc.

- Fixed compiling with the kqueue socket engine on NetBSD.

- Fixed relying on PWD being set in the makefile.

- Fixed the `--distribution-label` configure option erroneously making the configure script require the `--development` flag to be passed.

- Fixed the example `<wsorigin>` tag erroneously suggesting that a path was included.

- Fixed the filesystem permissions that files are installed with.

- Fixed the MAXLIST 005 token not reflecting the true lower limit.

- Fixed the parameters for the `/NAMES` command in the syntax hint and example helpop config.

- Raised the connection timeout in the example configs to 20s. This should give more time for clients on slow connections that want to do a lot of things (request caps, do SASL auth, etc) on connect.

- Silenced a harmless compiler warning in the pgsql module on newer GCCs.
