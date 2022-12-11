---
title: v{{ version }} Channel Modes
---

## Channel Modes

!!! note ""
    This page documents channel modes. For user modes see [the user mode page](/3/user-modes/).

{! 3/_mode_types_table.md !}

### Core

Core channel modes are channel modes which are always available. For details on the channel modes provided by modules, see the modules section below.

Name       | Character | Type      | Parameter Syntax | Usable By         | Description
---------- | --------- | --------- | ---------------- | ----------------- | -----------
ban        | b         | List      | `<mask>`         | Channel operators | Bans users matching &lt;mask&gt; from joining the channel.
inviteonly | i         | Switch    | *None*           | Channel operators | Prevents users from joining the channel without an invite.
key        | k         | ParamBoth | `<key>`          | Channel operators | Prevents users from joining the channel who have not specified the &lt;key&gt; password.
limit      | l         | Parameter | `<count>`        | Channel operators | Allows no more than &lt;count&gt; users to join the channel.
moderated  | m         | Switch    | *None*           | Channel operators | Prevents users without a prefix rank from messaging the channel.
noextmsg   | n         | Switch    | *None*           | Channel operators | Prevents users who are not in the channel from messaging the channel.
op         | o         | Prefix    | `<nick>`         | Channel operators | Grants channel operator status to &lt;nick&gt;.
private    | p         | Switch    | *None*           | Channel operators | Hides the channel in `/WHOIS` from people who are not a member. You probably want channel mode `s` (secret) rather than this.
secret     | s         | Switch    | *None*           | Channel operators | Hides the channel in `/WHOIS` and `/LIST` from people who are not a member.
topiclock  | t         | Switch    | *None*           | Channel operators | Prevents non-channel operators from changing the channel topic.
voice      | v         | Prefix    | `<nick>`         | Channel operators | Grants channel voice status to &lt;nick&gt;.

#### Example Usage

Bans users matching `*!*@example.com` from joining \#channel:

```plaintext
/MODE #channel +b *!*@example.com
```

Sets the channel key for \#cheese to "cheddar":

```plaintext
/MODE #cheese +k cheddar
```

Removes the channel key for \#cheese:

```plaintext
/MODE #cheese -k cheddar
```

Limits \#channel to 100 users:

```plaintext
/MODE #channel +l 100
```

Grants channel operator status to Sadie in \#channel:

```plaintext
/MODE #channel +o Sadie
```

Removes channel operator status from Sadie in \#channel:

```plaintext
/MODE #channel -o Sadie
```

Grants channel voice status to Sadie in \#channel:

```plaintext
/MODE #channel +v Sadie
```

Removes channel voice status from Sadie in \#channel:

```plaintext
/MODE #channel -v Sadie
```

### Modules

{# use the template defined in mkdocs_inspircd/ #}
{% set modes = module_chmodes %}
{% include "3/_modes_table.md" %}

### Configuration-defined modes

Server administrators can also define custom prefix modes for channel privileges, such as channel modes `q` (founder), `a` (admin), or `h` (halfop), using the [customprefix](/3/modules/customprefix/) module.
