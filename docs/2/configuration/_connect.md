<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<connect>`

The `<connect>` tag defines a class that users can be filtered into when they connect to the server. This tag can be defined as many times as required.

Name        | Type    | Default Value           | Description
----------- | ------- | ----------------------- | -----------
name        | Text    | *None*                  | If defined then the name of this connect class.
allow       | Text    | *None*                  | A glob pattern or CIDR range for an IP address which is allowed to connect to the server. If this is defined then `deny` (below) MUST NOT be defined.
deny        | Text    | *None*                  | A glob pattern or CIDR range for an IP address which is banned from connecting to the server. If this is defined then `allow` (below) MUST NOT be defined.
commandrate | Number  | *None*                  | The number of millicommands per second that a user can execute.
fakelag     | Boolean | Yes                     | Whether users should have their input/output delayed when they reach a soft limit rather than being killed.
globalmax   | Number  | *None*                  | The maximum number of users who can exist on the entire network from the range specified in the allow field.
hardsendq   | Number  | 1048576                 | The maximum amount of data allowed in a user's send queue before it is killed.
limit       | Number  | *None*                  | The maximum number of users who can be in this connect class.
localmax    | Number  | *None*                  | The maximum number of users who can exist on the local server from the range specified in the allow field.
maxchans    | Number  | *None*                  | If defined then the maximum number of channels that a user in this class can be in.
maxconnwarn | Boolean | No                      | Whether to send a server notice when a connect class limit is reached.
parent      | Text    | *None*                  | If defined then the name of the class to inherit most *core* settings from.
password    | Text    | *None*                  | *Not inherited from the parent block!*  The password that the user must send to be put into this connect class.
pingfreq    | Number  | 120                     | The number of seconds this client can be idle for before sending it a `PING` message.
port        | Number  | *None*                  | *Not inherited from the parent block!* The port on which a client must be connecting to be put into this connect class.
reason      | Number  | Unauthorised connection | *Not inherited from the parent block!* If `<connect:deny>` is set then the reason to give when disconnecting a user.
recvq       | Number  | 4096                    | The maximum amount of data allowed in a user's receive queue before it is killed.
registered  | Boolean | *None*                  | *Not inherited from the parent block!* If defined then whether this connect class matches a user in registration or a client that has completed registration.
softsendq   | Number  | 4096                    | The maximum number of bytes of data that can be in a user's send queue before the server stops processing their input to allow the send queue to drain.
threshold   | Number  | 10                      | The maximum amount of penalty that a user can have before being fakelagged or killed if fakelag is turned off.
timeout     | Number  | 90                      | The number of seconds after which an unregistered user is timed out.

#### Example Usage

Denies connections to clients connecting from 3ffe::0/32:

```xml
<connect name="6bone"
         deny="3ffe::0/32"
         reason="The 6bone address space is deprecated">
```

Defines a general connect class and then a SSL-only connect class that inherits from it:

```xml
<connect name="Secure"
         parent="Main"
         port="6697">

<connect name="Main"
         allow="*"
         commandrate="1000"
         fakelag="on"
         globalmax="3"
         hardsendq="1M"
         limit="5000"
         localmax="3"
         maxchans="30"
         maxconnwarn="no"
         pingfreq="120"
         recvq="8K"
         softsendq="8192"
         threshold="10"
         timeout="10">
```
