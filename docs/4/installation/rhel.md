---
title: v4 RHEL Installation
packages:
    RHEL 8: inspircd-{{ config.extra.releases.v4 }}-1.el8.x86_64.rpm
    RHEL 9: inspircd-{{ config.extra.releases.v4 }}-1.el9.x86_64.rpm
    RHEL 10: inspircd-{{ config.extra.releases.v4 }}-1.el10.x86_64.rpm
---

## Installing InspIRCd 4 using the RHEL package

An official package for RHEL is maintained by the InspIRCd Team. You can download this from [the releases page](https://github.com/inspircd/inspircd/releases/latest).

### What systems are supported by this package?

This package can be installed on all x86-64 systems running:

{% for package in page.packages %}
* {{ package }}
{% endfor %}

You can also install the package on RHEL rebuilds like AlmaLinux and Rocky Linux.

### How do I install this package?

First, download the RPM package to your server using Wget. If you do not have Wget installed you can install it using `sudo yum install wget`.

```sh
{%- for package in page.packages %}
# Use this package on {{ package }} and rebuilds.
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
sudo yum install "./{{ page.packages[package] }}" # {{ package }}
{%- endfor %}
```

The package should now be installed and you can proceed to set up your [configuration](/4/configuration).

Once you have configured your server you can start it by running `systemctl start inspircd.service` or, if you prefer not to use systemd, by running `sudo -g inspircd -u inspircd inspircd`.

### Where does this package store important files?

Configuration files are stored in `/etc/inspircd`.

Data files are stored in `/var/lib/inspircd`.

Log files are stored in `/var/log/inspircd`.
