<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<security>`

The `<security>` tag defines configuration options relating to server security. This tag can only be defined once.

Name                | Type     | Default Value | Description
------------------- | -------- | ------------- | -----------
allowcoreunload     | Boolean  | No            | Whether core modules can be unloaded by a server operator.
announceinvites     | Text     | dynamic       | Whether to send an announcement when a user is invited to a channel.
customversion       | Text     | *None*        | A custom string to show in the `/VERSION` output.
genericoper         | Boolean  | No            | Whether to show "is a server operator" in `/WHOIS` instead of the server operator's type.
hidebans            | Boolean  | No            | Whether to only show X-line messages to server operators.
hidekills           | Text     | *None*        | If defined then the text to show in a kill message instead of the name of the server operator who caused the kill.
hideserver          | Text     | *None*        | If defined then the text to show in place of a server name.
hidesplits          | Boolean  | No            | Whether to hide server names in netsplit quits from non-server operators.
hideulinekills      | Boolean  | No            | Whether to hide server notices about kills by users on U-lined servers.
maxtargets          | Number   | 20            | The maximum number of targets a user may specify in a command.
restrictbannedusers | Text     | Yes           | Whether to restrict the behaviour of users who are banned in a channel.
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

The restrictbannedusers field should be set to one of the following values:

Value  | Description
------ | -----------
yes    | Banned users should be restricted.
no     | Banned users should not be restricted.
silent | Banned users should be restricted but should not be informed.

#### Example Usage

```xml
<security allowcoreunload="no"
          announceinvites="dynamic"
          customversion=""
          genericoper="no"
          hidebans="yes"
          hidekills=""
          hideserver=""
          hidesplits="no"
          hideulinekills="yes"
          maxtargets="20"
          restrictbannedusers="yes"
          runasgroup=""
          runasuser=""
          userstats="Pu">
```
