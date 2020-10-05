<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<badnick>`

The `<badnick>` tag defines a permanent Q-line. This tag can be defined as many times as required.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
nick   | Text | *None*        | **Required!** A nickname to Q-line.
reason | Text | *None*        | **Required!** The reason for the Q-line being added.

#### Example Usage

```xml
<badnick nick="NickServ"
         reason="Reserved for a network service">
```
