<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<performance>`

The `<performance>` tag defines configuration options relating to server performance. This tag can only be defined once.

Name            | Type     | Default Value  | Description
--------------- | -------- | -------------- | -----------
clonesonconnect | Boolean  | Yes            | Whether to check for clones when a user connects to the server.
netbuffersize   | Number   | 10240          | The size of the buffer used to receive data from users.
softlimit       | Number   | *Varies*       | The maximum number of connections to allow to the IRC server.
somaxconn       | Number   | *Varies*       | The maximum number of connections that may be waiting in the connection accept queue.
timeskipwarn    | Duration | 2s             | The amount of time the server clock can skip by before server operators are warned about lag.

#### Example Usage

```xml
<performance clonesonconnect="yes"
             netbuffersize="10240"
             softlimit="15000"
             somaxconn="128"
             timeskipwarn="2s">
```
