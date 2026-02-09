---
title: How to enable TLS (SSL) on your IRC network
---

!!! note ""
    This page is a work in progress. If you find any part of it to be unclear [please open an issue](https://github.com/inspircd/docs/issues/new).

## How to enable TLS (SSL) on your IRC network

### Building a TLS (SSL) module

If you are building from source you will need to enable a TLS (SSL) module. Your current options are:

- [ssl_gnutls](/4/modules/ssl_gnutls) &mdash; requires [the GnuTLS library](https://gnutls.org).
- [ssl_openssl](/4/modules/ssl_openssl) &mdash; requires [the OpenSSL library](https://www.openssl.org).

You will also need to install [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/).

If you have these installed before running `./configure` then the appropriate modules will be enabled automatically. If you are installing after building InspIRCd or they were not automatically enabled for some reason you can build them with `./configure --enable-extras module-name-here` and then `make install`.

### Acquiring a TLS (SSL) certificate and key

If you have not already acquired a TLS (SSL) certificate and key you will need to do so. The recommended method of acquiring these files is an ACME client like [Certbot](https://certbot.eff.org/). You can acquire this from either your system package manager or from pip. See [the Certbot installation instructions](https://certbot.eff.org/instructions?ws=other&os=pip) for more information on how to install and configure Certbot. Alternatives to Certbot include [Dehydrated](https://github.com/dehydrated-io/dehydrated), [acme.sh](https://github.com/acmesh-official/acme.sh), and [many others](https://letsencrypt.org/docs/client-options/).

InspIRCd ships with a script called `deploy-ssl.sh` that you can customise for use as a post-deploy hook to automatically reload your TLS (SSL) profiles when your TLS (SSL) certificate and key are updated. Generally this should not require much tweaking but you should check it just in case. If you are using this you should also make sure that your IRC server has [the sslrehashsignal module](/4/modules/sslrehashsignal) loaded (see below).

### Loading and configuring a TLS (SSL) module

First you must add a `<module>` tag for the name of the TLS (SSL) module you want to use. e.g. to use the `ssl_gnutls` module use `<module name="ssl_gnutls">`.

Once this is added you need to create a TLS (SSL) profile. The syntax of these depend on the TLS (SSL) module that you are using.


- [ssl_gnutls](/4/modules/ssl_gnutls#sslprofile)
- [ssl_openssl](/4/modules/ssl_openssl#sslprofile)

You should note down the value of `<sslprofile:name>` as you will need this in the next step.

Now you have a TLS (SSL) profile you can create [a `<bind>` tag](/4/configuration/#bind) with the `sslprofile` key set to the name you specified in `<sslprofile:name>`. This might vary depending on your configuration but it will look something like this:

```xml
<bind address="*"
      port="6697"
      sslprofile="insert sslprofile name here"
      type="clients">
```

Once you have added this you should restart your server or run `/REHASH` followed by `/REHASH -ssl` as a server operator to reload both your configuration and your TLS (SSL) profiles.

### Diagnosing issues

InspIRCd ships with a tool named `inspircd-testssl` on binary installations and `./tools/testssl` on source installations. You can run this to diagnose any problems with your server configuration.

### Common mistakes

In older versions of InspIRCd you configured TLS (SSL) by setting `<bind:ssl>` to the name of a TLS (SSL) module and configuring the TLS (SSL) certificate and key in `<gnutls>`, `<mbedtls>`, or `<openssl>`. Configuring TLS (SSL) in this way is deprecated and will not work if you have a TLS (SSL) profile defined. It is strongly recommended that you do not use this method as it has been removed in the development branch.

In v3 TLS (SSL) certificates are not reloaded by default on a regular config rehash. You need to use `/REHASH -ssl` to reload TLS (SSL) certificates or load [the sslrehashsignal module](/3/modules/sslrehashsignal) and send SIGUSR1 to your IRC server. You can also set `<gnutls onrehash="yes">`, `<mbedtls onrehash="yes">`. or `<openssl onrehash="yes>` to reload your TLS (SSL) certificates on rehash.

Certbot provides multiple TLS (SSL) certificate files. If you are getting client errors about missing intermediary certificates you have probably used `cert.pem` as your certificate instead of `fullchain.pem`.

InspIRCd ships with the `inspircd-genssl` tool that allows you to generate a self-signed certificate and key. You can use these for testing your server but you should not use them in production as they do not provide much security over using a plaintext connection and do not work with all clients. This tool will be removed in a future release.
