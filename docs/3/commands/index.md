---
title: v3 Commands
---

## Commands

This page only lists core commands. For details on the commands of a specific module please refer to [the appropriate page for that module](/3/modules).

{% for cmd in core_commands -%}
### `/{{cmd.name}} {{cmd.syntax}}`

{{cmd.description}}

{% if cmd.example %}
#### Example Usage

{% for example in cmd.example %}

{% if example.note %}
<div class="admonition note" markdown="1">
{{example.note}}
</div>
{% endif %}

{% if example.description %}
{% if example.added %}<a href="/{{ example.added|first }}/change-log/#inspircd-{{ example.added|replace(".", "") }}"><strong>New in v{{ example.added }}!</strong></a> {% endif %}{{example.description}}{% if not example.skip_colon %}:{% endif %}
{% endif %}

```plaintext
{{example.text}}
```

{% endfor %}
{% endif %}

{% endfor %}
