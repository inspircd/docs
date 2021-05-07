<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<include>`

The `<include>` tag allows you include the contents of a file or the output of a command into your config file. This tag can be defined as many times as required.

Name         | Type    | Default Value                            | Description
------------ | ------- | ---------------------------------------- | -----------
directory    | Text    | *None*                                   | If defined then the directory to look for .conf files in.
executable   | Text    | *None*                                   | If defined then the command to execute.
file         | Text    | *None*                                   | If defined then the file to read.
mandatorytag | Text    | *None*                                   | If defined then a tag that must exist in a config file for it to be valid.
missingokay  | Boolean | Yes                                      | [**New in v3.10.0!**](/3/change-log/#inspircd-3100) Whether to ignore config files that don't exist.
noenv        | Boolean | Yes (executable)<br>No (directory, file) | [**New in v3.6.0!**](/3/change-log/#inspircd-360) Whether to allow environment variables to be used from within the included config.
noexec       | Boolean | Yes (executable)<br>No (directory, file) | Whether to allow executable includes from within the included config.
noinclude    | Boolean | No                                       | Whether to allow file includes from within the included config.

#### Example Usage

Includes links.conf into the config:

```xml
<include file="links.conf"
         noenv="no"
         noexec="no"
         noinclude="no"
         mandatorytag="link"
         missingokay="no">
```

Includes all of the config files in 'modules' into the config:

```xml
<include directory="modules"
         noenv="no"
         noexec="no"
         noinclude="no"
         mandatorytag="link">
```

Executes curl to download https://example.com/links.conf and include it into the config:

```xml
<include executable="curl --silent https://example.com/links.conf"
         noenv="yes"
         noexec="yes"
         noinclude="no"
         mandatorytag="link">
```
