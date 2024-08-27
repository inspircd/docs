<table markdown="1">
<thead>
<tr>
<th>Character</th>
<th>Module</th>
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for snomask in snomasks|sort(attribute="char") %}
<tr markdown="1">
<td markdown="1">{{ snomask.char }}</td>
<td markdown="1">[{{ snomask.module }}](/{{ version }}/modules/{{ snomask.module }}/)</td>
<td markdown="1">{{ snomask.description }}</td>
</tr>
{% endfor %}
</tbody>
</table>
