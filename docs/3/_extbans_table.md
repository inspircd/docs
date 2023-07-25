<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Character</th>
<th>Ban Syntax</th>
<th>Module</th>
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for extban in extbans|sort(attribute="char") %}
{% if '3' == version %}
{% set prefix = extban.char ~ ':' %}
{% else %}
{% set prefix = '[!]' ~ extban.name ~ ':' %}
{% endif %}
<tr markdown="1">
<td markdown="1">{{ extban.name }}</td>
<td markdown="1">{{ extban.char }}</td>
{% if extban.syntax is none %}
<td><em>None</em></td>
{% elif extban.syntax is string %}
<td markdown="1">`{{ prefix }}{{ extban.syntax }}`</td>
{% else %}
<td markdown="1">`{{ prefix }}{{ extban.syntax | join('`<br>{{ prefix }}`') }}`</td>
{% endif %}
<td markdown="1">[{{ extban.module }}](/{{ version }}/modules/{{ extban.module }}/)</td>
<td markdown="1">{{ extban.description }}</td>
</tr>
{% endfor %}
</tbody>
</table>
