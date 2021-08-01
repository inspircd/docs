<!-- This file contains a page fragment. Any changes will affect all pages that include it. -->

### `/MODE <channel>|<user> <modes> [<parameters>]+`

Changes the modes which are set on a channel or a user.

For a list of modes see th [channel modes](/3/channel-modes) and [user modes](/3/user-modes) pages.

#### Example Usage

Sets:

1. Channel mode `n` (noextmsg).
2. Channel parameter-set mode `k` (key) with the value "s3cr3t".
3. Channel parameter mode `l` (limit) with the value "100".
4. Channel prefix mode `o` (op) with the user "Sadie".

```plaintext
/MODE #channel +nklo s3cr3t 100 Sadie
```

Unsets:

1. Channel mode `n` (noextmsg).
2. Channel parameter-set mode `k` (key) with the value "s3cr3t".
3. Channel parameter mode `l` (limit).
4. Channel prefix mode `o` (op) with the user "Sadie".

```plaintext
/MODE #channel -nklo s3cr3t Sadie
```

Sets:

1. User mode `w` (wallops).
2. User parameter mode `s` (snomask) with the value "*".

```plaintext
/MODE Sadie +ws *
```

Unsets:

1. User mode `w` (wallops).
2. User parameter mode `s` (snomask).

```plaintext
/MODE Sadie -ws
```
