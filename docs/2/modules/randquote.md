---
title: Module Details (randquote)
---

## The "randquote" Module

### Description

This module allows random quotes to be sent to users when they connect to the server.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_randquote.so">
```

#### `<files>` &amp; `<execfiles>`

This module extends the core `<files>` and `<execfiles>` tags with the following fields:

Name   | Type | Default Value | Description
------ | ---- | ------------- | -----------
quotes | Text | *None*        | The file to read or command to execute to obtain the quotes text.

##### Example Usage

Obtains the quotes by reading conf/quotes.txt:

```xml
<files ...
       quotes="conf/quotes.txt">
```

Obtains the quotes by executing `curl https://www.example.com/quotes.txt`:

```xml
<execfiles ...
           quotes="curl https://www.example.com/quotes.txt">
```

#### `<randquote>`

The `<randquote>` tag defines settings about how the randquote module should behave. This tag can only be defined once.

Name   | Type    | Default Value | Description
------ | ------- | ------------- | -----------
file   | Text    | quotes        | The name of the field in &lt;files&gt; / &lt;execfiles&gt; to use when reading the quotes.
prefix | Text    | *None*        | If defined then text to prefix quotes with when sending them to a user.
suffix | Text    | *None*        | If defined then text to suffix quotes with when sending them to a user.

##### Example Usage

```xml
<randquote file="quotes"
           prefix=""
           suffix="">
```

### Commands

Name      | Parameter Count | Syntax | Description
--------- | --------------- | ------ | -----------
RANDQUOTE | 0               | *None* | Retrieves a random quote from the quotes file.
