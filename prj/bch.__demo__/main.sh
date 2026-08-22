#!/usr/bin/env bash

#:echo $(readlink ${BASH_SOURCE[0])
.  $(dirname $(readlink ${BASH_SOURCE[0]}))/.sys/first "$@"

. $this_sys/main "$@"

. $this_sys/last
