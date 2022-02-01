---
title: InspIRCd Spanning Tree Protocol &mdash; Concepts
---

## Concepts

{! server/_dev.md !}

This page explains concepts relating to the InspIRCd Spanning Tree protocol.

### Message Routing

InspIRCd supports three types of message routing.

#### Broadcast

Routed to every server on the network. You must process the message locally and then forward it to every server other than the sender. May be sent encapsulated in which case it is okay to disregard it instead.

#### Message

Routed to a glob mask, a user, or a channel.

If the target is a glob mask then you should process it locally if your server name matches the pattern and then forward to all servers that match the specified pattern.

If the target is a user on your server then you should process it locally.

If the target is a user on another server you should forward it to that server.

If the target is a channel you should process it locally if your server contains users in that channel and then forward it to all servers that have a user on that channel.

#### Unicast

Routed to a specific server. If your server is the target then you should process it locally. Otherwise, you should forward it to the appropriate server. May be sent encapsulated in which case it is okay to disregard it instead.

### UUIDs

As referring to users by their nickname may cause race conditions when they change it the server protocol refers to users using unique immutable identifiers that last for their entire connection and are effectively never reused. This identifier is known as a UUID (unique user identifier) and is made up of two segments:

- Three characters in the format `[0-9][A-Z0-9]{2}` that uniquely identify the server the user is connecting from. This is known as a SID (server identifier).

- Six characters in the format `[A-Z0-9]{6}` that uniquely identify the user on the server they are connected to. This is known as a UID (user identifier).

As nicknames beginning with a number are reserved and not normally usable a user may use, or in the case of nickname collisions be forced to use, their UUID as their nickname. You should make sure your software can handle this.
