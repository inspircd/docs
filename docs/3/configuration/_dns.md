<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<dns>`

The `<dns>` tag defines the DNS server to use when looking up hostnames. This tag can only be defined once.

Name       | Type   | Default Value | Description
---------- | ------ | ------------- | -----------
server     | Text   | *None*        | If defined then the DNS server to look up hostnames with.
timeout    | Number | 5             | The number of seconds before timing out DNS lookups.
sourceip   | Text   | *None*        | If defined then the IP address to connect from when doing DNS lookups.
sourceport | Number | *None*        | If defined then the UDP port to connect from when doing DNS lookups.

#### Example Usage

```xml
<dns server="127.0.0.53"
     timeout="5"
     sourceip=""
     sourceport="0">
```
