---
title: v5 Overview
---

{! _wip.md !}

## v5 Overview

This page contains an overview of the biggest changes in InspIRCd v5. As this release has not become stable yet this list is subject to change.

### Build system

The hand-written Perl/GMake build system has been replaced with CMake. This allows building InspIRCd on more systems without having to add explicit support to the build system and allows building using modern build tools like Ninja.

The interactive Perl configure script has been replaced with a Python rewrite. The questions it asks have also been reworked to be more relevant to the settings that the average user wishes to change.

The Perl Module Manager has been replaced with a Python rewrite. The new version has gained support for checksum-verification of modules, installing modules from specific sources, and viewing extended information about modules before install. Support for enabling extra modules has also moved to Module Manager from the configure script.

InspIRCd will now build using the mold, LLD, or gold linkers instead of the default system linker. This should speed up building InspIRCd on systems where one is available.

InspIRCd will now build with PGO on by default on release builds. This should improve overall performance.
