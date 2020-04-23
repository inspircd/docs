---
title: "Module Details: hostchange (v3)"
---

## The "hostchange" Module

### Description

This module allows the server administrator to define custom rules for applying hostnames to users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="hostchange">
```

#### `<hostchange>`

The `<hostchange>` tag defines an hostname setting rule. This tag can be defined as many times as required.

Name   | Type      | Default Value | Description
------ | --------- | ------------- | -----------
action | Text      | *None*        | The action to take when a user matches this rule.
mask   | Text      | *None*        | A glob pattern or CIDR range that a user must be connecting from to match against this rule.
ports  | No. Range | *None*        | A numeric range of ports that a user must be connecting from to match against this rule.
prefix | Text      | *None*        | If set then the value to prefix hostnames with in hostchange rules that use the addnick or addaccount actions
suffix | Text      | *None*        | If set then the value to suffix hsotnames with in hostchange rules that use the addnick or addaccount actions.
value  | Text      | *None*        | **Required for the set action!** The hostname to set on this user.

The action field should be set to one of the following values:

Value      | Description
---------- | -----------
addaccount | Set the user's hostname to the concatenated value of the host prefix, their account name, and the host suffix.
addnick    | Set the user's hostname to the concatenated value of the host prefix, their nickname, and the host suffix.
set        | Set the hostname of matching users to the value specified in the value field.

##### Example Usage

Sets the hostname of all connecting users to "ExampleNet/Users/&lt;account&gt;":

```xml
<hostchange action="addaccount"
            prefix="ExampleNet/Users/"
            mask="*">
```

Sets the hostname of all users who connected on port 6697 to "&lt;nick&gt;.secureusers.example.com":

```xml
<hostchange action="addnick"
            mask="*"
            port="6697"
            suffix=".secureusers.example.com">
```

Sets the hostname of users connecting from \*.servers.example.com to "webchat.example.com":

```xml
<hostchange action="set"
            mask="*.servers.example.com"
            value="webchat.example.com">
```
