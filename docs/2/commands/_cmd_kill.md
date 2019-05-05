<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/KILL <nick>[,<nick>]+ <reason>`

Forcibly disconnects one or more specified users from the network with the specified reason.

This command is only usable by server operators with KILL in one of their `<class>` blocks.

#### Example Usage

Forcibly disconnects opal from the network:

```plaintext
/KILL opal :Disruptive behaviour is not allowed
```

Forcibly disconnects Soni and opal from the network:

```plaintext
/KILL Soni,opal :Disruptive behaviour is not allowed
```
