<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/PONG <cookie> [<server>]`

Responds to a ping from `<server>` with the specified `<cookie>`.  If `<server>` is not specified then it defaults to the local server.

#### Example Usage

Responds to a ping from the local server with the cookie "wibble".

```plaintext
/PONG wibble
```

Responds to a ping from `irc2.example.com` with the cookie "wibble".

```plaintext
/PONG wobble irc2.example.com
```
