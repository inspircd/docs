<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<cidr>`

The `<cidr>` tag defines the number of bits of an IP address that should be looked at when locating clones. This tag can only be defined once.

Name      | Type   | Default Value | Description
--------- | ------ | ------------- | -----------
ipv4clone | Number | 32            | The number of bits (0-32) of an IPv4 address that should be looked at when locating clones.
ipv6clone | Number | 128           | The number of bits (0-128) of an IPv6 address that should be looked at when locating clones.

#### Example Usage

```xml
<cidr ipv4clone="32"
      ipv6clone="128">
```
