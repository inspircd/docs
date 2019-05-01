<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<whowas>`

The `<whowas>` tag defines the configuration of the `/WHOWAS` database. This tag can only be defined once.

Name      | Type     | Default Value | Description
--------- | -------- | ------------- | -----------
groupsize | Number   | 0             | The maximum number of `/WHOWAS` entries for a nickname.
maxgroups | Number   | 0             | The maximum number of `/WHOWAS` nickname groups.
maxkeep   | Duration | 1h            | The period of time to keep `/WHOWAS` records for.

#### Example Usage

```xml
<whowas groupsize="10"
        maxgroups="100000"
        maxkeep="3d">
```
