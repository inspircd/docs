<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/WHO <pattern> [<flags>][%[<fields>[,<querytype>]]] <pattern>`

Requests information about users who match the specified condition.

One or more of the following flags may be used:

Character | Description
--------- | -----------
A         | Show users who have an away message matching `<pattern>`.
a         | Show users who have an account name matching `<pattern>`.
f         | Only show users on remote (far) servers.
h         | Show users who have a hostname matching `<pattern>`. If the 'x' modifier is specified then this will match against the real hostname instead of the display hostname.
i         | Show users who have an IP address matching `<pattern>`.
l         | Only show users on the local server.
m         | Show users who have the modes listed in `<pattern>`. The pattern should be in the same format as a mode change e.g. +ow-i (server operators only).
n         | Show users who have a nickname matching `<pattern>`.
o         | Only show server operators.
p         | Show users who are connected to a port in the `<pattern>` range (server operators only).
r         | Show users who have a real name matching `<pattern>`.
s         | Show users who are on a server with a name matching `<pattern>`. If the 'x' modifier is specified then this will match against the real server name instead of the masked server name.
t         | Show users who have connected in the last `<pattern>` seconds.
u         | Show users who have an ident (username) matching `<pattern>`.
x         | Show sensitive data like real user hostnames and, when hideserver is enabled, real server hostnames.

One or more of the following fields may be used:

Character | Description
--------- | -----------
a         | Include the user's account name in the response.
c         | Include the first common channel name in the response.
d         | Include the user's server distance from you in the response.
f         | Include the user's away status, oper status, and highest channel prefix in the response.
h         | Include the user's hostname in the response. If the 'x' flag was specified then this is the real host rather than the display host.
i         | Include the user's IP address in the response.
l         | Include the user's idle time in the response.
n         | Include the user's nickname in the response.
o         | Include the user's channel operator rank level in the response.
r         | Include the user's real name in the response.
s         | Include the user's server name in the response. If the 'x' flag was specified then this is the real server name rather than the masked servername.
t         | Include the query type in the response.
u         | Include the user's username in the response.

#### Example Usage

Requests all users on the local server who have an away message matching `*brb*`:

```plaintext
/WHO *brb* Al
```

Requests the account name, hostname, and username of Sadie:

```plaintext
/WHO Sadie n%ahu
```
