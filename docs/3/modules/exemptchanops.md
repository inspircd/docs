---
title: Module Details (exemptchanops)
---

## The "exemptchanops" Module

### Description

This module adds channel mode `X` (exemptchanops) which allows channel operators to grant exemptions to various channel-level restrictions.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="exemptchanops">
```

This module requires no other configuration.

### Channel Modes

Name          | Character | Type | Parameter Syntax       | Description
------------- | --------- | ---- | ---------------------- | -----------
exemptchanops | X         | List | `<restriction>:<mode>` | Exempts users with the &lt;mode&gt; prefix mode or higher from &lt;restriction&gt;.

#### Example Usage

Exempts channel operators and above from channel mode `W` (regmoderated) (requires [the services_account module](/3/modules/services_account)):

```plaintext
/MODE #channel +X regmoderated:o
```

### Special Notes

The modules which ship with InspIRCd define the following restrictions:

Name           | Description
-------------- | -----------
auditorium-see | Exempts from the user list being hidden by channel mode `u` (auditorium). Requires [the auditorium module](/3/modules/auditorium).
auditorium-vis | Exempts from the being hidden from the user list by channel mode `u` (auditorium). Requires [the auditorium module](/3/modules/auditorium).
blockcaps      | Exempts users from channel mode `B` (blockcaps). Requires [the blockcaps module](/3/modules/blockcaps).
blockcolor     | Exempts users from channel mode `c` (blockcolor). Requires [the blockcolor module](/3/modules/blockcolor).
censor         | Exempts users from channel mode `G` (censor). Requires [the censor module](/3/modules/censor).
filter         | Exempts users from channel mode `g` (filter). Requires [the chanfilter module](/3/modules/chanfilter).
flood          | Exempts users from channel mode `f` (flood). Requires [the messageflood module](/3/modules/messageflood).
nickflood      | Exempts users from channel mode `F` (nickflood). Requires [the nickflood module](/3/modules/nickflood).
noctcp         | Exempts users from channel mode `C` (noctcp). Requires [the noctcp module](/3/modules/noctcp).
nonick         | Exempts users from channel mode `N` (nonick). Requires [the nonicks module](/3/modules/nonicks).
nonotice       | Exempts users from channel mode `T` (nonotice). Requires [the nonotice module](/3/modules/nonotice).
regmoderated   | Exempts users from channel mode `W` (regmoderated). Requires [the services_account module](/3/modules/services_account).
stripcolor     | Exempts users from channel mode `S` (stripcolor). Requires [the stripcolor module](/3/modules/stripcolor).
topiclock      | Exempts users from channel mode `t` (topiclock).
