<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<type>`

The `<type>` tag defines a type of server operator. This tag can be defined as many times as required.

Name     | Type | Default Value | Description
-------- | ---- | ------------- | -----------
class    | Text | *None*        | If defined then a connect class to assign users who log into this server operator account to.
classes  | Text | *None*        | If defined then a space-delimited list of `<class>` tags to inherit privileges from.
name     | Text | *None*        | **Required!** The name for this server operator account.
vhost    | Text | *None*        | If defined then a virtual hostname to set on users who log into this server operator account.

#### Example Usage

```xml
<type name="NetAdmin"
      class="ServerOperators"
      classes="BanControl HostCloak OperChat SACommands ServerLink Shutdown"
      vhost="staff.example.net">
```
