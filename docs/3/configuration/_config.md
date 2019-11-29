<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<config>`

The `<config>` tag allows you to to define how the config is parsed. This tag can be defined as many times as required.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
format | Text | xml           | The config format to use.

The format field should be set to one of the following values:

Value  | Description
------ | -----------
compat | *Deprecated!* Use the 1.2-style format with C-style escape sequences (e.g. `\n`).
xml    | Use the 2.0-style format with XML-style escapes (e.g. `&nl;`), numeric entities (e.g. `&#10;`) and `<define>`.

#### Example Usage

```xml
<config format="xml">
```
