<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/NOTICE <target>[,<target>]+ <message>`

Sends a notice to the targets specified in `<target>`. These targets can be a channel, a user, or a server mask (requires the users/mass-message server operator privilege).

#### Example Usage

Sends a notice to #channel saying "Hello!":

```plaintext
/NOTICE #channel :Hello!
```

Sends a notice to Sadie saying "Hello!":

```plaintext
/NOTICE Sadie :Hello!
```

Sends a notice to all users on servers matching the glob pattern `*.example.com` saying "Hello!":

```plaintext
/NOTICE $*.example.com :Hello!
```
