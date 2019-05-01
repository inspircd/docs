<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/WHOIS <nick1>[,<nick1>]  <nick2>[,<nick2>]`

Requests information about users who are currently connected with the specified nicks:

If the `<nick2>` parameter is specified for a user then remote information will be fetched about the user if they are not on the local server.

#### Example Usage

Requests locally available information about Adam:

```plaintext
/WHOIS Adam
```

Requests remotely available information about Adam:

```plaintext
/WHOIS Adam Adam
```

Requests locally available information about Adam and Sadie:

```plaintext
/WHOIS Adam,Sadie
```

Requests remotely available information about Adam and Sadie:

```plaintext
/WHOIS Adam,Sadie Adam,Sadie
```
