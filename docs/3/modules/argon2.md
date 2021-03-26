---
title: "Module Details: argon2 (v3)"
---

## The "argon2" Module

!!! note "New in v3.8.0!"
    If you are using an older version you will need to upgrade to use this module.

!!! note ""
    This module depends on a third-party library ([Argon2](https://github.com/P-H-C/phc-winner-argon2)) and must be manually enabled at compile time.

    Once you have installed the dependency you can enable this module using the following command:

    <pre><code>./configure --enable-extras argon2</code></pre>

### Description

This module allows other modules to generate [Argon2](https://en.wikipedia.org/wiki/Argon2) hashes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="argon2">
```

#### `<argon2>`

The `<argon2>` tag defines the defaults for the Argon2 algorithms. This tag can only be defined once.

Name       | Type   | Default Value | Description
---------- | ------ | ------------- | -----------
memory     | Number | 131072        | The memory hardness in kibibytes of the Argon2 algorithms.
iterations | Number | 3             | The time hardness of the Argon2 algorithms.
lanes      | Number | 1             | The number of parallel chains to run at once.
threads    | Number | 1             | The number of threads that generating an Argon2 hash can spawn.
length     | Number | 32            | The length of the output in bytes.
saltlength | Number | 16            | The length of the salt in bytes.
version    | Number | 13            | The version of the Argon2 algorithm to use.

The version field should be set to one of the following values:

Value  | Description
------ | -----------
10     | Use version 1.0 of the Argon2 algorithm.
13     | Use version 1.3 of the Argon2 algorithm.

##### Example Usage

```xml
<argon2 memory="128MB"
        iterations="3"
        lanes="1"
        threads="1"
        length="32"
        saltlength="16"
        version="13">
```

#### `<argon2d>`

The `<argon2d>` tag defines the settings for the Argon2d algorithm. This tag can only be defined once.

Name       | Type   | Default Value                   | Description
---------- | ------ | ------------------------------- | -----------
memory     | Number | *See &gt;argon2:memory&gt;*     | The memory hardness in kibibytes of the Argon2d algorithm.
iterations | Number | *See &gt;argon2:iterations&gt;* | The time hardness of the Argon2d algorithm.
lanes      | Number | *See &gt;argon2:lanes&gt;*      | The number of parallel chains to run at once.
threads    | Number | *See &gt;argon2:threads&gt;*    | The number of threads that generating an Argon2d hash can spawn.
length     | Number | *See &gt;argon2:length&gt;*     | The length of the output in bytes.
saltlength | Number | *See &gt;argon2:saltlength&gt;* | The length of the salt in bytes.
version    | Number | *See &gt;argon2:version&gt;*    | The version of the Argon2d algorithm to use.

The version field should be set to one of the following values:

Value  | Description
------ | -----------
10     | Use version 1.0 of the Argon2d algorithm.
13     | Use version 1.3 of the Argon2d algorithm.

##### Example Usage

```xml
<argon2d memory="128MB"
         iterations="3"
         lanes="1"
         threads="1"
         length="32"
         saltlength="16"
         version="13">
```

#### `<argon2i>`

The `<argon2i>` tag defines the settings for the Argon2i algorithm. This tag can only be defined once.

Name       | Type   | Default Value                   | Description
---------- | ------ | ------------------------------- | -----------
memory     | Number | *See &gt;argon2:memory&gt;*     | The memory hardness in kibibytes of the Argon2i algorithm.
iterations | Number | *See &gt;argon2:iterations&gt;* | The time hardness of the Argon2i algorithm.
lanes      | Number | *See &gt;argon2:lanes&gt;*      | The number of parallel chains to run at once.
threads    | Number | *See &gt;argon2:threads&gt;*    | The number of threads that generating an Argon2i hash can spawn.
length     | Number | *See &gt;argon2:length&gt;*     | The length of the output in bytes.
saltlength | Number | *See &gt;argon2:saltlength&gt;* | The length of the salt in bytes.
version    | Number | *See &gt;argon2:version&gt;*    | The version of the Argon2i algorithm to use.

The version field should be set to one of the following values:

Value  | Description
------ | -----------
10     | Use version 1.0 of the Argon2i algorithm.
13     | Use version 1.3 of the Argon2i algorithm.

##### Example Usage

```xml
<argon2i memory="128MB"
         iterations="3"
         lanes="1"
         threads="1"
         length="32"
         saltlength="16"
         version="13">
```

#### `<argon2id>`

The `<argon2id>` tag defines the settings for the Argon2id algorithm. This tag can only be defined once.

Name       | Type   | Default Value                   | Description
---------- | ------ | ------------------------------- | -----------
memory     | Number | *See &gt;argon2:memory&gt;*     | The memory hardness in kibibytes of the Argon2id algorithm.
iterations | Number | *See &gt;argon2:iterations&gt;* | The time hardness of the Argon2id algorithm.
lanes      | Number | *See &gt;argon2:lanes&gt;*      | The number of parallel chains to run at once.
threads    | Number | *See &gt;argon2:threads&gt;*    | The number of threads that generating an Argon2id hash can spawn.
length     | Number | *See &gt;argon2:length&gt;*     | The length of the output in bytes.
saltlength | Number | *See &gt;argon2:saltlength&gt;* | The length of the salt in bytes.
version    | Number | *See &gt;argon2:version&gt;*    | The version of the Argon2id algorithm to use.

The version field should be set to one of the following values:

Value  | Description
------ | -----------
10     | Use version 1.0 of the Argon2id algorithm.
13     | Use version 1.3 of the Argon2id algorithm.

##### Example Usage

```xml
<argon2id memory="128MB"
          iterations="3"
          lanes="1"
          threads="1"
          length="32"
          saltlength="16"
          version="13">
```
