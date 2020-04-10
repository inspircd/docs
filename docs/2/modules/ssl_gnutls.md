---
title: Module Details (ssl_gnutls)
---

{! 2/_support.md !}

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
<module name="m_ssl_gnutls.so">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following keys:

Name | Description
---- | -----------
ssl  | *This MUST be set to "gnutls" to listen for secure connections with GnuTLS.*

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

#### `<gnutls>`

The `<gnutls>` tag defines settings about how the ssl_gnutls module should behave. This tag can only be defined once.

Name            | Type    | Default Value | Description
--------------- | ------- | ------------- | -----------
advertisedports | Text    | *None*        | *Deprecated!* If defined then a static value to use for the 005 SSL token instead of guessing based on the available listeners.
cafile          | Text    | conf/ca.pem   | The path to the CA in PEM format.
certfile        | Text    | conf/cert.pem | The path to the certificate in PEM format.
crlfile         | Text    | conf/crl.pem  | The path to the CRL in PEM format.
dhbits          | Number  | 1024          | The size of DH parameters to generate.
hash            | Text    | md5           | The hash algorithm used for SSL client fingerprints.
keyfile         | Text    | conf/key.pem  | The path to the private key in PEM format.
priority        | Text    | NORMAL        | A [GnuTLS priority string](https://gnutls.org/manual/html_node/Priority-Strings.html).
showports       | Boolean | Yes           | *Deprecated!* Whether to show an IP/port that clients can connect securely on in the 005 message.
starttls        | Boolean | Yes           | *Deprecated!* Whether to enable support for the IRCv3 STARTTLS specification.

The hash field should be set to one of the following values:

Value  | Description
------ | -----------
md5    | Generates fingerprints using the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm.
sha1   | Generates fingerprints using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) algorithm.
sha256 | Generates fingerprints using the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) algorithm. Requires the ssl_gnutls module to be built with `INSPIRCD_GNUTLS_ENABLE_SHA256_FINGERPRINT` enabled.

##### Example Usage

```xml
<gnutls advertisedports="192.0.2.1:6697"
        cafile="conf/ca.pem"
        certfile="conf/cert.pem"
        crlfile="conf/crl.pem"
        dhbits="2048"
        hash="sha1"
        keyfile="conf/key.pem"
        priority="SECURE192"
        showports="yes"
        starttls="yes">
```

### Client Capabilities

Name                                                   | Description
------------------------------------------------------ | -----------
[tls](https://ircv3.net/specs/extensions/tls-3.1.html) | Allows plaintext connections to upgrade to SSL (TLS).
