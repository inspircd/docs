---
title: Module Details (chanlog)
---

{! 2/_support.md !}

## The "chanlog" Module

### Description

This module allows messages sent to snomasks to be logged to a channel.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_chanlog.so">
```

#### `<chanlog>`

The `<chanlog>` tag defines a channel to log server notices to. This tag can be defined as many times as required.

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
channel  | Text | *None*        | **Required!** The name of a channel to log server notices to.
snomasks | Text | *None*        | **Required!** One or more snomasks to log to the channel.

##### Example Usage

Logs the `cq` snomasks (local connections and quits) to #example:

```xml
<chanlog channel="#example"
         snomasks="cq">
```
