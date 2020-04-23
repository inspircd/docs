---
title: "Module Details: services_account (v2)"
---

{! 2/_support.md !}

## The "services_account" Module

### Description

This module adds various channel and user modes relating to services accounts.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_services_account.so">
```

This module requires no other configuration.

### Channel Modes

Name         | Character | Type   | Parameter Syntax | Description
------------ | --------- | ------ | ---------------- | -----------
c_registered | r         | Switch | *None*           | Marks the channel as being registered.
reginvite    | R         | Switch | *None*           | Prevents users who are not logged into a services account from joining the channel.
regmoderated | M         | Switch | *None*           | Prevents users who are not logged into a services account from speaking in the channel.

### User Modes

Name         | Character | Type   | Parameter Syntax | Description
------------ | --------- | ------ | ---------------- | -----------
regdeaf      | R         | Switch | *None*           | Prevents users who are not logged into a services account from messaging the user.
u_registered | r         | Switch | *None*           | Marks the user as being logged into a services account.

### Exemptions

Name         | Description
------------ | -----------
regmoderated | Allows exempted users to send messages to the channel without being logged in.

### Extended Bans

Character | Type     | Ban Syntax    | Description
--------- | -------- | ------------- | -----------
R         | Matching | `R:<pattern>` | Checks whether users are logged into a services account matching &lt;pattern&gt;.
U         | Matching | `U:<pattern>` | Checks whether users matching &lt;pattern&gt; are *not* logged into a services account.

#### Example Usage

Bans users logged into the services account named Soni:

```plaintext
/MODE #channel +b R:Soni
```

Bans users matching `*!*@example.com` that are not logged into a services account:

```plaintext
/MODE #channel +b U:*!*@example.com
```
