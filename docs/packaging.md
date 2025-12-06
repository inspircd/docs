---
title: Packaging advice
---

## Packaging Advice

### Mailing List

Sadie provides release notifications for package maintainers via email. If you want to be added to Sadie's email list please ask in [#inspircd.dev on Teranova](/support).

### General Advice

Other than to [older branches which are still supported](https://github.com/inspircd/inspircd/security/policy#supported-versions) we generally do not provide non-security patch backports due to it requiring a significant amount of work on our behalf. Please try to avoid backporting patches by only shipping the latest version of InspIRCd wherever possible.

Make sure to pass the `--distribution-label` option with a label that uniquely identifies your specific package and package version (e.g. mewos3.14) to configure when building. This helps us identify distribution packaged versions when people ask for support. See our [official RPM package sources](https://github.com/inspircd/package-builder/blob/v4/rpm/inspircd.spec.in) for an example of how to use this.

Please don't ship preconfigured config files as they become outdated very quickly and result in us having to answer the same support questions over and over again. Our example files should be well documented enough for users to create their own config files.

If you are performing a system-wide install you should use the `--system` option. This will automatically the install paths for use in a system-wide install.

You will probably want to set `INSPIRCD_DISABLE_RPATH=1` in the environment to avoid embedding [runtime paths](https://en.wikipedia.org/wiki/Rpath) into the compiled binaries.

When performing a system-wide build you may be asked to specify a user and group to run as. If you want to run as another user or if your package management system automatically handles changing file permissions then you may want to pass one of the following flag options to `./configure`.

```sh
# If always run as root.
./configure --gid 0 --uid 0 ...

# If running as another user.
./configure --gid $(id -g) --uid $(id -u) ...

# If you want to configure ownership yourself.
./configure --disable-ownership ...
```

## System Libraries

If your distribution's policies require building against specific versions of libraries rather than using our vendored versions you can specify some environment variables to enable this (requires InspIRCd 4.8.0 or newer):

```sh
# Build against the nodejs http_parser library from the system.
export SYSTEM_HTTP_PARSER=1

# Build against the UTF8-CPP library from the system.
export SYSTEM_UTFCPP=1
```

### Extra Modules

By default the extra modules for which the dependencies are installed are automatically enabled when you run `./configure`. To override this you can pass `--disable-auto-extras` option to your initial `./configure` run and then execute `./configure` again with the `--enable-extras` option followed by a space delimited string of the list of modules you want to enable as shown below.

```sh
./configure --disable-auto-extras ...
./configure --enable-extras "ldap regex_posix sslrehashsignal"`
```

It is recommended that you ship as many extra modules as possible but due to GPLv2 conflicts not all modules can legally be shipped in binary form. Below is a list of the modules shipped with the latest version and their legal status.

Module                                        | Library                         | License          | GPLv2 compatible?
--------------------------------------------- | ------------------------------- | ---------------- | -----------------
[argon2](/4/modules/argon2)                   | libargon2                       | Apache 2.0 / CC0 | Yes
[geo_maxmind](/4/modules/geo_maxmind)         | libmaxminddb                    | Apache 2.0       | **No**
[ldap](/4/modules/ldap)                       | libldap2                        | BSD-style        | Yes
[log_json](/4/modules/log_json)               | yyjson / RapidJSON (deprecated) | MIT              | Yes
[log_syslog](/4/modules/log_syslog)           | *C stdlib*                      | *Depends*        | *Maybe*
[mysql](/4/modules/mysql)                     | libmysqlclient                  | GPLv2            | Yes
[pgsql](/4/modules/pgsql)                     | libpq                           | MIT              | Yes
[regex_pcre2](/4/modules/regex_pcre2)         | libpcre2                        | BSD 3-Clause     | Yes
[regex_posix](/4/modules/regex_posix)         | *C stdlib*                      | *Depends*        | *Maybe*
[regex_re2](/4/modules/regex_re2)             | libre2                          | BSD 3-Clause     | Yes
[regex_tre](/4/modules/regex_tre)             | libtre                          | BSD 2-Clause     | Yes
[sqlite3](/4/modules/sqlite3)                 | libsqlite3                      | Public Domain    | Yes
[ssl_gnutls](/4/modules/ssl_gnutls)           | libgnutls                       | LGPL2.1+         | Yes
[ssl_openssl](/4/modules/ssl_openssl)         | libcrypto libssl                | Apache 2.0       | **No**
[sslrehashsignal](/4/modules/sslrehashsignal) | *C stdlib*                      | *Depends*        | *Maybe*

### Patches

Please don't make major changes to InspIRCd when packaging because it makes it really hard for us to handle support and tracing bugs. Distributions doing this in the past has [led to them introducing security vulnerabilities](https://nvd.nist.gov/vuln/detail/CVE-2015-6674) which put users at risk for *years*.

If you have any minor patches which are relevant to people outside of your distribution then please upstream them. We are happy to receive and review patches that improve InspIRCd for everyone.
