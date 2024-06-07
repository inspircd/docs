---
title: v4 Installation
---

## Installing InspIRCd 4

There are many different methods for installing InspIRCd. You should pick the method which fits your needs best.

### Docker

An official InspIRCd Docker image will be available on [Docker Hub](https://hub.docker.com/r/inspircd/inspircd-docker/) when v4 is released. Until that happens you will have to build from source.

### Packages

The InspIRCd team provide prebuilt packages for some common platforms. If you are using one of these platforms and do not want to install any third party modules it is recommended that you use one of these.

* [CentOS (EL7)](/4/installation/centos)

* [Debian](/4/installation/debian)

* [Rocky Linux (EL8, EL9)](/4/installation/rocky)

* [Ubuntu](/4/installation/ubuntu)

* [Windows](/4/installation/windows)

Some distributions may ship their own InspIRCd packages. Using these is not recommended as they are frequently out of date and do not contain the latest security fixes applied upstream.

### Source

On all other platforms the recommended installation method is to [build from source](/4/installation/source). You can choose between building the [the most recent release](/4/installation/source#release-tarball) or, if you enjoy living on the edge, [the latest code committed to Git](/4/installation/source#git). If you are building on Windows you should follow [these instructions instead](/4/installation/windows-source).
