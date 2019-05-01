---
title: Versioning Policy
---

## How InspIRCd releases are versioned

### Summary

As of InspIRCd 3.0.0 a new versioning policy has been adopted to allow users to easily determine how safe an upgrade will be.

The format of an InspIRCd version number is now `<MAJOR>.<MINOR>.<PATCH>[-<LABEL>]`. These components are defined as follows:

- MAJOR &mdash; Incremented when configuration, linking protocol, and/or module API (not module ABI, see below) compatibility is broken. Also incremented when the minimum C++ standard version and/or minimum C++ compiler version is raised.

- MINOR &mdash; Incremented when a new feature, configuration, linking protocol, and/or module API is added in a backwards-compatible way.

- PATCH &mdash; Incremented when bugs are fixed. No configuration, linking protocol, and/or module API changes will happen in this release type.

- LABEL &mdash; An optional descriptor (e.g. a9, rc1, etc) that defines the stability of a pre-release. No level of compatibility is guaranteed between releases with a label.

#### ABI compatibility

Module ABI compatibility happens on a best-effort basis. We will try to keep ABI-breaking changes to MAJOR and MINOR releases but guaranteeing this can be hard considering the fickle nature of C++ compilers.

When the module ABI is knowingly broken the internal ABI version will be incremented to ensure incompatible modules can no longer load without being rebuilt.

#### Vendor Directory

The contents of the vendor directory are considered internal and have no guarantee of compatibility across releases. If you are writing a module that depends on a third-party library you should either include it with your module or look it up with pkg-config.

### Frequently Asked Questions

#### Why not use Semantic Versioning?

Semantic Versioning is intended for libraries and has several issues that make it unsuitable for versioning software like InspIRCd. Most notably Semantic Versioning is intended for libraries and is concerned with ensuring API compatibility whereas InspIRCd has many different kinds of compatibility it needs to be concerned with (configuration, linking protocol, module API, module ABI) with varying levels of importance.
