---
title: InspIRCd Spanning Tree Protocol &mdash; Messages
---

{! server/_dev.md !}


## Syntax

Messages are formatted the same as [a standard IRCv3 message](https://ircv3.net/specs/extensions/message-tags.html#format) other than the following differences:

- The prefix will be [a SID or UUID](/server/concepts/#uuids) instead of a nick!user@host mask.
- Lines are terminated with a line feed (`\n`) instead of a carriage return and a line feed (`\r\n`).
- Tags that begin with a tilde (`~`) are internal to the server protocol and are not intended to be exposed to users.
- Once fully authenticated there are no message length limits.

## Messages

This page only lists server messages. For details on user commands that may be sent across the network see [the core commands page](/3/commands) or for a specific module please refer to [the appropriate page for that module](/3/modules).

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Syntax</th>
</tr>
</thead>
{% for msg in server_messages -%}
<tr markdown="1">
<td markdown="1">[{{ msg.name}}](/server/messages/{{msg.name|lower }}/)</td>
{% if msg.syntax is not defined %}
<td markdown="1">`{% if msg.source %}:<{{ msg.source }}> {% endif %}{{ msg.name }}`</td>
{% elif msg.syntax.text is string %}
<td markdown="1">`{% if msg.source %}:<{{ msg.source }}> {% endif %}{{ msg.name }} {{ msg.syntax.text }}`</td>
{% else %}
<td markdown="1">{% for syntax in msg.syntax.text %}`{% if syntax.startswith("^") %}{{ msg.name }} {{ syntax[1:] }}{% else %}{% if msg.source %}:<{{ msg.source }}> {% endif %}{{ msg.name }} {{ syntax }}{% endif %}`{% if not loop.last %}<br>{% endif %}{% endfor %}</td>
{% endif %}
</tr>
{% endfor %}
</tbody>
</table>
