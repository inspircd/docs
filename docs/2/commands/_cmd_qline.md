<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/QLINE <nick> [<duration> <reason>]`

If `<duration>` and `<reason>` are specified then prevents a nickname from being used. The `<duration>` may be specified as a number of seconds or as a duration in the format 1y2w3d4h5m6s. If the duration is zero then the Q-line will be permanent.

Otherwise, if just `<nick>` is specified, removes a reservation on a nickname.

This command is only usable by server operators with QLINE in one of their `<class>` blocks.

#### Example Usage

Q-lines Adam for one day with the reason "Testing":

```plaintext
/QLINE Adam 1d :Testing
```

Q-lines Sadie for one day with the reason "Testing":

```plaintext
/QLINE Sadie 86400 :Testing
```

Removes an Q-line on Adam:

```plaintext
/QLINE Adam
```
