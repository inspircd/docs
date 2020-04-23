---
title: "Module Details: filter (v2)"
---

{! 2/_support.md !}

## The "filter" Module

### Description

This module adds the `/FILTER` command which allows server operators to define regex matches for inappropriate phrases that are not allowed to be used in channel messages, private messages, part messages, or quit messages.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_filter.so">
```

#### `<filteropts>`

The `<filteropts>` tag defines settings about how the filter module should behave. This tag can only be defined once.

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
engine | Text | *None*        | The regular expression engine to use for checking matches.

The engine field should be set to the name of a regular expression engine.

{! 2/modules/_regex_table.md !}

##### Example Usage

```xml
<filteropts engine="glob">
```

#### `<keyword>`

The `<keyword>` tag defines an inappropriate phrase. This tag can be defined as many times as required.

Name     | Type     | Default Value  | Description
-------- | -------- | -------------- | -----------
action   | Text     | none           | The action to take when a user does something that matches this filter.
duration | Duration | 0s (Permanent) | If action is set to gline then the duration that users who match filters should be G-lined for.
flags    | Text     | \*             | One or more flags that define what type of messages this filter applies to.
pattern  | Text     | *None*         | The regex pattern to match against.
reason   | Text     | *None*         | **Required!** The reason to give to users when they are being punished for doing something that matches this filter.

The action field should be set to one of the following values:

Value  | Description
------ | -----------
block  | Block the message that matched the filter and inform server operators with the `a` (announcements) snomask.
gline  | G-line the user that matched the filter.
kill   | Kill the user that matched the filter.
none   | Write the match to the log file and take no other action.
silent | Block the message that matched the filter.

The flags field should be set to one or more of the following values:

Value | Description
----- | -----------
\*    | Enable every flag. Equivalent to `cnoPpq`.
c     | Strip color codes from messages before trying to match against filters.
n     | Match against `NOTICE` messages.
o     | Exempt server operators from matching this filter.
P     | Match against `PART` messages.
p     | Match against `PRIVMSG` messages.
q     | Match against `QUIT` messages.

##### Example Usage

!!! note ""
    The following examples assume that the "glob" regex module is being used.

    See the `<filteropts>` documentation above for more information.

G-lines unprivileged users for saying the phrase "fluffy capybara" in `PRIVMSG` and `NOTICE` messages:

```xml
<keyword pattern="*fluffy?capybara*"
         flags="nop"
         action="gline"
         duration="1h"
         reason="Fluffy capybaras are too cute for this network!">
```

### Commands

Name   | Parameter Count | Syntax                                                            | Description
------ | --------------- | ----------------------------------------------------------------- | -----------
FILTER | 1, 4-5          | `<pattern>`<br>`<pattern> <action> <flags> [<duration>] <reason>` | Allows server operators to add and remove filters.

#### Example Usage

!!! note ""
    The following examples assume that the "glob" regex module is being used.

    See the `<filteropts>` documentation above for more information.

G-lines users for saying the phrase "fluffy capybara" in `/PRIVMSG` and `/NOTICE` messages:

```plaintext
/FILTER *fluffy?capybara* gline nop 1h :Fluffy capybaras are too cute for this network
```

Kills users who have "spam" in their `/PART` message:

```plaintext
/FILTER *spam* kill coP :Spam is off-topic on ExampleNet
```

Removes a filter on \*fluffy?capybara\*:

```plaintext
/FILTER *fluffy?capybara*
```

### Statistics

Character | Description
--------- | -----------
s         | Lists all filters and filter-exempt targets.

### Special Notes

Having a high number of filters or having filters which take a long time to match can have significant impact on server performance.
