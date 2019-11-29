<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<include>`

The `<include>` tag allows you include the contents of a file or the output of a command into your config file. This tag can be defined as many times as required.

Name         | Type    | Default Value               | Description
------------ | ------- | --------------------------- | -----------
executable   | Text    | *None*                      | If defined then the command to execute.
file         | Text    | *None*                      | If defined then the file to read.
mandatorytag | Text    | *None*                      | If defined then a tag that must exist in a config file for it to be valid.
noexec       | Boolean | Yes (executable), No (file) | Whether to allow executable includes from within the included config.
noinclude    | Boolean | No                          | Whether to allow file includes from within the included config.



#### Example Usage

Includes links.conf into the config:

```xml
<include file="conf/links.conf"
         noexec="no"
         noinclude="no"
         mandatorytag="link">
```

Executes curl to download https://example.com/links.conf and include it into the config:

```xml
<include executable="curl --silent https://example.com/links.conf"
         noexec="yes"
         noinclude="no"
         mandatorytag="link">
```
