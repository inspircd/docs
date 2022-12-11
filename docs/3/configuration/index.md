---
title: v{{ version }} Configuration
---

{% if '4' == version %}
{! 4/_support.md !}
{% endif %}

## Configuration

!!! note ""
    If you are configuring your server from scratch you might find the example configuration files helpful.

    These are located in:

      - `/usr/share/doc/inspircd` if using our UNIX binary packages.
      - `C:\Program Files\InspIRCd\conf\examples` if using our Windows binary package.
      - `[ROOT]/run/conf/examples` if you have built in your home directory.

This page only lists core configuration. For details on the configuration of a specific module please refer to [the appropriate page for that module](/{{ version }}/modules).

{% for tag in core_config_tags -%}
### `<{{ tag.name }}>`

{{ tag.description }}

{% if tag.attributes %}
<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Default Value</th>
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for attr in tag.attributes %}
<tr markdown="1">
{% if attr.name is string %}
<td markdown="1">{{ attr.name }}</td>
{% else %}
<td markdown="1">
{% for name, version in attr.name.items() %}
{{ name }} *({{ version }})*{% if not loop.last %}<br>{% endif %}
{% endfor %}
</td>
{% endif %}
<td markdown="1">{{ attr.type }}</td>
<td markdown="1">{% if attr.default is none %}<em>None</em>{% else %}{{ attr.default }}{% endif %}</td>
<td markdown="1">{% if attr.added %}<a href="/{{ attr.added | first }}/change-log/#inspircd-{{ attr.added | replace(".", "") }}"><strong>New in v{{ attr.added }}!</strong></a> {% endif %}{% if attr.required %}<strong>Required!</strong> {% endif %}{{ attr.description }}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% endif %}

{% if extra_tag_fields[tag.name] %}
Additionally, the following fields are provided by modules:

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Default Value</th>
<th>Module</th>
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for field_name in extra_tag_fields[tag.name].keys()|sort -%}
{% for field in extra_tag_fields[tag.name][field_name] %}
<tr markdown="1">
{% if loop.first %}
{% if field.name is string %}
<td markdown="1" rowspan="{{ loop.length }}">{{ field.name }}</td>
{% else %}
<td markdown="1" rowspan="{{ loop.length }}">
{% for name, version in field.name.items() %}
{{ name }} *({{ version }})*{% if not loop.last %}<br>{% endif %}
{% endfor %}
</td>
{% endif %}
<td markdown="1" rowspan="{{ loop.length }}">{{ field.type }}</td>
<td markdown="1" rowspan="{{ loop.length }}">{% if field.default is none %}<em>None</em>{% else %}{{ field.default }}{% endif %}</td>
{% endif %}
<td markdown="1">[{{ field.module }}](/{{ version }}/modules/{{ field.module }}/)</td>
<td markdown="1">{% if field.required %}<strong>Required!</strong> {% endif %}{{ field.description }}</td>
</tr>
{% endfor %}
{% endfor %}
</tbody>
</table>
{% endif %}

{{ tag.details }}

#### Example Usage

{{ tag.example }}

{% endfor %}
