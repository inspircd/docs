<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<define>`

The `<define>` tag allows you to to define XML-style entities which you can use in your config to avoid duplication. This tag can be defined as many times as required.

Name  | Type | Default Value | Description
----- | ---- | ------------- | -----------
name  | Text | *None*        | **Required!** The name of the entity.
value | Text | *None*        | The value to replace instances of the entity with.

#### Example Usage

Creates the `&ServerHost;` entity with a value of "example.com":

```xml
<define name="ServerHost"
        value="example.com">
```
