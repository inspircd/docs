<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<path>`

The `<path>` tag defines the location of the config, data, log, and module directories. This tag can only be defined once.

Name       | Type | Default Value | Description
---------- | ---- | ------------- | -----------
configdir  | Text | conf          | The location of the config directory.
datadir    | Text | data          | The location of the data directory.
logdir     | Text | logs          | The location of the logs directory.
moduledir  | Text | modules       | The location of the modules directory.
runtimedir | Text | data          | [**New in v3.9.0!**](/3/change-log/#inspircd-390) The location of the runtime directory.

#### Example Usage

```xml
<path configdir="conf"
      datadir="data"
      logdir="logs"
      moduledir="modules"
      runtimedir="data">
```
