#!/usr/bin/env bash

verify () {
    got=$1
    exp=$2
    shift 2 
    cmp $got $exp 2> /dev/null && pass $* || fail $*
}

pass () { echo pass: $* ; }
fail () { echo fail: $* ; }

f_loop () {
    while read line; do
        echo $line | tr '[:lower:]' '[:upper:]'
    done
}
f_args() {
    echo "$@" | tr '[:lower:]' '[:upper:]'
}
