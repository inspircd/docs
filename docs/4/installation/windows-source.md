---
title: v4 Windows Source Installation
---

{! 4/_support.md !}

## Installing InspIRCd 4 from source on Windows

If you want to build InspIRCd with contrib modules or non-included extra modules you can build from source.

### What systems can InspIRCd be built on?

InspIRCd can be built on Windows 10 build 17061 or newer using the MSVC 19.15+ (Visual Studio 15.8 2017) compiler and CMake 3.20 or newer. Some extra modules may require newer versions in order to build.

### How do I install from source?

#### Dependencies

In order to build from source you will need to have the following development tools installed on your system:

0. [The Windows SDK for your system](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/).

0. [Visual Studio 15.8 2017 or newer](https://visualstudio.microsoft.com/downloads/).

0. [CMake 3.20 or newer](https://cmake.org/download/).

0. [Conan](https://conan.io/downloads.html).

0. [NSIS](https://nsis.sourceforge.io/Download).

Once you have the development tools installed you need to download the source code. You can choose between building the most recent release or, if you enjoy living on the edge, the latest code committed to Git.

#### Release Tarball

To download the most recent release tarball you will need to have access to a PowerShell terminal.

```sh
(New-Object System.Net.WebClient).DownloadFile("https://github.com/inspircd/inspircd/archive/refs/tags/[VERSION].zip" ".\inspircd-[VERSION].zip"
```

Once the archive has downloaded you can unpack it.

```sh
Expand-Archive -Path ".\inspircd-[VERSION].zip" -DestinationPath ".\inspircd-[VERSION]"
```

A copy of the latest InspIRCd source code will now exist in the `inspircd-[VERSION]` directory.

#### Git

To download the most recent code committed to Git you will need to have Git installed. You can install this from [the Git website](https://git-scm.com/download/win). Once you have Git installed you can download the latest source with the following command:

```sh
git clone --branch master "https://github.com/inspircd/inspircd.git"
```

A copy of the latest InspIRCd source code will now exist in the `inspircd` directory.

#### Compilation

First you will need to install the extra module dependencies. If you want to enable any modules which aren't built by default for legal reasons you should uncomment their dependencies in `conanfile.txt` now. Once you have done this you should install the dependencies.

```sh
cd "[SOURCE]\win\build"
conan install .. --build=missing
```

Once Conan has finished installing all of the third party dependencies you should run CMake to generate the project files.

```sh
cmake .. -A x64 -D CMAKE_BUILD_TYPE=Release
```

When CMake finishes you you can now run the `msbuild PACKAGE.vcxproj /P:Configuration=Release /P:Platform=x64 /VERBOSITY:MINIMAL` command to build InspIRCd from source. On modern hardware this should take less than ten minutes to complete. If you prefer you can also just open InspIRCd.sln in Visual Studio and build the PACKAGE target.

Once InspIRCd has been built you can run the installer from the build directory and move on to [configuring it](/4/configuration).
