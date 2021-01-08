<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/WHOIS [<server>] <nick>[,<nick>]+`

Requests information about users who are currently connected with the specified nicks:

If the `<server>` parameter is specified then only one `<nick>` can be specified and remote information will be fetched about the user if they are not on the local server.

#### Example Usage

Requests locally available information about Adam:

```plaintext
/WHOIS Adam
```

Requests remotely available information about Adam by specifying the server they're on:

```plaintext
/WHOIS irc.example.com Adam
```

Requests remotely available information about Adam by repeating their nick:

```plaintext
/WHOIS Adam Adam
```

Requests locally available information about Adam and Sadie:

```plaintext
/WHOIS Adam,Sadie
```
