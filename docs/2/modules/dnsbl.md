---
title: Module Details (dnsbl)
---

{! 2/_support.md !}

## The "dnsbl" Module

### Description

This module allows the server administrator to check the IP address of connecting users against a [DNSBL](https://en.wikipedia.org/wiki/DNSBL). This is useful for preventing malicious hosts from connecting to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_dnsbl.so">
```

#### `<connect>`

This module extends the core `<connect>` tags with the following fields:

Name     | Type    | Default Value | Description
-------- | ------- | ------------- | -----------
dnsbl    | Text    | *None*        | Match users to this connect class by DNSBL name when using the MARK action.
usednsbl | Boolean | Yes           | Whether users in this connect class should be looked up in a DNSBL.

##### Example Usage

Disables DNSBL lookups for users in the WebChat class:

```xml
<connect name="WebChat"
         ...
         usednsbl="no">
```

#### `<dnsbl>`

The `<dnsbl>` tag defines a DNSBL to check connecting users against. This tag can be defined as many times as required.

Name     | Type      | Default Value                 | Description
-------- | --------- | ----------------------------- | -----------
action   | Text      | *None*                        | **Required!** The action to take against users who's IP address is in this DNSBL.
bitmask  | Number    | *None*                        | **Required for the bitmask type!** A bitmask of DNSBL result types to match against.
domain   | Text      | *None*                        | **Required!** The domain name of this DNSBL.
duration | Duration  | 1m                            | If action is set to GLINE, KLINE, or ZLINE then the duration for an X-line to last for.
host     | Text      | *None*                        | If action is set to MARK then a new hostname to set on users who's IP address is in this DNSBL.
ident    | Text      | *None*                        | If action is set to MARK then a new username (ident) to set on users who's IP address is in this DNSBL.
name     | Text      | *None*                        | **Required!** The human readable name of this DNSBL.
reason   | Text      | Your IP has been blacklisted. | The message to send to users who's IP address is in a DNSBL. The template variable %ip% will be replaced with the IP address of the user.
records  | No. Range | *None*                        | **Required for the record type!** A numeric range of DNSBL result types to match against.
type     | Text      | record                        | The type of result that this DNSBL will provide.

The action field should be set to one of the following values:

Value | Description
----- | -----------
GLINE | G-line users who's IP address is in the DNSBL.
KILL  | Kill users who's IP address is in the DNSBL.
KLINE | K-line users who's IP address is in the DNSBL.
MARK  | Marks users who's IP address is in the DNSBL.
ZLINE | Z-line users who's IP address is in the DNSBL.

The type field should be set to one of the following values:

Value   | Description
------- | -----------
bitmask | DNSBL results will be compared against the [bit mask](https://en.wikipedia.org/wiki/Mask_(computing)) specified in the bitmask field to see if the IP address in question is in a DNSBL. For example, `15` would match against DNSBL result types 1, 2, 4, and 8.
record  | DNSBL results will be compared against a numeric range of values. For example, `1-3,4,5` would match all DNSBL result types between 1 and 5.

##### Example Usage

[DroneBL](https://dronebl.org) is a DNSBL for IRC networks:

```xml
<dnsbl name="DroneBL"
       domain="dnsbl.dronebl.org"
       type="record"
       records="3,5,6,7,8,9,10,11,13,14,15,16,17,19"
       action="ZLINE"
       duration="7d"
       reason="You are listed in DroneBL. Please visit https://dronebl.org/lookup.do?ip=%ip% for more information.">
```

[EFnet RBL](https://rbl.efnetrbl.org) is a DNSBL of undesirable IP addresses detected by the [EFnet IRC Network](http://www.efnet.org/):

```xml
<dnsbl name="EFnet RBL"
       domain="rbl.efnetrbl.org"
       type="record"
       records="1,2,3,4,5"
       action="ZLINE"
       duration="7d"
       reason="You are listed in the EFnet RBL. Please visit https://rbl.efnetrbl.org/?i=%ip% for more information.">
```

[torexit.dan.me.uk](https://www.dan.me.uk/dnsbl) is a DNSBL of [Tor](https://www.torproject.org) exit nodes.

```xml
<dnsbl name="torexit.dan.me.uk"
       domain="torexit.dan.me.uk"
       type="record"
       records="100"
       action="ZLINE"
       duration="7d"
       reason="Tor exit nodes are not allowed on this network. See https://metrics.torproject.org/rs.html#search/%ip% for more information.">
```

### Statistics

Character | Description
--------- | -----------
d         | Lists information about DNSBL hits and misses.
