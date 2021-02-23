<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/STATS <character> [<server>]`

Requests the specified server statistics.

If `<server>` is specified then requests the server statistics for the specified server.

Otherwise, requests the server statistics for the local server.

#### Statistics Characters

This page only lists core statistics characters. Modules which provide additional characters will list the characters on the specific module page.

Character | Description
--------- | -----------
e         | Show E-lines (global user@host ban exceptions).
g         | Show G-lines (global user@host bans).
k         | Show K-lines (local user@host bans).
q         | Show Q-lines (global nick bans).
Z         | Show Z-lines (global IP mask bans).
i         | Show connect class permissions.
Y         | Show connection classes.
l         | Show all client connections with information (sendq, commands, bytes, time connected).
L         | Show all client connections with information and IP address.
m         | Show command statistics, number of times commands have been used.
o         | Show a list of all valid oper usernames and hostmasks.
O         | Show opertypes and the allowed user and channel modes it can set.
p         | Show open client ports, and the port type (ssl, plaintext, etc).
P         | Show online opers and their idle times.
u         | Show server uptime.
z         | Show memory usage statistics.
E         | Show socket engine events.
T         | Show bandwidth/socket statistics.
U         | Show U-lined servers.

#### Example Usage

Requests `p` (ports) statistics for the local server:

```plaintext
/STATS p
```

Requests `p` (ports) statistics for the remote server irc.eu.example.com:

```plaintext
/STATS p irc.eu.example.com
```
