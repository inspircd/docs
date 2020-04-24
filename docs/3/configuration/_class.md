<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<class>`

The `<class>` tag defines a set of server operator privileges. This tag can be defined as many times as required.

Name      | Type | Default Value | Description
--------- | ---- | ------------- | -----------
name      | Text | *None*        | A name that uniquely identifies this server operator class.
commands  | Text | *None*        | A space-delimited list of server operator-only commands that server operators with this class can execute.
privs     | Text | *None*        | A space-delimited list of server operator privileges that server operators with this class have.
chanmodes | Text | *None*        | The server operator-only channel modes that server operators with this class can change.
usermodes | Text | *None*        | The server operator-only user modes that server operators with this class can change.
snomasks  | Text | \*            | [**New in v3.6.0!**](/3/change-log/#inspircd-360) The server operator-only snomasks that server operators with this class can change.

#### Example Usage

```xml
<class name="OperChat"
       commands="WALLOPS GLOBOPS"
       privs="users/mass-message"
       chanmodes="*"
       usermodes="*"
       snomasks="gG">
```
