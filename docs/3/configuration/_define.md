<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<define>`

The `<define>` tag allows you to to define XML-style entities which you can use in your config to avoid duplication. This tag can be defined as many times as required.

Name  | Type | Default Value | Description
----- | ---- | ------------- | -----------
name  | Text | *None*        | **Required!** The name of the entity.
value | Text | *None*        | The value to replace instances of the entity with.

The following entities are already defined:

Name                  | Description
--------------------- | -----------
`&amp;`               | An ampersand.
`&apos;`              | [**New in v3.9.0!**](/3/change-log/#inspircd-390) A single quote. This can be used unescaped but is supported for compatibility with XML generators.
`&env.NAME;`          | The value of the `NAME` environment variable when InspIRCd was first started.
`&gt;`                | [**New in v3.9.0!**](/3/change-log/#inspircd-390) A greater than symbol. This can be used unescaped but is supported for compatibility with XML generators.
`&irc.bold;`          | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Makes subsequent text within an IRC message bold.
`&irc.color;`         | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Makes subsequent text within an IRC message colored. Should be followed by color codes in the format `FG[,BG]`. See [ircdocs](https://modern.ircdocs.horse/formatting.html#colors) for more information.
`&irc.italic;`        | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Makes subsequent text within an IRC message italic.
`&irc.monospace;`     | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Makes subsequent text within an IRC message monospace (not widely supported).
`&irc.reset;`         | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Disables all text formatting for subsequent text.
`&irc.reverse;`       | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Makes subsequent text within an IRC message reversed.
`&irc.strikethrough;` | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Makes subsequent text within an IRC message struckthrough (not widely supported).
`&irc.underline;`     | [**New in v3.9.0!**](/3/change-log/#inspircd-390) Makes subsequent text within an IRC message underlined
`&lt;`                | [**New in v3.9.0!**](/3/change-log/#inspircd-390) A less than symbol. This can be used unescaped but is supported for compatibility with XML generators.
`&nl;`                | A new line.
`&quot;`              | A double quote.

#### Example Usage

Creates the `&ServerHost;` entity with a value of "example.com":

```xml
<define name="ServerHost"
        value="example.com">
```
