<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

The core supplies the following server operator privileges for use in `<class:privs>`.

Name                          | Description
----------------------------- | -----------
channels/auspex               | Allows server operators to see more details about channels than normal users.
servers/auspex                | Allows server operators to see more details about server information than normal users.
users/auspex                  | Allows server operators to see more details about users than normal users.
users/channel-spy             | Allows server operators to view the private/secret channels that a user is on.
users/flood/increased-buffers | Allows server operators to send and receive data without worrying about being disconnected for exceeding limits.
users/flood/no-fakelag        | Prevents server operators from being penalized with fake lag for flooding.
users/flood/no-throttle       | Allows server operators to send commands without being throttled.
users/mass-message            | Allows server operators to send a PRIVMSG or NOTICE to a server mask.

!!! warning ""
    The `users/flood/*` privileges are potentially dangerous as they grant a server operator the ability to hammer your server's CPU/RAM as much as they want.
