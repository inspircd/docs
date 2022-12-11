---
title: v4 Source Installation
---

{! 4/_support.md !}

## Installing InspIRCd 4 from source

If there is no official InspIRCd package for your system and you don't want to use Docker you can build from source.

### What systems can InspIRCd be built on?

InspIRCd can be built on the following platforms:

- Most recent BSD variants using the Clang 5+ or GCC 7+ compilers and the GNU toolchains (Make, etc).

- Most recent Linux distributions using the Clang 5+ or GCC 7+ compilers and the GNU toolchain.

- The most recent three major releases of macOS using the AppleClang 10, Clang 5+, or GCC 7+ (*not* LLVM-GCC) compilers and the GNU toolchain.

Alternate platforms and toolchains may also work but are not officially supported by the InspIRCd team. Generally speaking if you are using a reasonably modern UNIX-like system you should be able to build InspIRCd on it.

If you want to build natively on Windows you should use [the Windows source instructions](/4/installation/windows-source) instead.

### How do I install from source?

#### Dependencies

In order to build from source you will need to have the development tools for your system installed. On Debian-based systems this is the `build-essential` package and on RHEL-based systems this is the `Development Tools` package group.

If you want to use any modules with third-party dependencies you should have pkg-config and the development headers for the dependency installed.

Once you have the dependencies installed you need to download the source code. You can choose between building the most recent release or, if you enjoy living on the edge, the latest code committed to Git.

#### Release Tarball

To download the most recent release tarball you will need to have a download tool such as cURL or Wget installed. You can install one of these from your system's package manager. Once you have a download tool installed you can download the most recent release tarball from [the releases page](https://github.com/inspircd/inspircd/releases/latest).

```sh
# You can replace `wget` with `curl --remote-name` if using cURL.
wget "https://github.com/inspircd/inspircd/archive/refs/tags/[VERSION].tar.gz"
```

Once the archive has downloaded you can unpack it using an archival tool such as GNU Tar.

```sh
tar -xvf "./inspircd-[VERSION].tar.gz"
```

A copy of the latest InspIRCd source code will now exist in the `inspircd-[VERSION]` directory.

#### Git

To download the most recent code committed to Git you will need to have Git installed. You can install this from your system's package manager. Once you have Git installed you can download the latest source with the following command:

```sh
git clone --branch master "https://github.com/inspircd/inspircd.git"
```

A copy of the latest InspIRCd source code will now exist in the `inspircd` directory.

#### Configuration

Execute the `./configure` script from the directory which contains the InspIRCd sources from the previous step. This will start an interactive wizard to help you configure your installation.

You will initially be shown the installation paths that InspIRCd defaults to. The default is to install into a self-contained folder in your home directory but you can change this if you want. If the shown paths are okay then press enter to continue. Otherwise, enter "no", press enter, and fill in the paths that it prompts you for.

After you have configured the paths you will be asked whether you want to enable extra modules automatically based on whether you have the dependencies installed. If you want to do this then press enter to continue. Otherwise, enter "no", press enter, and select the extra modules that you want to use. You can enable modules later using `./configure --enable-extras foo` if you change your mind..

Finally, if you enabled a TLS (SSL) module in the previous step, you will be asked if you want to generate a self-signed certificate for testing purposes. If you want to do this then input "yes", press enter to continue, and fill in the details it prompts you for. Otherwise, press enter to skip this step.

#### Compilation

You can now run the `make install` command to build InspIRCd from source. On modern hardware this should take less than ten minutes to complete.

Once InspIRCd has been installed you can move on to [configuring it](/4/configuration).
