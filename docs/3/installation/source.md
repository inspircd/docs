---
title: Source Installation
---

## Installing InspIRCd 3 from source

If there is no official InspIRCd package for your system and you don't want to use Docker you can build from source.

### What systems can InspIRCd be built on?

InspIRCd can be built on on the following platforms:

- Most recent BSD variants using the Clang or GCC compilers and the GNU toolchain (Make, etc).

- Most recent Linux distributions using the Clang or GCC compilers and the GNU toolchain.

- The most recent three major releases of macOS using the AppleClang, Clang, or GCC (*not* LLVM-GCC) compilers and the GNU toolchain.

- Windows 7 or newer using the MSVC 14 (Visual Studio 2015) compiler and CMake 2.8 or newer.

Alternate platforms and toolchains may also work but are not officially supported by the InspIRCd team. Generally speaking if you are using a reasonably modern UNIX-like system you should be able to build InspIRCd on it.

### How do I install from source?

#### Dependencies

In order to build from source you will need to have the development tools for your system installed. On Debian-based systems this is the `build-essential` package and on RHEL-based systems this is the `Development Tools` package group.

If you want to use any modules with third-party dependencies you should have pkg-config and the development headers for the dependency installed.

Once you have dependencies installed you need to download the source code. You can choose between building the most recent release or, if you enjoy living on the edge, the latest code committed to Git.

#### Release Tarball

To download the most recent release tarball you will need to have a download tool such as cURL or Wget installed. You can install one of these from your system's package manager. Once you have a download tool installed you can download the most recent release tarball from [the releases page](https://github.com/inspircd/inspircd/releases/latest).

```sh
# You can replace `wget` with `curl --remote-name` if using cURL.
wget "https://github.com/inspircd/inspircd/archive/[VERSION].tar.gz"
```

Once the archive has downloaded you can unpack it using an archival tool such as GNU Tar.

```sh
tar -xvf "./inspircd-[VERSION].tar.gz"
```

A copy of the latest InspIRCd source code will now exist in the `inspircd-[VERSION]` directory.

#### Git

To download the most recent code committed to Git you will need to have Git installed. You can install this from your system's package manager. Once you have Git installed you can download the latest source with the following command:

```sh
git clone --branch insp3 "https://github.com/inspircd/inspircd.git"
```

A copy of the latest InspIRCd source code will now exist in the `inspircd` directory.

#### Configuration

Execute the `./configure` script from the directory which contains the InspIRCd sources from the previous step. This will start an interactive wizard to help you configure your installation.

You will initially be prompted to enter the location which you want the InspIRCd files to be copied to. The default is to install into a self-contained folder in your home directory but you can do a system-wide install if you really must.

After you have configured the paths you will be asked a question about whether you want to use epoll/kqueue/poll/ports. You can almost always leave this as the default value as the most optimal socket engine will be selected automatically.

If you have installed the development for either GnuTLS or OpenSSL you will now be asked if you want to build them. If available you should always say yes but if you don't you can enable them later with `./configure --enable-gnutls` or `./configure --enable-openssl`. After doing this it will prompt you to enable a self-signed certificate for your server.

Finally, you will be asked if you want to check for updates to third-party modules. If you are installing the first time you don't need to do this but if you are rerunning `./configure` at a later date you might find it useful to do so.

#### Compilation

You can now run the `make install` command to build InspIRCd from source. On modern hardware this should take less than ten minutes to complete.

Once InspIRCd has been installed you can move on to [configuring it](/3/configuration).
