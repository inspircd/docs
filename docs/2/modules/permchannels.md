---
title: Module Details (permchannels)
---

{! 2/_support.md !}

## The "permchannels" Module

### Description

This module adds channel mode `P` (permanent) which prevents the channel from being deleted when the last user leaves.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="m_permchannels.so">
```

#### `<permchanneldb>`

The `<permchanneldb>` tag defines settings about how the permchannels module should behave. This tag can only be defined once.

Name      | Type    | Default Value | Description
--------- | ------- | ------------- | -----------
filename  | Text    | *None*        | If defined then the location to write a permchannels configuration file to.
listmodes | Boolean | No            | Whether to save list modes to the permchannels configuration file.

##### Example Usage

```xml
<permchanneldb filename="conf/permchannels.conf"
               listmodes="yes">
```

#### `<permchannels>`

The `<permchannels>` tag defines a permanent channel. This tag can be defined as many times as required.

Name       | Type   | Default Value           | Description
---------- | ------ | ----------------------- | -----------
channel    | Text   | *None*                  | **Required!** The name of the channel.
modes      | Text   | *None*                  | If defined then the modes set on the channel.
topic      | Text   | *None*                  | If defined then the topic of the channel.
topicsetby | Text   | *The server name*       | The nickname of the user who set the channel topic.
topicts    | Number | *The current UNIX time* | The UNIX time at which the channel topic was set.
ts         | Number | *The current UNIX time* | The UNIX time at which the channel was created.

##### Example Usage

```xml
<permchannels channel="#example"
              modes="+bnt *!*@example.com"
              topic="Welcome to the Example channel!"
              topicsetby="Sadie"
              topicts="956188800"
              ts="726192000">
```

### Channel Modes

Name      | Character | Type   | Parameter Syntax | Description
--------- | --------- | ------ | ---------------- | -----------
permanent | P         | Switch | *None*           | Prevents the channel from being deleted when the last user leaves.

### Special Notes

You should remember to `<include>` the file specified in `<permchannels:filename>` in your server configuration.

It is recommended that you set channel mode +P (permanent) on channels and let InspIRCd write a configuration file rather than manually defining permanent channels in your server configuration.
