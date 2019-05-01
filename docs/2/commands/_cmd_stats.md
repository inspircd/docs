<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/STATS <character> [<server>]`

Requests the specified server statistics.

If `<server>` is specified then requests the server statistics for the specified server.

Otherwise, requests the server statistics for the local server.

#### Example Usage

Requests `p` (ports) statistics for the local server:

```plaintext
/STATS p
````

Requests `p` (ports) statistics for the remote server irc.eu.example.com:

```plaintext
/STATS p irc.eu.example.com
```
