<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/GLINE <ident@host> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then bans an ident@host mask from connecting to the network. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the G-line will be permanent.

Otherwise, if just `<ident@host>` is specified, removes a network-wide ban on an ident@host mask.

This command is only usable by server operators with GLINE in one of their `<class>` blocks.

#### Example Usage

G-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/GLINE sadie@example.com 1d :Testing
```

G-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/GLINE sadie@example.com 86400 :Testing
```

Removes an G-line on sadie@example.com:

```plaintext
/GLINE sadie@example.com
```
