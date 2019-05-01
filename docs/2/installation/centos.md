---
title: CentOS Linux Installation
---

## Installing InspIRCd 2 using the CentOS package

An official package for CentOS is maintained by [Adam](https://github.com/Adam-). You can download this from [the releases page](https://github.com/inspircd/inspircd/releases/latest).

### What systems are supported by this package?

This package can be installed on all x86-64 systems running CentOS 7.

### How do I install this package?

First, download the RPM package to your server using Wget. If you do not have Wget installed you can install it using `sudo yum install wget`.

```sh
# Replace the URL here with the URL you obtained from the releases page.
wget "https://github.com/inspircd/inspircd/releases/download/[VERSION]/inspircd-[VERSION].el7.centos.x86_64.rpm"
```

Once the package has downloaded ensure that the file has not been corrupted during download by running `sha256sum` and comparing its output to the hash specified on the releases page.

```sh
# Replace the filename here with the name of the file you obtained from the releases page.
sha256sum "./inspircd-[VERSION].el7.centos.x86_64.rpm"
```

If the hash matches the one specified on the releases page you can proceed to install the package.

```sh
# Replace the filename here with the name of the file you obtained from the releases page.
sudo yum install "./inspircd-[VERSION].el7.centos.x86_64.rpm"
```

The package should now be installed and you can proceed to set up your [configuration](/2/configuration).

### Where does this package store important files?

Configuration files are stored in `/etc/inspircd`.

Data files are stored in `/var/inspircd`.

Log files are stored in `/var/log/inspircd`.
