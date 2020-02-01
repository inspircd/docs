---
title: Module Details (ssl_openssl)
---

{! 2/_support.md !}

## The "ssl_openssl" Module

!!! note ""
    This module depends on a third-party library ([OpenSSL](https://www.openssl.org)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras m_ssl_openssl.cpp</code></pre>

### Description

This module allows TLS-encrypting connections using the [OpenSSL](https://www.openssl.org) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_ssl_openssl.so">
```

#### `<bind>`

This module extends the core `<bind>` tags with the following keys:

Name | Description
---- | -----------
ssl  | *This MUST be set to "openssl" to listen for secure connections with OpenSSL.*

##### Example Usage

Listens for OpenSSL-encrypted IRC connections on the *:6697 endpoint:

```xml
<bind address="*"
      port="6697"
      ...
      ssl="openssl"
      type="clients">
```

Listens for OpenSSL-encrypted server connections on the *:7000 endpoint:

```xml
<bind address="*"
      port="7000"
      ...
      ssl="openssl"
      type="servers">
```

#### `<openssl>`

The `<openssl>` tag defines settings about how the ssl_openssl module should behave. This tag can only be defined once.

Name                 | Type    | Default Value     | Description
-------------------- | ------- | ----------------- | -----------
advertisedports      | Text    | *None*            | *Deprecated!* If defined then a static value to use for the 005 SSL token instead of guessing based on the available listeners.
cafile               | Text    | conf/ca.pem       | The path to the CA in PEM format.
certfile             | Text    | conf/cert.pem     | The path to the certificate in PEM format.
ciphers              | Text    | *None*            | If defined then an [OpenSSL cipher string](https://www.openssl.org/docs/manmaster/man1/ciphers.html).
cipherserverpref     | Boolean | Yes               | Whether the server's cipher preferences should be used instead of the client's.
clientclearoptions   | Number  | 0                 | Raw integer value of options to clear on the client context. Don't change this unless you know what you are doing.
clientsetoptions     | Number  | 0                 | Raw integer value of options to set on the client context. Don't change this unless you know what you are doing.
compression          | Boolean | Yes               | Whether insecure SSL compression is enabled.
customcontextoptions | Boolean | No                | Whether custom context options (\{client,server}\{clear,set}options) are enabled.  Don't change this unless you know what you are doing.
dhfile               | Text    | conf/dhparams.pem | The path to the certificate in PEM format.
ecdhcurve            | Text    | prime256v1        | The ECDH curve. Requires the ssl_openssl module to be built with `INSPIRCD_OPENSSL_ENABLE_ECDH` enabled.
hash                 | Text    | md5               | The hash algorithm used for SSL client fingerprints.
keyfile              | Text    | conf/key.pem      | The path to the private key in PEM format.
renegotiation        | Boolean | Yes               | Whether SSL renegotiation is enabled. This setting requires the ssl_openssl module to be built with `INSPIRCD_OPENSSL_ENABLE_RENEGO_DETECTION` enabled to take effect. Renegotiation is *always* enabled otherwise.
serverclearoptions   | Number  | 0                 | Raw integer value of options to clear on the server context.  Don't change this unless you know what you are doing.
serversetoptions     | Number  | 0                 | Raw integer value of options to set on the server context.  Don't change this unless you know what you are doing.
showports            | Boolean | Yes               | *Deprecated!* Whether to show an IP/port that clients can connect securely on in the 005 message.
sslv3                | Boolean | Yes               | Whether the insecure SSLv3 protocol is enabled.
tlsv1                | Boolean | Yes               | Whether the insecure TLSv1.0 protocol is enabled.

The hash field should be set to one of the following values:

Value  | Description
------ | -----------
md5    | Generates fingerprints using the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm.
sha1   | Generates fingerprints using the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) algorithm.

##### Example Usage

```xml
<openssl advertisedports="192.0.2.1:6697"
         cafile="conf/ca.pem"
         certfile="conf/cert.pem"
         ciphers="DEFAULT"
         cipherserverpref="yes"
         compression="no"
         dhfile="conf/dhparams.pem"
         hash="sha1"
         keyfile="conf/key.pem"
         renegotiation="yes"
         showports="yes"
         sslv3="no"
         tlsv1="no">
```
