<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/ZLINE <ipaddr> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then bans an IP address or CIDR range from connecting to the network. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the Z-line will be permanent.

Otherwise, if just `<ipaddr>` is specified, removes a network-wide ban on an IP address.

This command is only usable by server operators with ZLINE in one of their `<class>` blocks.

#### Example Usage

Z-lines 192.0.2.1 for one day with the reason "Testing":

```plaintext
/ZLINE 192.0.2.1 1d :Testing
```

Z-lines 192.0.2.0/24 for one day with the reason "Testing":

```plaintext
/ZLINE 192.0.2.0/24 86400 :Testing
```

Removes a Z-line on 192.0.2.1:

```plaintext
/ZLINE 192.0.2.1
```
