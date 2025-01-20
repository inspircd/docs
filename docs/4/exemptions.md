---
title: v{{ version }} Exemptions
---

## Exemptions

Exemptions allow exempting users with a channel prefix mode from channel restrictions.

### Core

!!! note ""
    Core exemptions are exemptions which are always available. For details on the exemptions provided by modules, see the modules section below.

Name      | Description
--------- | -----------
topiclock | Allows exempted users to change the channel topic.

### Modules

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Module</th>
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for exemption in module_exemptions|sort(attribute="name") %}
<tr markdown="1">
<td markdown="1">{{ exemption.name }}</td>
<td markdown="1">[{{ exemption.module }}](/{{ version }}/modules/{{ exemption.module }}/)</td>
<td markdown="1">{{ exemption.description }}</td>
</tr>
{% endfor %}
</tbody>
</table>
