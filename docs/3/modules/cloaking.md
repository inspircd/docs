---
title: Module Details (cloaking)
---

## The "cloaking" Module

### Description

This module adds user mode `x` (cloak) which allows user hostnames to be hidden.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="cloaking">
```

#### `<cloak>`

The `<cloak>` tag defines a cloaking profile. This tag can be defined as many times as required.

Name        | Type   | Default Value | Description
----------- | ------ | ------------- | -----------
domainparts | Number | 3             | If the half mode is used then the maximum number of domain labels that should be visible.
mode        | Text   | *None*        | The cloaking method to use.
prefix      | Text   | *None*        | The value to prefix IP address cloaks with.
suffix      | Text   | *None*        | The value to suffix IP address cloaks with.
key         | Text   | *None*        | **Required for the half and full modes!** A random 30+ character value to use as a secret key when cloaking. The longer this is the more secure it is.

The mode field should be set to one of the following values:

Value       | Description
----------- | -----------
full        | Cloak the user completely using three slices for common CIDR bans (IPv4: /16 /24 /32, IPv6: /32 /48 /64).
half        | Cloak only the unique portion of a hostname. The last two segments of a hostname, /16 subnet of a IPv4 address, or /48 subnet of a IPv6 adddress will be visible.

##### Example Usage

Cloaking using the full mode:

```xml
<cloak mode="full"
       key="changeme"
       prefix="MyNet-"
       suffix=".IP">
```

Cloaking using the half mode:

```xml
<cloak mode="half"
       key="changeme"
       prefix="MyNet-"
       suffix=".IP"
       domainparts="3">
```

### User Modes

Name  | Character | Type   | Parameter Syntax | Usable By | Description
----- | --------- | ------ | ---------------- | --------- | -----------
cloak | x         | Switch | *None*           | Anyone    | Enables hiding of the user's hostname.

### Special Notes

The first `<cloak>` tag will be used for the cloak set when a user enables user mode `x` (cloak). The rest will be generated and used to check bans. This allows you to migrate cloaking mode or to change your cloaking key without breaking your bans.
