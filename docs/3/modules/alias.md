---
title: Module Details (alias)
---

## The "alias" Module

### Description

This module allows the server administrator to define custom channel commands (e.g. `!kick`) and server commands (e.g. `/OPERSERV`).

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="alias">
```

#### `<alias>`

The `<alias>` tag defines a custom channel or server command. This tag can be defined as many times as required.

Name           | Type    | Default Value | Description
-------------- | ------- | ------------- | -----------
text           | Text    | *None*        | **Required!** The name of the custom command.
replace        | Text    | *None*        | **Required!** The message to replace the custom command with.
format         | Text    | *None*        | If defined then a glob pattern that the command parameters must match.
requires       | Text    | *None*        | If defined then the nickname of a user which most be online for the alias to work.
channelcommand | Boolean | No            | Whether the command can be executed as a channel command.
usercommand    | Boolean | Yes           | Whether the command can be executed as a server command.
operonly       | Boolean | No            | Whether the user executing the command must be a server operator.
uline          | Boolean | No            | Whether the user specified in the requires value must be on a U-lined server.

The replacement field can contain any of the following template variables:

Variable     | Description
------------ | -----------
$1 to $9     | The value of the parameter at the specified position.
$1- to $9-   | The values of the parameters at and after the specified position.
$chan        | If executed as a channel command then the name of the channel.
$host        | The real hostname of the user that executed the command.
$ident       | The username (ident) of the user that executed the command.
$nick        | The nickname of the user that executed the command.
$requirement | The nickname specified in the requires field.
$vhost       | The virtual hostname of the user that executed the command.

##### Example Usage

Defines an oper-only `/OPERSERV` server command that messages the OperServ client if it is on a U-lined server:

```xml
<alias text="OPERSERV"
       replace="PRIVMSG OperServ :$2-"
       format="*"
       requires="OperServ"
       channelcommand="no"
       usercommand="yes"
       operonly="yes"
       uline="yes">
```

#### `<fantasy>`

The `<fantasy>` tag defines settings about custom channel commands. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
allowbots | Boolean | No            | Whether users with the bot user mode (+B) can execute channel commands.
prefix    | Text    | !             | The prefix that indicates that a message is a channel command

##### Example Usage

```xml
<fantasy allowbots="no"
         prefix=".">
```

### Special Notes

If you are using services you may find it useful to use one of the predefined service files which ship with InspIRCd.

If you are using Anope for your services add the following tag to your configuration:

```xml
<include file="examples/services/anope.conf.example">
```

If you are using Atheme for your services add the following tag to your configuration:

```xml
<include file="examples/services/atheme.conf.example">
```
