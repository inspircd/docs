---
title: Module Details (denychans)
---

{! 2/_support.md !}

## The "denychans" Module

### Description

This module allows the server administrator to prevent users from joining channels matching a glob.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_denychans.so">
```

#### `<badchan>`

The `<badchan>` tag defines a channel to prevent users from joining. This tag can be defined as many times as required.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
allowopers | Boolean | No            | Whether to allow server operators to join channels matching this rule.
name       | Text    | *None*        | **Required!** A glob pattern for a channel name that users should be prevented from joining.
reason     | Text    | *None*        | A message to tell a user who tries to join a channel that matches this rule.
redirect   | Text    | *None*        | If defined then the name of a channel to join users to who try to join a channel matching this rule.

##### Example Usage

Bans channels matching #potato\* from being joined:

```xml
<badchan name="#potato*"
         reason="Discussion of vegetables is banned on this network!"
         allowopers="no">
```

Redirects users joining channel #eggplant to #aubergine:

```xml
<badchan name="#eggplant"
         redirect="#aubergine"
         reason="This network uses British English."
         allowopers="no">
```

#### `<goodchan>`

The `<goodchan>` tag defines an exemption to the rules specified with `<badchan>`. This tag can be defined as many times as required.

Name | Type | Default Value | Description
---- | ---- | ------------- | -----------
name | Text | *None*        | **Required!** A glob pattern for a channel name that users should be allowed to join regardless of any rules banning it.

##### Example Usage

```xml
<goodchan name="#*ircd">
```
