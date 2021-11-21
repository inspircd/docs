<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Character</th>
<th>Type</th>
<th>Parameter Syntax</th>
<th>Usable By</th>
<th>Module</td>
</tr>
</thead>
<tbody markdown="1">
{% for mode in modes|sort(attribute="char") %}
<tr markdown="1">
<td markdown="1">{{mode.name}}</td>
<td markdown="1">{{mode.char}}</td>
<td markdown="1">{{mode.type}}</td>
{% if mode.syntax is string %}
<td markdown="1">{% if mode.syntax == "None" %}<em>None</em>{% else %}`{{mode.syntax}}`{% endif %}</td>
{% else %}
<td markdown="1">`{{mode.syntax|join('`<br>`')}}`</td>
{% endif %}<td markdown="1">{{mode.usable_by}}</td>
<td markdown="1">[{{mode.module}}](/3/modules/{{mode.module}}/)</td>
</tr>
{% endfor %}
</tbody>
</table>
