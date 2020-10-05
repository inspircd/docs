<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<badip>`

The `<badip>` tag defines a permanent Z-line. This tag can be defined as many times as required.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
ipmask | Text | *None*        | **Required!** An IP address to Z-line.
reason | Text | *None*        | **Required!** The reason for the Z-line being added.

#### Example Usage

```xml
<badip ipmask="192.0.2.0/24"
       reason="Spamming">
```
