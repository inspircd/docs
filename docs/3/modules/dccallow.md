---
title: Module Details (dccallow)
---

## The "dccallow" Module

### Description

This module allows the server administrator to configure what files are allowed to be sent via DCC SEND and allows users to configure who can send them DCC CHAT and DCC SEND requests.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="dccallow">
```

#### `<banfile>`

The `<banfile>` tag defines a rule to use when determining if a file can be sent with `DCC SEND`. This tag can be defined as many times as required.

Name    | Type | Default Value | Description
------- | ---- | ------------- | -----------
action  | Text | deny          | The action to take when a file matches the pattern.
pattern | Text | *None*        | **Required!** A glob pattern for the filename.

The action field should be set to one of the following values:

Value | Description
----- | -----------
allow | Allows files matching the pattern to be sent.
deny  | Denies file matching the pattern from being sent.

##### Example Usage

Bans executables from being sent:

```xml
<banfile action="block"
         pattern="*.exe">
```

Allows only text files to be sent:

```xml
<banfile action="allow"
         pattern="*.txt">
<banfile action="deny"
         pattern="*">
```

#### `<dccallow>`

The `<dccallow>` tag defines settings about how the dccallow module should behave. This tag can only be defined once.

Name       | Type    | Default Value | Description
---------- | ------- | ------------- | -----------
action     | Text    | deny          | The default action to take if a file does not match a `<banfile>` rule.
blockchat  | Boolean | No            | Whether DCC CHAT also requires the source to be on the DCC whitelist.
length     | Number  | 0             | The default time a DCC whitelist entry is valid for. Setting this to 0 means the entry is permanent.
maxentries | Number  | 20            | The maximum number of entries that a user can have on their DCC whitelist.

See the `<banfile>` documentation above for a list of possible values for the action field.

##### Example Usage

```xml
<dccallow action="deny"
          blockchat="no"
          length="0"
          maxentries="20">
```

### Commands

Name     | Parameter Count | Syntax                                                | Description
-------- | --------------- | ----------------------------------------------------- | -----------
DCCALLOW | 1-2             | `[+]<nick> [<time>]`<br>`-<nick>`<br>`HELP`<br>`LIST` | Allows users to add other users to their DCC whitelist, remove other users from their DCC whitelist, and view the users on their DCC whitelist.

#### Example Usage

Lists all users on your DCC whitelist:

```plaintext
/DCCALLOW LIST
```

Adds Adam to your DCC whitelist until the server expires it:

```plaintext
/DCCALLOW +Adam
```

Adds Sadie to your DCC whitelist for two hours:

```plaintext
/DCCALLOW +Sadie 2h
```

Removes "Attila" from your DCC whitelist:

```plaintext
/DCCALLOW -Attila
```
