---
title: v{{ version }} User Modes
---

## User Modes

!!! note ""
    This page documents user modes. For channel modes see [the channel mode page](/3/channel-modes/).

{! 3/_mode_types_table.md !}

### Core

Core user modes are user modes which are always available. For details on the user modes provided by modules, see the modules section below.

Name      | Character | Type      | Parameter Syntax  | Usable By        | Description
--------- | --------- | --------- | ----------------- | ---------------- | -----------
invisible | i         | Switch    | *None*            | Anyone           | Marks the user as invisible.
oper      | o         | Switch    | *None*            | Server operators | Marks the user as a server operator (can only be set by the server).
snomask   | s         | Parameter | `(+|-)<snomasks>` | Server operators | Enables receiving the specified types of [server operator notice](/3/snomasks).
wallops   | w         | Switch    | *None*            | Anyone           | Enables receiving `/WALLOPS` messages from server operators.

#### Example Usage

Enables snomasks `l` (LINK) and `L` (REMOTELINK) and disables snomask `d` (DEBUG):

```plaintext
/MODE YourNick +s +lL-d
```

Enables all available snomasks:

```plaintext
/MODE YourNick +s +*
```

Disables all enabled snomasks:

```plaintext
/MODE YourNick -s
```

### Modules

{# use the template defined in mkdocs_inspircd/ #}
{% set modes = module_umodes %}
{% include "3/_modes_table.md" %}
