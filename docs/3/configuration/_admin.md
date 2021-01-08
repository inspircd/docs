<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<admin>`

The `<admin>` tag defines contact details for the server administrator. This tag can only be defined once.

Name  | Type | Default Value    | Description
----- | ---- | ---------------- | -----------
name  | Text | *None*           | If defined then the real name of the server operator.
nick  | Text | admin            | The nickname of the server operator.
email | Text | null@example.com | The email address of the server operator.

#### Example Usage

```xml
<admin name="John Doe"
       nick="JDoe123"
       email="jdoe123@example.com">
```
