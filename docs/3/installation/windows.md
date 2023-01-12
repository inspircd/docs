---
title: v3 Windows Installation
---

## Installing InspIRCd 3 using the Windows package

An official package for Windows is maintained by the InspIRCd Team. You can download this from [the releases page](https://github.com/inspircd/inspircd/releases/latest).

### What systems are supported by this package?

This package can be installed on all x86-64 systems running Windows 8 or newer.

### How do I install this package?

First, download the package installer. If you have access to a PowerShell terminal you can do this using:

```sh
# Replace the URL here with the URL you obtained from the releases page.
(New-Object System.Net.WebClient).DownloadFile("https://github.com/inspircd/inspircd/releases/download/[VERSION]/InspIRCd-[VERSION].exe", "InspIRCd-[VERSION].exe")
```

Once the package installer has downloaded you can either double click it to install or run the following command:

```sh
# Replace the filename here with the name of the file you obtained from the releases page.
Start-Process ".\InspIRCd-[VERSION].exe"
```

### Where does this package store important files?

By default the package is installed to `C:\Program Files\InspIRCd`. All paths listed below are relative to this base directory.

Configuration files are stored in `.\conf`.

Data files are stored in `.\data`.

Log files are stored in `.\logs`.
