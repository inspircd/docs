---
title: Module Details (censor)
---

{! 2/_support.md !}

## The "censor" Module

### Description

This module allows the server administrator to define inappropriate phrases that are not allowed to be used in private or channel messages.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_censor.so">
```

#### `<badword>`

The `<badword>` tag defines an inappropriate phrase. This tag can be defined as many times as required.

Name    | Type | Default Value | Description
------- | ---- | ------------- | -----------
text    | Text | *None*        | **Required!** A phrase to match within a message.
replace | Text | *None*        | If defined then a replacement phrase to replace the matched phrase with instead of blocking the message.

##### Example Usage

Replaces the phrase "wibble" with "wobble":

```xml
<badword text="wibble"
         replace="wobble">
```

Prevents users from saying the phrase "fluffy capybara":

```xml
<badword text="fluffy capybara">
```

### Channel Modes

Name   | Character | Type   | Parameter Syntax | Description
------ | --------- | ------ | ---------------- | -----------
censor | G         | Switch | *None*           | Enables censoring messages sent to the channel.

### User Modes

Name     | Character | Type   | Parameter Syntax | Description
-------- | --------- | ------ | ---------------- | -----------
u_censor | G         | Switch | *None*           | Enables censoring messages sent to the user.

### Exemptions

Name   | Description
------ | -----------
censor | Allows exempted users to send messages that contain censored phrases.

### Special Notes

The censor module does not support any kind of advanced (glob, regex, etc) matching or punishment other than message blocking. If you need that you should use [the filter module](/2/modules/filter) instead.

You should take care to avoid [the Scunthorpe problem](https://en.wikipedia.org/wiki/Scunthorpe_problem) when adding badwords.
