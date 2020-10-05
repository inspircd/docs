<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<exception>`

The `<exception>` tag defines a permanent E-line. This tag can be defined as many times as required.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
host   | Text | *None*        | **Required!** A user@host to E-line.
reason | Text | *None*        | **Required!** The reason for the E-line being added.

#### Example Usage

```xml
<exception host="*@localhost"
           reason="Local connections">
```
