<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<badhost>`

The `<badhost>` tag defines a permanent K-line. This tag can be defined as many times as required.

Name   | Type | Default Value  | Description
------ | ---- | -------------- | -----------
host   | Text | *None*         | **Required!** A user@host to K-line.
reason | Text | &lt;Config&gt; | The reason for the K-line being added.

#### Example Usage

```xml
<badhost host="*@example.com"
         reason="Spamming">
```
