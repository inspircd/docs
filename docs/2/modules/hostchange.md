---
title: Module Details: hostchange (v2)
---

{! 2/_support.md !}

## The "hostchange" Module

### Description

This module allows the server administrator to define custom rules for applying hostnames to users.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_hostchange.so">
```

#### `<host>`

The `<host>` tag defines settings about how the hostchange module should behave. This tag can only be defined once.

Name      | Type | Default Value | Description
--------- | ---- | ------------- | -----------
prefix    | Text | *None*        | If set then the value to prefix nicknames with in hostchange rules that use the addnick action.
separator | Text | *None*        | If set then the value to include between the prefix/suffix and another value.
suffix    | Text | *None*        | If set then the value to suffix nicknames with in hostchange rules that use the addnick action or the value to use as the host in hostchange rules that use the suffix action.

##### Example Usage

```xml
<host prefix="example"
      separator="."
      suffix="example.com">
```

#### `<hostchange>`

The `<hostchange>` tag defines an hostname setting rule. This tag can be defined as many times as required.

Name   | Type      | Default Value | Description
------ | --------- | ------------- | -----------
action | Text      | *None*        | The action to take when a user matches this rule.
mask   | Text      | *None*        | A glob pattern or CIDR range that a user must be connecting from to match against this rule.
ports  | No. Range | *None*        | A numeric range of ports that a user must be connecting from to match against this rule.
value  | Text      | *None*        | **Required for the set action!** The hostname to set on this user.

The action field should be set to one of the following values:

Value   | Description
------- | -----------
addnick | Set the hostname of matching users to their nickname. If `<host:prefix>` is defined the nickname will be prefixed by `<host:prefix>` and `<host:separator>`. Otherwise, it will be suffixed by `<host:separator>` and `<host:suffix>`.
set     | Set the hostname of matching users to the value specified in the value field.
suffix  | Set the hostname of matching users to the value specified in `<host:suffix>`.

##### Example Usage

Sets the hostname of all connecting users to "ExampleNet/Users/&lt;nick&gt;":

```xml
<host prefix="ExampleNet/Users"
      separator="/">

<hostchange action="addnick"
            mask="*">
```

Sets the hostname of all users who connected on port 6697 to "&lt;nick&gt;.secureusers.example.com":

```xml
<host separator="."
      suffix="secureusers.example.com">

<hostchange action="addnick"
            mask="*"
            port="6697">
```

Sets the hostname of users connecting from \*.servers.example.com to "webchat.example.com":

```xml
<hostchange action="set"
            mask="*.servers.example.com"
            value="webchat.example.com">
```

Sets the hostname of users connecting from \*.example.com to the host suffix:

```xml
<host suffix="example.com">

<hostchange action="suffix"
            mask="*.example.com"
```
