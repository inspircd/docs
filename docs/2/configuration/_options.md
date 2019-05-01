<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<options>`

The `<options>` tag defines general configuration options. This tag can only be defined once.

Name               | Type    | Default Value  | Description
------------------ | ------- | -------------- | -----------
cyclehosts         | Boolean | No             | Whether to fake a connect and reconnect for users whose hostnames have changed to allow clients to update their hostname cache.
cyclehostsfromuser | Boolean | No             | Whether to send modes from the user rather than the server when sending a fake rejoin.
defaultbind        | Text    | auto           | The IP version to bind using if an IP address is not specified.
defaultmodes       | Text    | nt             | The default modes to apply to newly created channels.
exemptchanops      | Text    | *None*         | The privileges to exempt ranked channel users from. See the notes for [the exemptchanops module](/2/modules/exemptchanops) for more information.
fixedpart          | Text    | *None*         | If defined then a static value to replace users' part messages with.
fixedquit          | Text    | *None*         | If defined then a static value to replace users' quit messages with.
hostintopic        | Boolean | No             | Whether to show the full user mask of a topic setter rather than just their nickname.
invitebypassmodes  | Boolean | Yes            | Whether being invited to a channel allows the invitee to bypass channel modes which would otherwise prevent them from joining.
ircumsgprefix      | Boolean | No             | *Deprecated!* Whether to prefix `PRIVMSG` and `NOTICE`  messages with the status character when sending a status message.
moronbanner        | Text    | You're banned! | The message to send to users who have been banned from the server.
nosnoticestack     | Boolean | No             | Whether to stop identical server notices from being stacked with "last message repeated X times".
prefixpart         | Text    | *None*         | If defined then the value to prefix users' part messages with.
prefixquit         | Text    | *None*         | If defined then the value to prefix users' quit messages with.
suffixpart         | Text    | *None*         | If defined then the value to suffix users' part messages with.
suffixquit         | Text    | *None*         | If defined then the value to suffix users' quit messages with.
syntaxhints        | Boolean | No             | Whether to send syntax hints to users who send commands with not enough parameters.
welcomenotice      | Boolean | Yes            | *Deprecated!* Whether to send a welcome message to users on connect.

The defaultbind field should be set to one of the following values:

Value | Description
----- | -----------
auto  | Bind to :: if IPv6 support is available. Otherwise, bind to 0.0.0.0.
ipv4  | Bind to 0.0.0.0 by default.
ipv6  | Bind to :: by default.

#### Example Usage

```xml
<options cyclehosts="yes"
         cyclehostsfromuser="no"
         defaultbind="auto"
         defaultmodes="nst"
         exemptchanops=""
         fixedpart=""
         fixedquit=""
         hostintopic="yes"
         invitebypassmodes="yes"
         ircumsgprefix="no"
         moronbanner="You're banned. Email abuse@example.com to appeal this decision."
         nosnoticestack="no"
         prefixpart="&quot;"
         prefixquit="Quit: "
         suffixpart="&quot;"
         suffixquit=""
         syntaxhints="yes"
         welcomenotice="no">
```
