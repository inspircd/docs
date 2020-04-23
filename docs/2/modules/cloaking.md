---
title: "Module Details: cloaking (v2)"
---

{! 2/_support.md !}

## The "cloaking" Module

### Description

This module adds user mode `x` (cloak) which allows user hostnames to be hidden.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_cloaking.so">
```

#### `<cloak>`

The `<cloak>` tag defines settings about how the cloaking module should behave. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
mode      | Text    | *None*        | The cloaking method to use.
prefix    | Text    | *None*        | The value to prefix IP address cloaks with.
suffix    | Text    | *None*        | The value to suffix IP address cloaks with.
key       | Text    | *None*        | **Required for the half and full modes!** A random value to use as a secret key when cloaking. The longer this is the more secure it is.
key1      | Number  | *None*        | **Required for the compat-host and compat-ip modes!** *Deprecated!* A number between 1 and 2147483648 to use as a secret key when cloaking.
key2      | Number  | *None*        | **Required for the compat-host and compat-ip modes!** *Deprecated!* A number between 1 and 2147483648 to use as a secret key when cloaking.
key3      | Number  | *None*        | **Required for the compat-host and compat-ip modes!** *Deprecated!* A number between 1 and 2147483648 to use as a secret key when cloaking.
key4      | Number  | *None*        | **Required for the compat-host and compat-ip modes!** *Deprecated!* A number between 1 and 2147483648 to use as a secret key when cloaking.
lowercase | Boolean | No            | *Deprecated!* Whether to use a lower case character table when using compat-host or compat-ip mode.

The mode field should be set to one of the following values:

Value       | Description
----------- | -----------
compat-host | *Deprecated!* InspIRCd 1.2-compatible hostname-based cloaking.
compat-ip   | *Deprecated!* InspIRCd 1.2-compatible IP-based cloaking.
full        | Cloak the user completely using three slices for common CIDR bans (IPv4: /16 /24 /32, IPv6: /32 /48 /64).
half        | Cloak only the unique portion of a hostname. The last two segments of a hostname, /16 subnet of a IPv4 address, or /48 subnet of a IPv6 adddress will be visible.

##### Example Usage

Cloaking using the full mode:

```xml
<cloak mode="full"
       key="secret"
       prefix="MyNet-"
       suffix=".IP">
```

Cloaking using the deprecated compat-ip mode:

```xml
<cloak mode="compat-ip"
       key1="824139951"
       key2="738628638"
       key3="904374187"
       key4="164349800"
       prefix="MyNet-"
       suffix=".IP"
       lowercase="no">
```

### User Modes

Name  | Character | Type   | Parameter Syntax | Description
----- | --------- | ------ | ---------------- | -----------
cloak | x         | Switch | *None*           | Enables hiding of the user's hostname.
