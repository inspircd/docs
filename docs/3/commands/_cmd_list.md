<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/LIST [(>|<)<count>|C(>|<)<minutes>|T(>|<)<minutes>|[!]<pattern>]`

Lists all channels visibile to the requesting user.

If `><count>` is specified then only lists channels which contain more than `<count>` users.

If `<<count>` is specified then only lists channels which contain less than `<count>` users.

If `C><minutes>` is specified then only lists channels which were created more than `<minutes>` minutes ago.

If `C<<minutes>` is specified then only lists channels which were created less than `<minutes>` minutes ago.

If `T><minutes>` is specified then only lists channels which have had the topic changed more than `<minutes>` minutes ago.

If `T<<minutes>` is specified then only lists channels which have had the topic changed less than `<minutes>` minutes ago.

If `<pattern>` is specified then only lists channels with a name or a topic matching `<pattern>`.

If `!<pattern>` is specified then only lists channels with a name or a topic not matching `<pattern>`.

#### Example Usage

Lists channels with more than five users:

```plaintext
/LIST >5
```

Lists channels with less than five users:

```plaintext
/LIST <5
```



Lists channels which were created more than ten minutes ago:

```plaintext
/LIST C>10
```

Lists channels which were created less than ten minutes ago:

```plaintext
/LIST C<10
```

Lists channels which had the topic changed more than ten minutes ago:

```plaintext
/LIST T>10
```

Lists channels which had the topic changed less than ten minutes ago:

```plaintext
/LIST T<10
```

Lists all channels with a name or topic matching `*support*`:

```plaintext
/LIST *support*
```

Lists all channels with a name or topic not matching `*support*`:

```plaintext
/LIST !*support*
```
