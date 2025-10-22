<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

Escape            | Example (raw)                                             | Example (formatted)                                                                                             | Description
----------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -----------
`\b`              | `foo \bbar\b baz`                                         | foo <b>bar</b> baz                                                                                              | Toggles whether text should be bold.
`\c<fg>[,<bg>]`   | `foo \c03bar\c baz`<br>`foo \c11,04bar\c baz`             | foo <f style="color:green">bar</f> baz<br>foo <f style="background-color:red;color:cyan">bar</f> baz            | Toggles the foreground and/or background color of text.
`\c{<fg>[,<bg>]}` | `foo \c{green}bar\c baz`<br>`foo \c{cyan,red}bar\c baz`   | foo <f style="color:green">bar</f> baz<br>foo <f style="background-color:red;color:cyan">bar</f> baz            | [**New in v4.3.0!**](/4/change-log/#inspircd-430) Toggles the foreground and/or background color of text using color names (see below).
`\h<fg>[,<bg>]`   | `foo \hea74dcbar\h baz`<br>`foo \h613583,2ec27ebar\h baz` | foo <f style="color:#ea74dc">bar</f> baz<br>foo <f style="background-color:#2ec27e;color:#613583">bar</f> baz   | Toggles the foreground and/or background color of text using hex colors (not widely supported).
`\i`              | `foo \ibar\i baz`                                         | foo <i>bar</i> baz                                                                                              | Toggles whether text should be italicised.
`\m`              | `foo \mbar\m baz`                                         | foo <code style="color:#222">bar</code> baz                                                                     | Toggles whether text should be monospace (not widely supported).
`\r`              | `foo \c{blue,orange}bar\r baz`                            | foo <f style="background-color:orange;color:blue">bar</f><f style="background-color:blue;color:orange"> baz</f> | Swaps the foreground and background color.
`\s`              | `foo \sbar\s baz`                                         | foo <del>bar</del> baz                                                                                          | Toggles whether text should be struckthrough (not widely supported).
`\u`              | `foo \ubar\u baz`                                         | foo <u>bar</u> baz                                                                                              | Toggles whether text should be underlined.
`\x`              | `foo \b\ibar\x baz`                                       | foo <b><i>bar</i></b> baz                                                                                       | Terminates any previously specified formatting.

If using named colors they are converted to raw color codes as follows:

Code | Name        | Example
---- | ----------- | -------
00   | white       | <div style="background-color:white;border:1px solid black;border:1px solid black">&nbsp;</div>
01   | black       | <div style="background-color:black;border:1px solid black">&nbsp;</div>
02   | blue        | <div style="background-color:blue;border:1px solid black">&nbsp;</div>
03   | green       | <div style="background-color:green;border:1px solid black">&nbsp;</div>
04   | red         | <div style="background-color:red;border:1px solid black">&nbsp;</div>
05   | brown       | <div style="background-color:brown;border:1px solid black">&nbsp;</div>
06   | magenta     | <div style="background-color:magenta;border:1px solid black">&nbsp;</div>
07   | orange      | <div style="background-color:orange;border:1px solid black">&nbsp;</div>
08   | yellow      | <div style="background-color:yellow;border:1px solid black">&nbsp;</div>
09   | light green | <div style="background-color:lightgreen;border:1px solid black">&nbsp;</div>
10   | cyan        | <div style="background-color:cyan;border:1px solid black">&nbsp;</div>
11   | light cyan  | <div style="background-color:lightcyan;;border:1px solid black">&nbsp;</div>
12   | light blue  | <div style="background-color:lightblue;border:1px solid black">&nbsp;</div>
13   | pink        | <div style="background-color:pink;border:1px solid black">&nbsp;</div>
14   | grey        | <div style="background-color:grey;border:1px solid black">&nbsp;</div>
15   | light grey  | <div style="background-color:lightgrey;border:1px solid black">&nbsp;</div>
99   | default     | *Depends on client theme*

Colors in the range 16-98 are not widely supported and do not have names. See [ircdocs](https://modern.ircdocs.horse/formatting) for more information.
