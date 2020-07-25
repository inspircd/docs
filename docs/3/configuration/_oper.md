<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<oper>`

The `<oper>` tag defines a server operator account. This tag can be defined as many times as required.

Name        | Type    | Default Value | Description
----------- | ------- | ------------- | -----------
autologin   | Boolean | No            | If a fingerprint for this oper is specified, automatically log them in.
class       | Text    | *None*        | If defined then a connect class to assign users who log into this server operator account to.
fingerprint | Text    | *None*        | A space separated list of of TLS client certificate fingerprints. These can be obtained by using the /SSLINFO command while the module is loaded, and is also noticed on connect.
hash        | Text    | *None*        | If defined then the hash algorithm that the password field is hashed with.
host        | Text    | *None*        | **Required!** A space-delimited list of glob patterns for the username@hostname mask that users must be connecting from to log into this server operator account.
name        | Text    | *None*        | **Required!** The username for this server operator account.
password    | Text    | *None*        | **Required!** The password for this server operator account.
sslonly     | Boolean | No            | If enabled, this oper can only oper up if they're using a TLS (SSL) connection.  This setting only takes effect if the sslinfo module is loaded.
type        | Text    | *None*        | **Required!** The type of server operator this account is.
vhost       | Text    | *None*        | If defined then a virtual hostname to set on users who log into this server operator account.

{! 3/modules/_hash_table.md !}

#### Example Usage

```xml
<oper name="Sadie"
      password="7H8Tqm+i$jaG48RHAcoLXSB3Guzaf1bQehaNRNbblMoNrHPdguvU"
      hash="hmac-sha256"
      class="ServerOperators"
      host="*@bnc.example.com"
      type="NetAdmin"
      vhost="staff.example.net">
```


