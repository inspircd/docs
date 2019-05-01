<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<performance>`

The `<performance>` tag defines configuration options relating to server performance. This tag can only be defined once.

Name           | Type    | Default Value  | Description
-------------- | ------- | -------------- | -----------
limitsomaxconn | Boolean | Yes            | Whether to limit to the somaxconn field to the compile-time `SOMAXCONN` constant.
netbuffersize  | Number  | 10240          | The size of the buffer used to receive data from users.
nouserdns      | Boolean | No             | Whether DNS lookups should be performed to resolve the hostnames of connecting users.
softlimit      | Number  | *Varies*       | The maximum number of connections to allow to the IRC server.
somaxconn      | Number  | *Varies*       | The maximum number of connections that may be waiting in the connection accept queue.

#### Example Usage

```xml
<performance limitsomaxconn="yes"
             netbuffersize="10240"
             nouserdns="no"
             softlimit="15000"
             somaxconn="128">
```
