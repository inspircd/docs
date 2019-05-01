<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/JOIN <channel>[,<channel>]+ [<key>][,[<key>]+]`

Joins one or more channels using the specified channel keys if required.

#### Example Usage

Joins #channel:

```plaintext
/JOIN #channel
```

Joins #channel with the key hunter2:

```plaintext
/JOIN #channel hunter2
```

Joins #channel-one with no key and #channel-two with the key hunter2:

```plaintext
/JOIN #channel-one,#channel-two ,hunter2
```
