<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/INVITE [[<nick> <channel>] <duration>]`

If `<nick>` and `<channel>` are specified then sends an invite to `<nick>` inviting them to join `<channel>`.

If `<duration>` is specified then the invite will expire after the specified duration passes. This duration can be given as a number of seconds or as a duration in the format 1y2w3d4h5m6s.

Otherwise, if no parameters are specified, then lists the invites which you have been sent that haven't been acted on yet.

#### Example Usage

Lists all pending invites that you have been sent:

```plaintext
/INVITE
```

Invites Sadie to #example:

```plaintext
/INVITE Sadie #example
```

Invites Sadie to #example with a five minute invite expiry:

```plaintext
/INVITE Sadie #example 5m
```

Invites Sadie to #example with a five minute invite expiry:

```plaintext
/INVITE Sadie #example 300
```
