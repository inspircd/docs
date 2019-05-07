---
title: Module Details (pbkdf2)
---

## The "pbkdf2" Module

### Description

This module allows other modules to generate [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) hashes.

### Configuration

To load this module use the following `<module>` tag:

```xml
<module name="pbkdf2">
```

#### `<pbkdf2>`

The `<pbkdf2>` tag defines settings about how the pbkdf2 module should behave. This tag can only be defined once.

Name       | Type   | Default Value | Description
---------- | ------ | ------------- | -----------
iterations | Number | 12288         | The number of iterations of the hashing function that should be performed.
length     | Number | 32            | The length of the derived key.

##### Example Usage

```xml
<pbkdf2 iterations="12288"
        length="32">
```

The `<pbkdf2prov>` tag defines settings for a specific hash algorithm. This tag can be defined as many times as required.

Name       | Type   | Default Value | Description
---------- | ------ | ------------- | -----------
hash       | Text   | *None*        | **Required!** The name of the hash algorithm to configure.
iterations | Number | 12288         | The number of iterations of the hashing function that should be performed.
length     | Number | 32            | The length of the derived key.

##### Example Usage

```xml
<pbkdf2prov hash="sha256"
            iterations="12288"
            length="32">
```
