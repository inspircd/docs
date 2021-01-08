<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<server>`

The `<server>` tag defines settings about the local server. This tag can only be defined once.

Name        | Type | Default Value | Description
----------- | ---- | ------------- | -----------
name        | Text | *None*        | **Required!** The hostname of the local server.
description | Text | Configure Me  | A description of the local server.
network     | Text | Network       | The name of the IRC network the local server is attached to.
id          | Text | *None*        | If defined then a unique server identifier in the format [0-9][0-9A-Z][0-9A-Z].

#### Example Usage

```xml
<server name="irc.eu.example.com"
        description="ExampleNet's European server"
        network="ExampleNet"
        id="34C">
```
