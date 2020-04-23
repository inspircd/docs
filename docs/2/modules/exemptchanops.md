---
title: Module Details: exemptchanops (v2)
---

{! 2/_support.md !}

## The "exemptchanops" Module

### Description

This module adds channel mode `X` (exemptchanops) which allows channel operators to grant exemptions to various channel-level restrictions.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_exemptchanops.so">
```

This module requires no other configuration.

### Channel Modes

Name          | Character | Type | Parameter Syntax       | Description
------------- | --------- | ---- | ---------------------- | -----------
exemptchanops | X         | List | `<restriction>:<mode>` | Exempts users with the &lt;mode&gt; prefix mode or higher from &lt;restriction&gt;.

#### Example Usage

Exempts channel operators and above from channel mode `M` (regmoderated) (requires [the services_account module](/2/modules/services_account)):

```plaintext
/MODE #channel +X regmoderated:o
```

### Special Notes

The modules which ship with InspIRCd define the following restrictions:

Name           | Description
-------------- | -----------
auditorium-see | Exempts from the user list being hidden by channel mode `u` (auditorium). Requires [the auditorium module](/2/modules/auditorium).
auditorium-vis | Exempts from being hidden from the user list by channel mode `u` (auditorium). Requires [the auditorium module](/2/modules/auditorium).
blockcaps      | Exempts users from channel mode `B` (blockcaps). Requires [the blockcaps module](/2/modules/blockcaps).
blockcolor     | Exempts users from channel mode `c` (blockcolor). Requires [the blockcolor module](/2/modules/blockcolor).
censor         | Exempts users from channel mode `G` (censor). Requires [the censor module](/2/modules/censor).
filter         | Exempts users from channel mode `g` (filter). Requires [the chanfilter module](/2/modules/chanfilter).
flood          | Exempts users from channel mode `f` (flood). Requires [the messageflood module](/2/modules/messageflood).
nickflood      | Exempts users from channel mode `F` (nickflood). Requires [the nickflood module](/2/modules/nickflood).
noctcp         | Exempts users from channel mode `C` (noctcp). Requires [the noctcp module](/2/modules/noctcp).
nonick         | Exempts users from channel mode `N` (nonick). Requires [the nonicks module](/2/modules/nonicks).
nonotice       | Exempts users from channel mode `T` (nonotice). Requires [the nonotice module](/2/modules/nonotice).
regmoderated   | Exempts users from channel mode `M` (regmoderated). Requires [the services_account module](/2/modules/services_account).
stripcolor     | Exempts users from channel mode `S` (stripcolor). Requires [the stripcolor module](/2/modules/stripcolor).
topiclock      | Exempts users from channel mode `t` (topiclock).
