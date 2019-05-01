<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<channels>`

The `<channels>` tag defines the maximum number of channels that a user can be in. This tag can only be defined once.

Name  | Type   | Default Value | Description
----- | ------ | ------------- | -----------
opers | Number | 60            | The maximum number of channels that a server operator can join.
users | Number | 20            | The maximum number of channels that a normal user can join.

#### Example Usage

```xml
<channels opers="60"
          users="20">
```
