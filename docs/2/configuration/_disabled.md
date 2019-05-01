<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<disabled>`

The `<disabled>` tag defines commands and modes which normal users can not change. This tag can only be defined once.

Name            | Type    | Default Value | Description
--------------- | ------- | ------------- | -----------
fakenonexistant | Boolean | No            | Whether to pretend that a disabled command/mode does not exist.
commands        | Text    | *None*        | A space-delimited list of commands to disable.
chanmodes       | Text    | *None*        | A list of channel modes to disable.
usermodes       | Text    | *None*        | A list of user modes to disable.

#### Example Usage

```xml
<disabled fakenonexistant="no"
          commands="MODE TOPIC"
          chanmodes="kp"
          usermodes="iw">
```
