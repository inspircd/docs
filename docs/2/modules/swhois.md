---
title: Module Details (swhois)
---

{! 2/_support.md !}

## The "swhois" Module

### Description

This module adds the `/SWHOIS` command which adds custom lines to a user's WHOIS response.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_swhois.so">
```

#### `<oper>` &amp; `<type>`

This module extends the core `<oper>` and `<type>` tags with the following fields:

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
swhois | Text | *None*        | If defined then defines a custom line to add to the server operator's WHOIS response.

##### Example Usage

Adds "hates cheese" to Sadie's WHOIS response:

```xml
<oper name="Sadie"
      ...
      swhois="hates cheese">
```

### Commands

Name   | Parameter Count | Syntax          | Description
------ | --------------- | --------------- | -----------
SWHOIS | 2               | `<nick> <line>` | Sets the custom WHOIS line for &lt;nick&gt; to &lt;line&gt;.

#### Example Usage

Sets the custom WHOIS line for Sadie to "hates cheese":

```plaintext
/SWHOIS Sadie :hates cheese
```
