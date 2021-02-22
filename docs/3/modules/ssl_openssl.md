---
title: "Module Details: ssl_openssl (v3)"
---

## The "ssl_openssl" Module

!!! note ""
    This module depends on a third-party library ([OpenSSL](https://www.openssl.org)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras ssl_openssl</code></pre>

### Description

This module allows TLS (SSL) encrypted connections using the [OpenSSL](https://www.openssl.org) library.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="ssl_openssl">
```

#### `<bind>`

This module extends [the core `<bind>` tags](/3/configuration#bind) with the following keys:

Name | Description
---- | -----------
ssl  | *This MUST be set to the name of an OpenSSL TLS (SSL) profile to listen for secure connections with OpenSSL.*

##### Example Usage

Listens for OpenSSL encrypted IRC connections on the *:6697 endpoint with an [SSL profile](#sslprofile) named "Clients":

```xml
<bind address="*"
      port="6697"
      ...
      ssl="Clients"
      type="clients">
```

Listens for OpenSSL encrypted server connections on the *:7000 endpoint with an [SSL profile](#sslprofile) named "Servers":

```xml
<bind address="*"
      port="7000"
      ...
      ssl="Servers"
      type="servers">
```

#### `<sslprofile>`

The `<sslprofile>` tag defines a TLS (SSL) profile for sockets to use. This tag can be defined as many times as required.

If no `<sslprofile>` tags are defined a default profile named `openssl` will be created. This profile will use the contents of the deprecated `<openssl>` tag if one has been defined. It is strongly recommended that you do not use this as it will be removed in a future release.

Name               | Type    | Default Value | Description
------------------ | ------- | ------------- | -----------
name               | Text    | *None*        | **Required!** The name of this TLS (SSL) profile. This is used in `<bind:ssl>` for incoming connections and `<link:ssl>` for outgoing server connections.
provider           | Text    | *None*        | **Required!** *This MUST be set to "openssl" to use the OpenSSL library.*
cafile             | Text    | ca.pem        | The path to the CA in PEM format.
certfile           | Text    | cert.pem      | The path to the certificate in PEM format.
ciphers            | Text    | *None*        | If defined then an [OpenSSL cipher string](https://www.openssl.org/docs/manmaster/man1/ciphers.html).
clientclearoptions | Number  | 0             | Raw integer value of options to clear on the client context. Don't change this unless you know what you are doing.
clientsetoptions   | Number  | 0             | Raw integer value of options to set on the client context. Don't change this unless you know what you are doing.
compression        | Boolean | No            | Whether insecure TLS (SSL) compression is enabled.
crlfile            | Text    | *None*        | If defined then the path to the CRL file in PEM format.
crlmode            | Text    | chain         | The mode to use when checking for certificate revocations.
crlpath            | Text    | *None*        | If defined then the path to the CRL directory.
dhfile             | Text    | dhparams.pem  | The path to the certificate in PEM format.
ecdhcurve          | Text    | prime256v1    | The ECDH curve.
hash               | Text    | md5           | The hash algorithm used for TLS (SSL) client fingerprints.
keyfile            | Text    | key.pem       | The path to the private key in PEM format.
renegotiation      | Boolean | No            | Whether insecure TLS (SSL) renegotiation is enabled.
requestclientcert  | Boolean | Yes           | Whether to request a TLS (SSL) certificate from clients.
serverclearoptions | Number  | 0             | Raw integer value of options to clear on the server context.  Don't change this unless you know what you are doing.
serversetoptions   | Number  | 0             | Raw integer value of options to set on the server context.  Don't change this unless you know what you are doing.
tlsv1              | Boolean | No            | Whether the insecure TLSv1.0 protocol is enabled.
tlsv11             | Boolean | Yes           | [**New in v3.2.0!**](/3/change-log/#inspircd-320) Whether the TLSv1.1 protocol is enabled.
tlsv12             | Boolean | Yes           | [**New in v3.2.0!**](/3/change-log/#inspircd-320) Whether the TLSv1.2 protocol is enabled.

The crlmode field should be set to one of the following values:

Value | Description
----- | -----------
chain | Check if any certificate in the chain has been revoked.
leaf  | Only check if the leaf certificate has been revoked.

The hash field should be set to one of the values shown in `openssl list --digest-commands`.

##### Example Usage

```xml
<sslprofile name="Clients"
            provider="openssl"
            cafile="ca.pem"
            certfile="cert.pem"
            crlfile=""
            ciphers="DEFAULT"
            compression="no"
            dhfile="dhparams.pem"
            ecdhcurve="prime256v1"
            hash="sha256"
            keyfile="key.pem"
            renegotiation="no"
            requestclientcert="yes"
            tlsv1="no"
            tlsv11="no"
            tlsv12="yes">
```

## Special Notes

If you are using a CA-provided certificate and key you will also need to provide a DH parameters file. This file can be generated using `openssl dhparam -out dhparams.pem 2048` and then be placed in your config directory.
