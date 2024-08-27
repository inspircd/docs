---
title: v{{ version }} Extended Bans
---

## Extended Bans

Some [list modes](/{{ version }}/channel-modes), such as [channel mode `b` (ban)](/{{ version }}/channel-modes), take a `<nick>!<user>@<host>` mask as their parameter. These list modes can be extended to support alternate forms of matching and actions. {% if '4' == version %} If prefixed with an `!` then the behaviour is inverted.{% endif %}

### Acting

Acting extended bans allow restricting actions that users can perform. Such actions can include preventing a user from speaking in a channel (requires [the muteban module](/{{ version }}/modules/muteban)) or changing their nickname (requires [the nonicks module](/{{ version }}/modules/nonicks)). Acting extended bans can also be stacked with matching extended bans (see below).

{% set extbans = acting_module_extbans %}
{% include "4/_extbans_table.md" %}

### Matching

Matching extended bans allow matching against extended user attributes such as connect class (requires [the classban module](/{{ version }}/modules/classban)) or TLS (SSL) fingerprint (requires [the sslmodes module](/{{ version }}/modules/sslmodes)).

{% set extbans = matching_module_extbans %}
{% include "4/_extbans_table.md" %}
