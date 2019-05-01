<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<limits>`

The `<limits>` tag defines the maximum length of user-configurable fields. This tag can only be defined once.

Name     | Type   | Default Value | Description
-------- | ------ | ------------- | -----------
maxaway  | Number | 200           | The maximum length of an away message.
maxchan  | Number | 64            | The maximum length of a channel name.
maxhost  | Number | 64            | The maximum length of a hostname.
maxident | Number | 10            | The maximum length of a username (ident).
maxkick  | Number | 255           | The maximum length of a kick message.
maxmodes | Number | 20            | The maximum number of non-flag modes that can be changed in a single `MODE` message.
maxnick  | Number | 30            | The maximum length of a nickname.
maxquit  | Number | 255           | The maximum length of a quit message.
maxreal  | Number | 128           | The maximum length of a real name (gecos).
maxtopic | Number | 307           | The maximum length of a channel topic.

#### Example Usage

```xml
<limits maxaway="200"
        maxchan="64"
        maxhost="64"
        maxident="11"
        maxkick="255"
        maxmodes="20"
        maxnick="32"
        maxquit="255"
        maxreal="128"
        maxtopic="307">
```
