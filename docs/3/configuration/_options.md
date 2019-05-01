<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->


### `<options>`

The `<options>` tag defines general configuration options. This tag can only be defined once.

Name               | Type    | Default Value  | Description
------------------ | ------- | -------------- | -----------
allowzerolimit     | Boolean | Yes            | Whether to allow channels to have channel mode `l` (limit) set to 0.
casemapping        | Text    | rfc1459        | The casemapping to use when comparing channel and nicknames insensitively.
cyclehostsfromuser | Boolean | No             | Whether to send modes from the user rather than the server when sending a fake rejoin.
defaultbind        | Text    | auto           | The IP version to bind using if an IP address is not specified.
defaultmodes       | Text    | not            | The default modes to apply to newly created channels.
exemptchanops      | Text    | *None*         | The privileges to exempt ranked channel users from. See the notes for [the exemptchanops module](/2/modules/exemptchanops) for more information.
fixedpart          | Text    | *None*         | If defined then a static value to replace users' part messages with.
fixedquit          | Text    | *None*         | If defined then a static value to replace users' quit messages with.
hostintopic        | Boolean | No             | Whether to show the full user mask of a topic setter rather than just their nickname.
invitebypassmodes  | Boolean | Yes            | Whether being invited to a channel allows the invitee to bypass channel modes which would otherwise prevent them from joining.
nosnoticestack     | Boolean | No             | Whether to stop identical server notices from being stacked with "last message repeated X times".
prefixpart         | Text    | *None*         | If defined then the value to prefix users' part messages with.
prefixquit         | Text    | *None*         | If defined then the value to prefix users' quit messages with.
splitwhois         | Text    | no             | Whether to split private/secret channels from normal channels in WHOIS responses.
suffixpart         | Text    | *None*         | If defined then the value to suffix users' part messages with.
suffixquit         | Text    | *None*         | If defined then the value to suffix users' quit messages with.
syntaxhints        | Boolean | No             | Whether to send syntax hints to users who send commands with not enough parameters.
xlinemessage       | Text    | You're banned! | The message to send to users who have been banned from the server.


The casemapping field should be set to one of the following values:

Value   | Description
------- | -----------
ascii   | Use the ASCII case mapping for nicknames and channels.
rfc1459 | Use the broken RFC1459 casemapping for nicknames and channels.

The defaultbind field should be set to one of the following values:

Value | Description
----- | -----------
auto  | Bind to :: if IPv6 support is available. Otherwise, bind to 0.0.0.0.
ipv4  | Bind to 0.0.0.0 by default.
ipv6  | Bind to :: by default.

The splitwhois field should be set to one of the following values:

Value    | Description
-------- | -----------
no       | Don't split private/secret channels from normal channels in WHOIS responses.
yes      | Split private/secret channels from normal channels in WHOIS responses.
splitmsg | Split private/secret channels from normal channels in WHOIS responses with an explanation.

#### Example Usage

```xml
<options allowzerolimit="no"
         casemapping="ascii"
         cyclehostsfromuser="no"
         defaultbind="auto"
         defaultmodes="nost"
         exemptchanops=""
         fixedpart=""
         fixedquit=""
         hostintopic="yes"
         invitebypassmodes="yes"
         nosnoticestack="no"
         prefixpart="&quot;"
         prefixquit="Quit: "
         splitwhois="no"
         suffixpart="&quot;"
         suffixquit=""
         syntaxhints="yes"
         xlinemessage="You're banned. Email abuse@example.com to appeal this decision.">
```
