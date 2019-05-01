<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<banlist>`

The `<banlist>` tag defines the number of bans which can be created in a channel. This tag can be defined as many times as required.

Name  | Type   | Default Value | Description
----- | ------ | ------------- | -----------
chan  | Text   | *None*        | **Required!** A glob pattern for channels that this limit applies to.
limit | Number | *None*        | **Required!** The number of bans which can be created in these channels.

#### Example Usage

```xml
<banlist chan="#largechan"
         limit="500">

<banlist chan="*"
         limit="100">
```
