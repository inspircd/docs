<table markdown="1">
<thead>
<tr>
<th>Character</th>
<th>Ban Syntax</th>
<th>Module</th>
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for extban in extbans|sort(attribute="char") %}
<tr markdown="1">
<td markdown="1">{{extban.char}}</td>
<td markdown="1">{% if extban.syntax == "None" %}<em>None</em>{% else %}{{extban.syntax}}{% endif %}</td>
<td markdown="1">[{{extban.module}}](/3/modules/{{extban.module}}/)</td>
<td markdown="1">{{extban.description}}</td>
</tr>
{% endfor %}
</tbody>
</table>
