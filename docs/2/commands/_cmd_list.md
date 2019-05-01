<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/LIST [(>|<)<count>|<pattern>]`

Lists all channels visibile to the requesting user.

If `><count>` is specified then only lists channels which contain more than `<count>` users.

If `<<count>` is specified then only lists channels which contain less than `<count>` users.

If `<pattern>` is specified then only lists channels with a name or a topic matching `<pattern>`.

## Example Usage

Lists channels with more than five users:

```plaintext
/LIST >5
```

Lists channels with less than five users:

```plaintext
/LIST <5
```

Lists all channels with a name or topic matching `*support*`:

```plaintext
/LIST *support*
```
