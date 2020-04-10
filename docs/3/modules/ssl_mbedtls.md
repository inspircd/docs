---
title: Module Details (ssl_mbedtls)
---

## The "ssl_mbedtls" Module

!!! note ""
    This module depends on a third-party library ([mbedTLS](https://tls.mbed.org)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_ssl_mbedtls.cpp</code></pre>

### Description

This module allows TLS (SSL) encrypted connections using the [mbedTLS](https://tls.mbed.org) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ssl_mbedtls">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following keys:

Name | Description
---- | -----------
ssl  | *This MUST be set to the name of a mbedTLS TLS (SSL) profile to listen for secure connections with mbedTLS.*

##### Example Usage

Listens for mbedTLS encrypted IRC connections on the *:6697 endpoint:

```xml
<bind address="*"
      port="6697"
      ...
      ssl="mbedtls"
      type="clients">
```

Listens for mbedTLS encrypted server connections on the *:7000 endpoint:

```xml
<bind address="*"
      port="7000"
      ...
      ssl="mbedtls"
      type="servers">
```

#### `<sslprofile>`

The `<sslprofile>` tag defines a TLS (SSL) profile for sockets to use. This tag can be defined as many times as required.

If no `<sslprofile>` tags are defined a default profile named `mbedtls` will be created. This profile will use the contents of the deprecated `<mbedtls>` tag if one has been defined.

Name              | Type    | Default Value | Description
----------------- | ------- | ------------- | -----------
name              | Text    | *None*        | **Required!** The name of this TLS (SSL) profile. This is used in `<bind:ssl>` for incoming connections and `<link:ssl>` for outgoing server connections.
provider          | Text    | *None*        | **Required!** *This MUST be set to "mbedtls" to use the mbedTLS library.*
cafile            | Text    | *None*        | If defined then the path to the CA in PEM format.
certfile          | Text    | cert.pem      | The path to the certificate in PEM format.
ciphersuites      | Text    | *None*        | If defined then a colon-delimited list of [mbedTLS ciphersuites](https://tls.mbed.org/supported-ssl-ciphersuites).
crlfile           | Text    | *None*        | If defined then the path to the CRL in PEM format.
curves            | Text    | *None*        | If defined then a colon-delimited list of curves for use with ECDHE.
dhfile            | Text    | dhparams.pem  | The path to the DH parameters in PEM format.
hash              | Text    | sha256        | The hash algorithm used for TLS (SSL) client fingerprints.
keyfile           | Text    | key.pem       | The path to the private key in PEM format.
maxver            | Number  | *None*        | If defined then the maximum version of TLS (SSL) to use.
mindhbits         | Number  | 2048          | The minimum number of bits of the DH parameters file to use in an Diffie-Hellman key exchange.
minver            | Number  | *None*        | If defined then the minimum version of TLS (SSL) to use.
outrecsize        | Number  | 2048          | The maximum size of an outgoing mbedTLS record.
requestclientcert | Boolean | Yes           | Whether to request a TLS (SSL) certificate from clients.

The hash field should be set to one of the values shown [in the mbedTLS MD documentation](https://tls.mbed.org/api/group__hashing__module.html).

##### Example Usage

```xml
<sslprofile name="Clients"
            provider="mbedtls"
            cafile="ca.pem"
            certfile="cert.pem"
            crlfile="crl.pem"
            dhfile="dhparams.pem"
            hash="sha256"
            keyfile="key.pem"
            mindhbits="2048"
            outrecsize="2048"
            requestclientcert="yes">
```
