---
title: "Module Details: ssl_gnutls (v3)"
---

## The "ssl_gnutls" Module

!!! note ""
    This module depends on a third-party library ([GnuTLS](https://gnutls.org)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_ssl_gnutls.cpp</code></pre>

### Description

This module allows TLS (SSL) encrypted connections using the [GnuTLS](https://gnutls.org) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ssl_gnutls">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following keys:

Name | Description
---- | -----------
ssl  | *This MUST be set to the name of a GnuTLS TLS (SSL) profile to listen for secure connections with GnuTLS.*

##### Example Usage

Listens for GnuTLS encrypted IRC connections on the *:6697 endpoint:

```xml
<bind address="*"
      port="6697"
      ...
      ssl="gnutls"
      type="clients">
```

Listens for GnuTLS encrypted server connections on the *:7000 endpoint:

```xml
<bind address="*"
      port="7000"
      ...
      ssl="gnutls"
      type="servers">
```

#### `<sslprofile>`

The `<sslprofile>` tag defines a TLS (SSL) profile for sockets to use. This tag can be defined as many times as required.

If no `<sslprofile>` tags are defined a default profile named `gnutls` will be created. This profile will use the contents of the deprecated `<gnutls>` tag if one has been defined.

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
            cafile="ca.pem"
            certfile="cert.pem"
            crlfile="crl.pem"
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
