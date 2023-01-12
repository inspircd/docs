---
title: v3 Ubuntu Installation
---

## Installing InspIRCd 3 using the Ubuntu package

An official package for Ubuntu is maintained by the InspIRCd Team. You can download this from [the releases page](https://github.com/inspircd/inspircd/releases/latest).

### What systems are supported by this package?

This package can be installed on all x86-64 systems running Ubuntu 18.04 (Bionic Beaver), 20.04 (Focal Fossa), and 22.04 (Jammy Jellyfish).

### How do I install this package?

First, download the .deb package to your server using Wget. If you do not have Wget installed you can install it using `sudo apt-get install wget`.

```sh
# Replace the URL here with the URL you obtained from the releases page.
wget "https://github.com/inspircd/inspircd/releases/download/[VERSION]/inspircd_[VERSION]_amd64.deb"
```

Once the package has downloaded ensure that the file has not been corrupted during download by running `sha256sum` and comparing its output to the hash specified on the releases page.

```sh
# Replace the filename here with the name of the file you obtained from the releases page.
sha256sum "./inspircd_[VERSION]_amd64.deb"
```

If the hash matches the one specified on the releases page you can proceed to install the package.

```sh
# Replace the filename here with the name of the file you obtained from the releases page.
sudo apt-get install "./inspircd_[VERSION]_amd64.deb"
```

The package should now be installed and you can proceed to set up your [configuration](/3/configuration).

Once you have configured your server you can start it by running `systemctl start inspircd.service` or, if you prefer not to use systemd, by running `inspircd`.

### Where does this package store important files?

Configuration files are stored in `/etc/inspircd`.

Data files are stored in `/var/lib/inspircd`.

Log files are stored in `/var/log/inspircd`.
