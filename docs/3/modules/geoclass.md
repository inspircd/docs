---
title: Module Details (geoclass)
---

## The "geoclass" Module

### Description

This module allows the server administrator to assign users to connect classes by the country they are connecting from.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="geoclass">
```

#### `<connect>`

This module extends the core `<connect>` tags with the following fields:

Name    | Type | Default Value | Description
------- | ---- | ------------- | -----------
country | Text | *None*        | A space-delimited list of [ISO 3166-1 alpha-2 country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) that users must be connecting from to be assigned to this class.

##### Example Usage

Requires users to be connecting from China or Russia to be assigned to the Example class:

```xml
<connect name="Example"
         ...
         country="CN RU">
```

### Statistics

Character | Description
--------- | -----------
G         | Lists the number of users currently connected from each country.
