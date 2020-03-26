<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<insane>`

The `<insane>` tag defines limits to protect against overly wide X-lines being created. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
hostmasks | Boolean | No            | Whether to bypass the limit for E-lines, G-lines, and K-lines.
ipmasks   | Boolean | No            | Whether to bypass the limit for Z-lines.
nickmasks | Boolean | No            | Whether to bypass the limit for Q-lines.
trigger   | Decimal | 95.5          | The percentage of connected users who must match the X-line for it to be rejected as overly wide.

#### Example Usage

```xml
<insane hostmasks="no"
        ipmasks="no"
        nickmasks="no"
        trigger="95.5">
```
