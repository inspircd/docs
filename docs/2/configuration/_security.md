<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<security>`

The `<security>` tag defines configuration options relating to server security. This tag can only be defined once.

Name                | Type     | Default Value | Description
------------------- | -------- | ------------- | -----------
announceinvites     | Text     | none          | Whether to send an announcement when a user is invited to a channel.
customversion       | Text     | Network IRCd  | A custom string to show in the `/VERSION` output.
genericoper         | Boolean  | No            | Whether to show "is an IRC operator" in `/WHOIS` instead of the server operator's type.
hidebans            | Boolean  | No            | Whether to only show X-line messages to server operators.
hidekills           | Text     | *None*        | If defined then the text to show in a kill message instead of the name of the server operator who caused the kill.
hidemodes           | Text     | *None*        | The list modes to hide from users without channel privileges.
hidesplits          | Boolean  | No            | Whether to hide server names in netsplit quits from non-server operators.
hideulinekills      | Boolean  | No            | Whether to hide server notices about kills by users on U-lined servers.
hidewhois           | Text     | *None*        | If defined then the text to show in place of a server name in `/WHOIS` output.
maxtargets          | Number   | 20            | The maximum number of targets a user may specify in a command.
operspywhois        | Text     | no            | Whether to show private/secret channels to operators with the users/auspex privilege.
restrictbannedusers | Boolean  | Yes           | Whether to restrict the behaviour of users who are banned in a channel.
runasgroup          | Text     | *None*        | If defined then the group to switch to after starting up (requires starting as root).
runasuser           | Text     | *None*        | If defined then the user to switch to after starting up (requires starting as root).
userstats           | Text     | *None*        | The `/STATS` characters that a non-server operator can view.

The announceinvites field should be set to one of the following values:

Value   | Description
------- | -----------
none    | Don't send any invite announcements.
ops     | Send invite announcements to channel operators and higher ranked users.
dynamic | Send invites to channel half-operators (if available) and higher ranked users.
all     | Send invites to all channel members.

The operspywhois field should be set to one of the following values:

Value    | Description
-------- | -----------
no       | Don't show private/secret channels to operators with the users/auspex privilege.
yes      | Show private/secret channels to operators with the users/auspex privilege.
splitmsg | Show private/secret channels to operators with the users/auspex privilege in a separate message with an explanation.

#### Example Usage

```xml
<security announceinvites="dynamic"
          customversion=""
          genericoper="no"
          hidebans="yes"
          hidekills=""
          hidemodes="be"
          hidesplits="no"
          hideulinekills="yes"
          hidewhois=""
          maxtargets="20"
          operspywhois="yes"
          restrictbannedusers="yes"
          runasgroup=""
          runasuser=""
          userstats="Pu">
```
