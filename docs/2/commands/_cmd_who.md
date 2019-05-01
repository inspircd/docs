<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/WHO <server>|<nick>|<channel>|<host>|<pattern>|<realname>|0 [afhilMmoprt]`

Requests information about users who match the specified condition. One or more of the following flags may be used.

Character | Description
--------- | -----------
a         | Show users who have an away message matching `<pattern>`.
f         | Only show users on remote (far) servers.
h         | Show real hostnames rather than display hostnames (server operators only).
i         | Show users who have an ident (username) matching `<pattern>`.
l         | Only show users on the local server.
M         | Show users who have metadata attached to them with a key name matching `<pattern>` (server operators only).
m         | Show users who have the modes listed in `<pattern>`. The pattern should be in the same format as a mode change e.g. +ow-i (server operators only).
o         | Only show server operators.
p         | Show users who are connected to a port in the `<pattern>` range (server operators only).
r         | Show users who have a real name matching `<pattern>`.
t         | Show users who have connected in the last `<pattern>` seconds.

#### Example Usage

Requests all users on the local server who have an away message matching `*brb`:

```plaintext
/WHO *brb* al
```

Requests all server operators on irc.eu.example.com:

```plaintext
/WHO irc.eu.example.com o
```
