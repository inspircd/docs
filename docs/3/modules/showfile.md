---
title: Module Details (showfile)
---

## The "showfile" Module

### Description

This module adds support for showing the contents

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="showfile">
```

#### `<showfile>`

The `<showfile>` tag defines a command to show the contents of a file. This tag can be defined as many times as required.

Name         | Type   | Default Value   | Description
------------ | ------ | --------------- | -----------
name         | Text   | *None*          | **Required!** The name of the command that users should execute to receive this file.
file         | Text   | *None*          | **Required!** The name of the field in `<files>` / `<execfiles>` to use when reading the file.
method       | Text   | numeric         | The method to use to send the message to the user.
endnumeric   | Number | 309             | If the method field is set to numeric then the numeric to use to stop the response.
endtext      | Text   | End of COMMAND  | If the method field is set to numeric then the message to use in the stopping numeric.
intronumeric | Number | 308             | If the method field is set to numeric then the numeric to use to start the response.
introtext    | Text   | Showing COMMAND | If the method field is set to numeric then the message to use in the starting numeric.
textnumeric  | Number | 232             | If the method field is set to numeric then the numeric to use to show the response.

The method field should be set to one of the following values:

Value   | Description
------- | -----------
numeric | Send the message using the specified numerics.
msg     | Send the message using `PRIVMSG`.
notice  | Send the message using `NOTICE`.
