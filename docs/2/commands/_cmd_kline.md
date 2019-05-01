<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/KLINE <ident@host> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then bans an ident@host mask from connecting to the local server. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the K-line will be permanent.

Otherwise, if just `<ident@host>` is specified, removes a local server ban on an ident@host mask.

This command is only usable by server operators with KLINE in one of their `<class>` blocks.

#### Example Usage

K-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/KLINE sadie@example.com 1d :Testing
```

K-lines sadie@example.com for one day with the reason "Testing":

```plaintext
/KLINE sadie@example.com 86400 :Testing
```

Removes an K-line on sadie@example.com:

```plaintext
/KLINE sadie@example.com
```
