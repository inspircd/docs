---
title: v3 Module Manager
---

## Managing third-party modules with Module Manager

### Summary

The InspIRCd community has created many third-party modules and Module Manager is an easy-to-use helper script for finding and installing those modules.

### Usage

To see the list of Module Manager subcommands you can run execute `./modulemanager help` in the root of the InspIRCd source directory.

#### Installing a module

To install a module use the `./modulemanager install <name>` command. The module will be downloaded and placed into the `./src/modules` directory. You can then build and install the module by running `make install`.

#### Upgrading modules

To upgrade modules use the `./modulemanager upgrade` command. All outdated modules will be updated and you can rebuild them as mentioned above.

#### Listing available modules

The `./modulemanager list` command shows the names, versions, and descriptions of all available modules.

### Other Methods

If for some reason you are unable to use the Module Manager you can download and install modules manually using the following steps:

1. Download the module you wish to install from [the inspircd-contrib repository on GitHub](https://github.com/inspircd/inspircd-contrib).

2. Move it to the ./src/modules directory.

3. Run `make install` to build and install the module.
