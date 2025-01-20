#!/bin/sh
set -ex
./tools/find-broken-redirects
./tools/find-missing
./tools/find-orphans
./tools/find-whitespace
yamllint docs/
