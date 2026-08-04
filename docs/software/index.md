---
title: Third-party software that works with InspIRCd
---

## Third-party software that works with InspIRCd

{% for category in software -%}

### {{ category.name }}

{{ category.description }}

{% set has_maintainer = (category.software | map(attribute='maintainer') | select('defined') | list | length > 0) %}
{% set has_version = (category.software | map(attribute='version') | select('defined') | list | length > 0) %}

<table markdown="1">
<thead>
<tr>
<th>Name</th>
{% if has_maintainer %}
<th>Maintainer</th>
{% endif %}
{% if has_version %}
<th>Minimum Version</th>
{% endif %}
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for software in category.software %}
<tr markdown="1">
<td markdown="1"><a href="{{ software.website }}">{{ software.name }}</a></td>
{% if has_maintainer %}
<td markdown="1">{{ software.maintainer | default("Unknown") }}</td>
{% endif %}
{% if has_version %}
<td markdown="1">{{ software.version | default("Any") }}</td>
{% endif %}
<td markdown="1">{{ software.description }}</td>
</td>
{% endfor %}
</tbody>
</table>

{% endfor %}
