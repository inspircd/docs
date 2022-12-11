<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

The following TLS (SSL) modules are included with InspIRCd:

Name    | Module                                            | Description
------- | ------------------------------------------------- | -----------
gnutls  | [ssl_gnutls](/{{ version }}/modules/ssl_gnutls)   | Uses the [GnuTLS](https://www.gnutls.org) library.
mbedtls | [ssl_mbedtls](/{{ version }}/modules/ssl_mbedtls) | Uses the [mbedTLS](https://tls.mbed.org) library.
openssl | [ssl_openssl](/{{ version }}/modules/ssl_openssl) | Uses the [OpenSSL](https://www.openssl.org) library.
