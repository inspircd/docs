---
title: v4 Debian Installation
packages:
    Debian 12 (Bookworm): inspircd_{{ config.extra.releases.v4 }}.deb12u1_amd64.deb
    Debian 13 (Trixie): inspircd_{{ config.extra.releases.v4 }}.deb13u1_amd64.deb
    Debian 14 (Forky): inspircd_{{ config.extra.releases.v4 }}.deb14u1_amd64.deb
---

## Installing InspIRCd 4 using the Debian package

An official package for Debian is maintained by the InspIRCd Team. You can download this from [the releases page](https://github.com/inspircd/inspircd/releases/latest).

### What systems are supported by this package?

This package can be installed on all x86-64 systems running:

{% for package in page.packages %}
* {{ package }}
{% endfor %}

### How do I install this package?

If you've previously installed InspIRCd from the Debian repositories you should start by backing up your config and data directories and removing the existing package.

```sh
cp -r /etc/inspircd conf
cp -r /var/run/inspircd data
sudo apt-get purge inspircd
```

Then, download the .deb package to your server using Wget. If you do not have Wget installed you can install it using `sudo apt-get install wget`.

```sh
{%- for package in page.packages %}
# Use this package on {{ package }}
wget "https://github.com/inspircd/inspircd/releases/download/v{{ config.extra.releases.v4 }}/{{ page.packages[package] }}"{% if not loop.last %}
{% endif %}
{%- endfor %}
```

Once the package has downloaded ensure that the file has not been corrupted during download by running `sha256sum` and comparing its output to the hash specified on the releases page.

```sh
# Use the appropriate command for your distribution.
{%- for package in page.packages %}
sha256sum "./{{ page.packages[package] }}" # {{ package }}
{%- endfor %}
```

If the hash matches the one specified on the releases page you can proceed to install the package.

```sh
# Use the appropriate command for your distribution.
{%- for package in page.packages %}
sudo apt-get install "./{{ page.packages[package] }}" # {{ package }}
{%- endfor %}
```

The package should now be installed and you can proceed to set up your [configuration](/4/configuration).

Once you have configured your server you can start it by running `systemctl start inspircd.service` or, if you prefer not to use systemd, by running `sudo -g irc -u irc inspircd`.

### Where does this package store important files?

Configuration files are stored in `/etc/inspircd`.

Data files are stored in `/var/lib/inspircd`.

Log files are stored in `/var/log/inspircd`.
