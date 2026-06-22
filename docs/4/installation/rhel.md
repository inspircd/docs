---
title: v4 RHEL Installation
packages:
    RHEL 8: inspircd-{{ config.extra.releases.v4 }}-1.el8.x86_64.rpm
    RHEL 9: inspircd-{{ config.extra.releases.v4 }}-1.el9.x86_64.rpm
    RHEL 10: inspircd-{{ config.extra.releases.v4 }}-1.el10.x86_64.rpm
---

## Installing InspIRCd 4 using the RHEL package

An official package for RHEL is maintained by the InspIRCd Team. You can download this from [the releases page](https://github.com/inspircd/inspircd/releases/v{{ config.extra.releases.v4 }}).

### What systems are supported by this package?

This package can be installed on all x86-64 systems running:

{% for package in page.packages %}
* {{ package }}
{% endfor %}

You can also install the package on RHEL rebuilds like AlmaLinux and Rocky Linux.

### How do I install this package?

#### Download the package

To start, download the RPM package to your server using Wget. If you do not have Wget installed you can install it using `sudo dnf install wget`.

```sh
{%- for package in page.packages %}
# Use this package on {{ package }} and rebuilds.
wget "https://github.com/inspircd/inspircd/releases/download/v{{ config.extra.releases.v4 }}/{{ page.packages[package] }}"{% if not loop.last %}
{% endif %}
{%- endfor %}
```

#### Validate the package integrity (optional)

If you want to validate the integrity of the downloaded package, SHA-256 checksums are available on the releases page. If you have `jq` installed you can automate fetching the release checksum using:

```sh
{%- for package in page.packages %}
# Fetches the expected checksum of the {{ package  }} package
wget --quiet --output-document - "https://api.github.com/repos/inspircd/inspircd/releases/tags/v{{ config.extra.releases.v4 }}" | jq --raw-output 'first(.assets[] | select(.name == "{{ page.packages[package] }}").digest | ltrimstr("sha256:"))'{% if not loop.last %}
{% endif %}
{%- endfor %}
```

Once you have obtained the expected checksum for the package you can validate the integrity of the downloaded package by comparing it to the actual checksum from `sha256sum`.

```sh
{%- for package in page.packages %}
# Calculates the actual checksum of the {{ package }} package
sha256sum "./{{ page.packages[package] }}"{% if not loop.last %}
{% endif %}
{%- endfor %}
```

If the checksum matches the one specified on the releases page you can proceed to install the package. Otherwise, you should redownload the package.

#### Install the package

To install the package pass the filename to `dnf install`. If you want to check what extra packages will be installed first you can use `dnf deplist` instead.


```sh
{%- for package in page.packages %}
# Installs the package on {{ package }}
sudo dnf install "./{{ page.packages[package] }}"{% if not loop.last %}
{% endif %}
{%- endfor %}
```

#### Configuration

The package should now be installed and you can proceed to set up your [configuration](/4/configuration).

Once you have configured your server you can start it by running `systemctl start inspircd.service` or, if you prefer not to use systemd, by running `sudo -g inspircd -u inspircd inspircd`.

### Where does this package store important files?

Configuration files are stored in `/etc/inspircd`.

Data files are stored in `/var/lib/inspircd`.

Log files are stored in `/var/log/inspircd`.
