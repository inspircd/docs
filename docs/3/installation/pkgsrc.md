---
title: v3 pkgsrc Installation
---

## Installing InspIRCd 3 using the pkgsrc package

An official package for [pkgsrc](https://pkgsrc.org) platforms is maintained by [nia](https://github.com/niacat). It lives in chat/inspircd3.

### What systems are supported by this package?

It is known to build on:

* NetBSD (stable, -current)
* illumos (SmartOS, etc)
* Darwin (macOS)
* Linux (CentOS, etc)

Other unix-likes probably work too.

### How do I install this package?

#### Binary package

Using [pkgin](https://pkgsrc.joyent.com):

```sh
pkgin install inspircd
```

Using pkg_install:

```sh
pkg_add inspircd
```

#### Source package.

If you're not using NetBSD, you need to bootstrap first. Consult the [pkgsrc documentation](https://www.netbsd.org/docs/pkgsrc/platforms.html) for information on how to do this.

```sh
cd chat/inspircd3
make package
make install
```

### Where does this package store important files?

As well as the normal system configuration directory (e.g. on NetBSD, `/usr/pkg/etc/inspircd`), important files can be found in `$PREFIX/inspircd`.

### Init scripts

#### rc.subr (NetBSD, others)

By default, the init script is installed to `$PREFIX/share/examples/rc.d/inspircd`, and should be copied to `/etc/rc.d` to be used on NetBSD. Note that `PREFIX` defaults to `/usr/pkg` on NetBSD.

All the normal init commands are available (`service inspircd start`, `service inspircd restart`, etc).

In addition, `rehash` and `sslrehash` commands are available. `rehash` reloads configuration without stopping the server, while `sslrehash` will reload the SSL certificate.
