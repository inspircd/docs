---
title: Module Details (codepage)
---

## The "codepage" Module

!!! note "New in v3.5.0!"
    If you are using an older version you will need to upgrade to use this module.

### Description

This module allows the server administrator to define what characters are allowed in nicknames and how characters should be compared in a case insensitive way.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="codepage">
```

#### `<codepage>`

The `<codepage>` tag defines settings about how the codepage module should behave. This tag can only be defined once.

Name | Type | Default Value | Description
---- | ---- | ------------- | -----------
name | Text | *None*        | *Required!* The name of the codepage; sent to users in the `005` (RPL_ISUPPORT) numeric.

##### Example Usage

```xml
<codepage name="latin1">
```

#### `<cpchars>`

The `<cpchars>` tag defines a single character or inclusive range of characters that are allowed in nicknames. This tag can be defined as many times as required.

Name  | Type    | Default Value | Description
----- | ------- | ------------- | -----------
begin | Number  | *None*        | The start of an inclusive range of characters to allow in nicknames.
end   | Number  | *None*        | The end of an inclusive range of characters to allow in nicknames.
front | Boolean | No            | Whether the characters specified in this tag can exist at the start of a nickname.
index | Number  | *None*        | A character to allow in nicknames.

##### Example Usage

Allows the character with the numeric code point 45 in a nickname except as the first character.

```
<cpchars index="45"
         front="no">
```

Allows characters with the numeric code points in the inclusive range 123 to 125 at any point in a nickname:

```
<cpchars begin="123"
         end="125"
         front="yes">
```

### Special Notes

The following code pages for use with this module are present in the config examples directory.

Code page       | Include Tag
--------------- | -----------
ascii           | `<include file="examples/codepages/ascii.conf.example">`
latin1          | `<include file="examples/codepages/latin1.conf.example">`
rfc1459         | `<include file="examples/codepages/rfc1459.conf.example">`
strict-rfc1459  | `<include file="examples/codepages/strict-rfc1459.conf.example">`
