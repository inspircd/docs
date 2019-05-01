<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/ADMIN [<server>]`

Requests the contact details for the administrator of the specified server.

If `<server>` is not specified then it defaults to the local server.

#### Example Usage

Requests the contact details for the local server administrator:

```plaintext
/ADMIN
```

Requests the contact details for the server administrator of irc.example.com:

```plaintext
/ADMIN irc.example.com
```
