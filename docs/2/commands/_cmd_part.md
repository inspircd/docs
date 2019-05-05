<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/PART <channel>[,<channel>]+ [<reason>]`

Leaves one or more channels. If `<reason>` is specified then it will be used as the message shown when parting.

#### Example Usage

Leaves \#channel with no reason:

```plaintext
/PART #channel
```

Leaves \#channel-one and \#channel-two with no reason:

```plaintext
/PART #channel-one,#channel-two
```

Leaves \#channel with the reason "Going to bed":

```plaintext
/PART #channel :Going to bed
```

Leaves \#channel-one and \#channel-two with the reason "Going to bed":

```plaintext
/PART #channel-one,#channel-two :Going to bed
```
