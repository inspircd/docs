<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/PRIVMSG <target>[,<target>]+ <message>`

Sends a message to the targets specified in `<target>`. These targets can be a channel, a user, or a server mask (requires the users/mass-message server operator privilege).

#### Example Usage

Sends a message to #channel saying "Hello!":

```plaintext
/PRIVMSG #channel :Hello!
```

Sends a message to Sadie saying "Hello!":

```plaintext
/PRIVMSG Sadie :Hello!
```

Sends a message to all users on servers matching the glob pattern `*.example.com` saying "Hello!":

```plaintext
/PRIVMSG $*.example.com :Hello!
```
