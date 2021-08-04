---
title: v3 Configuration
---

## Configuration

!!! note ""
    If you are configuring your server from scratch you might find the example configuration files helpful.

    These are located in `/usr/share/doc/inspircd` if using our binary packages and `./run/conf/examples` if you have built from source.

This page only lists core configuration. For details on the configuration of a specific module please refer to [the appropriate page for that module](/3/modules).

{% for tag in core_config_tags -%}
### `{{tag.name}}`

{{tag.description}}

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
<td markdown="1">{{attr.name}}</td>
<td markdown="1">{{attr.type}}</td>
<td markdown="1">{% if attr.default == "None" %}<em>None</em>{% else %}{{attr.default}}{% endif %}</td>
<td markdown="1">{% if attr.required %}<strong>Required!</strong> {% endif %}{{attr.description}}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% endif %}

{{tag.details}}

#### Example Usage

{{tag.example}}

{% endfor %}
