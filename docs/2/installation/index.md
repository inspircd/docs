---
title: v2 Installation
---

{! 2/_support.md !}

## Installing InspIRCd 2

There are many different methods for installing InspIRCd. You should pick the method which fits your needs best.

### Docker

An official InspIRCd Docker image is available on [Docker Hub](https://hub.docker.com/r/inspircd/inspircd-docker/).

### Packages

The InspIRCd development team provide prebuilt packages for some common platforms. If you are using
one of these platforms and do not want to install any third party modules it is recommended that you
use one of these.

* [CentOS Linux](/2/installation/centos)

* [Debian Linux](/2/installation/debian)

* [Microsoft Windows](/2/installation/windows)

Some distributions may ship their own InspIRCd packages. Using these is not recommended as they are frequently out of date and do not contain the latest security fixes applied upstream.

### Source

On all other platforms the recommended installation method is to [build from source](/2/installation/source). You can choose between building the [the most recent release](/2/installation/source#release-tarball) or, if you enjoy living on the edge, [the latest code committed to Git](/2/installation/source#git).
