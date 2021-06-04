---
title: "Module Details: sslrehashsignal (v3)"
---

## The "sslrehashsignal" Module

!!! note ""
    This module depends on UNIX-specific features and must be manually enabled at compile time.

    If you are building on a UNIX platform you can enable this module using the following command:

    <pre><code>./configure --enable-extras sslrehashsignal</code></pre>

### Description

This module allows the `SIGUSR1` signal to be sent to the server to reload TLS (SSL) certificates.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="sslrehashsignal">
```

This module requires no other configuration.

### Signals

Name    | Description
------- | -----------
SIGUSR1 | Reloads the server's TLS (SSL) certificates.


### Special Notes

If you are using an automated tool such as Certbot for renewing your certificates you may find it useful to use the following script as a deploy hook:

```sh
#!/bin/sh
set -e

# The location your renewal tool places your certificates.
CERT_DIR="/var/lib/dehydrated/certs/irc.example.com"

# The location of the InspIRCd config directory.
INSPIRCD_CONFIG_DIR="/etc/inspircd"

# The location of the InspIRCd pid file.
INSPIRCD_PID_FILE="/var/lib/inspircd.pid"

# The user:group that InspIRCd runs as.
INSPIRCD_OWNER="inspircd:inspircd"

if [ -e ${CERT_DIR} -a -e ${INSPIRCD_CONFIG_DIR} ]
then
	cp "${CERT_DIR}/fullchain.pem" "${INSPIRCD_CONFIG_DIR}/cert.pem"
	cp "${CERT_DIR}/privkey.pem" "${INSPIRCD_CONFIG_DIR}/key.pem"
	chown ${INSPIRCD_OWNER} "${INSPIRCD_CONFIG_DIR}/cert.pem" "${INSPIRCD_CONFIG_DIR}/key.pem"
	if [ -e ${INSPIRCD_PID_FILE} ]
	then
		kill -USR1 `cat ${INSPIRCD_PID_FILE}`
	fi
fi
```
