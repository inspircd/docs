<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/REHASH <server>|-<type>`

Reloads the server configuration.

If `<type>` is specified then a specific module is rehashed on the local server.

If `<server>` is specified then the specified server's configuration is reloaded.

Otherwise, if no parameters are specified, the local server's configuration is reloaded.

This command is only usable by server operators with REHASH in one of their `<class>` blocks.

#### Example Usage

Reloads the local server configuration:

```plaintext
/REHASH
```

Reloads the server configuration for remote.example.com:

```plaintext
/REHASH remote.example.com
```

Reloads the TLS (SSL) certificates (requires [the sslinfo module](/3/modules/sslinfo)):

```plaintext
/REHASH -ssl
```
