<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `<power>`

The `<power>` tag defines the passwords for the `/DIE` and `/RESTART` commands. This tag can only be defined once.

Name        | Type | Default Value | Description
----------- | ---- | ------------- | -----------
hash        | Text | *None*        | If defined then the hash algorithm that the password fields are hashed with.
diepass     | Text | *None*        | The password for the `/DIE` command.
restartpass | Text | *None*        | The password for the `/RESTART` command.

{! 2/modules/_hash_table.md !}

#### Example Usage

```xml
<power hash="hmac-sha256"
       diepass="dsPt0O0a$hzRT2ODLGgQnyaugt74ACaP4YN1BBtff/rU94ZJi29U"
       restartpass="hpMUFNl5$YVcwiAWphiqm1zgzzz8j+lBi7bOtSDNVhdpBmflL5VQ">
```
