---
title: "Module Details: ssl_gnutls (v3)"
---

## The "ssl_gnutls" Module

!!! note ""
    This module depends on a third-party library ([GnuTLS](https://gnutls.org)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras ssl_gnutls</code></pre>

### Description

This module allows TLS (SSL) encrypted connections using the [GnuTLS](https://gnutls.org) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ssl_gnutls">
```

#### `<bind>`

This module extends [the core `<bind>` tags](/3/configuration#bind) with the following keys:

Name | Description
---- | -----------
ssl  | *This MUST be set to the name of a GnuTLS TLS (SSL) profile to listen for secure connections with GnuTLS.*

##### Example Usage

Listens for GnuTLS encrypted IRC connections on the *:6697 endpoint with an [SSL profile](#sslprofile) named "Clients":

```xml
<bind address="*"
      port="6697"
      ...
      ssl="Clients"
      type="clients">
```

Listens for GnuTLS encrypted server connections on the *:7000 endpoint with an [SSL profile](#sslprofile) named "Servers":

```xml
<bind address="*"
      port="7000"
      ...
      ssl="Servers"
      type="servers">
```

#### `<sslprofile>`

The `<sslprofile>` tag defines a TLS (SSL) profile for sockets to use. This tag can be defined as many times as required.

If no `<sslprofile>` tags are defined a default profile named `gnutls` will be created. This profile will use the contents of the deprecated `<gnutls>` tag if one has been defined. It is strongly recommended that you do not use this as it will be removed in a future release.

Name              | Type    | Default Value | Description
----------------- | ------- | ------------- | -----------
name              | Text    | *None*        | **Required!** The name of this TLS (SSL) profile. This is used in `<bind:ssl>` for incoming connections and `<link:ssl>` for outgoing server connections.
provider          | Text    | *None*        | **Required!** *This MUST be set to "gnutls" to use the GnuTLS library.*
cafile            | Text    | ca.pem        | The path to the CA in PEM format.
certfile          | Text    | cert.pem      | The path to the certificate in PEM format.
crlfile           | Text    | crl.pem       | The path to the CRL in PEM format.
dhfile            | Text    | dhparams.pem  | The path to the DH parameters in PEM format.
hash              | Text    | md5           | The hash algorithm used for TLS (SSL) client fingerprints.
keyfile           | Text    | key.pem       | The path to the private key in PEM format.
mindhbits         | Number  | 1024          | The minimum number of bits of the DH parameters file to use in an Diffie-Hellman key exchange.
outrecsize        | Number  | 2048          | The maximum size of an outgoing GnuTLS record.
priority          | Text    | NORMAL        | A [GnuTLS priority string](https://gnutls.org/manual/html_node/Priority-Strings.html).
requestclientcert | Boolean | Yes           | Whether to request a TLS (SSL) certificate from clients.
strictpriority    | Boolean | No            | Whether to require that all tokens in the GnuTLS priority string are valid.

The hash field should be set to one of the values shown in `gnutls-cli --list | grep ^Digests:`.

##### Example Usage

```xml
<sslprofile name="Clients"
            provider="gnutls"
            cafile=""
            certfile="cert.pem"
            crlfile=""
            dhfile="dhparams.pem"
            hash="sha256"
            keyfile="key.pem"
            mindhbits="1024"
            outrecsize="2048"
            priority="SECURE192"
            requestclientcert="yes"
            strictpriority="no">
```
## Special Notes

If you are using a CA-provided certificate and key you will also need to provide a DH parameters file. This file can be generated using `certtool --generate-dh-params --sec-param normal --outfile dhparams.pem` and then be placed in your config directory. You may need to use `gnutls-certtool` instead of `certtool` on macOS and `--bits 2048` instead of `--sec-param normal` on GnuTLS 2.x.

SSL profiles are not reloaded as part of a normal rehash. If you wish to reload SSL profiles you should use `/REHASH -ssl` or use [the sslrehashsignal](/3/modules/sslrehashsignal) to allow you to reload SSL profiles by sending SIGUSR1 to the InspIRCd process.

If you are having trouble getting InspIRCd to read your .pem files then check that it has read access to the full path up to the location of them. If you are using a system that uses AppArmor (such as our Debian and Ubuntu packages) you may need to edit the AppArmor profile to allow InspIRCd to read them too.
