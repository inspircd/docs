---
title: v{{version}} Server Notice Masks
---

## Server Notice Masks

Server notice masks (snomasks) are a method of filtering the messages sent to a server operator who has user mode `s` (snomask) enabled. They allow a server operator to only receive the messages that they care about.

### Usage

To enable receiving server notices set user mode `s` (snomask) with the server notice masks you want as a parameter to the mode.
For example, to see local and remote connections and quit notices, execute the following command:

```plaintext
/MODE YourNick +s +cCqQ
```

To disable receiving a specific type of server notice set user mode `s` (snomask) again but remove masks by sending a "negative" change. For example, to disable remote connection and quit notices, execute the following command:

```plaintext
/MODE YourNick +s -CQ
```

To disable all server notice masks simply remove user mode `s` (snomask) entirely:

```plaintext
/MODE YourNick -s
```

A list of the valid server notice masks and what they do is listed below.

### Core SNOMasks

Core snomasks are server notice masks which are always available. For details on snomasks provided by modules, see the modules section below.

Character | Description
--------- | -----------
a         | Notifications about unspecified events on the local server.
A         | Notifications about unspecified events on a remote server.
c         | Notifications about users connecting to the local server.
C         | Notifications about users connecting to a remote server.
k         | Notifications about users being killed on the local server.
K         | Notifications about users being killed on a remote server.
o         | Notifications about users logging in and out of server operator accounts on the local server.
O         | Notifications about users logging in and out of server operator accounts on a remote server.
q         | Notifications about users disconnecting from the local server.
Q         | Notifications about users disconnecting from a remote server.
t         | Notifications about *local and remote* attempts to use the `/STATS` command.
x         | Notifications about X-lines being added/removed/expired on the local server.
X         | Notifications about X-lines being added/removed/expired on a remote server.

### Module SNOMasks

<table markdown="1">
<thead>
<tr>
<th>Character</th>
<th>Module</th>
<th>Description</th>
</tr>
</thead>
<tbody markdown="1">
{% for snomask in module_snomasks|sort(attribute="char") %}
<tr markdown="1">
<td markdown="1">{{ snomask.char }}</td>
<td markdown="1">[{{ snomask.module }}](/3/modules/{{ snomask.module }}/)</td>
<td markdown="1">{{ snomask.description }}</td>
</tr>
{% endfor %}
</tbody>
</table>
