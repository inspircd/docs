<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/KICK <channel> <nick>[,<nick>]+ [<reason>]`

Kicks one or more users from the specified channel.

You must at least a channel half-operator, or channel operator if that channel mode is not enabled, and must be an equal or higher rank to the user you are kicking.

#### Example Usage

Kicks Soni from #channel with no reason:

```plaintext
/KICK #channel Soni
```

Kicks Soni from #channel:

```plaintext
/KICK #channel Soni :Disruptive behaviour is not allowed
```

Kicks opal and Soni from #channel:

```plaintext
/KICK #channel opal,Soni :Disruptive behaviour is not allowed
```
