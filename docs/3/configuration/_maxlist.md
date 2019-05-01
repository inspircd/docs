<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<maxlist>`

The `<maxlist>` tag defines the number of list modes which can be created in a channel. This tag can be defined as many times as required.

Name  | Type   | Default Value | Description
----- | ------ | ------------- | -----------
chan  | Text   | *None*        | **Required!** A glob pattern for channels that this limit applies to.
mode  | Number | *None*        | The character or name for the mode this limit applies to. If not defined then it applies to all modes.
limit | Number | *None*        | **Required!** The number of bans which can be created in these channels.

#### Example Usage

```xml
<maxlist chan="#largechan"
         mode="b"
         limit="500">

<maxlist chan="*"
         limit="100">
```
