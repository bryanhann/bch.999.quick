#!/usr/bin/env bash

verify () {
    got=$1
    exp=$2
    shift 2 
    cmp $got $exp 2> /dev/null &&  echo pass $* || echo fail $*
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

f_loopc () {
    case $1. in
        --upper.)
            while read line; do
                echo $line | tr '[:lower:]' '[:upper:]'
            done
            ;;
        --lower.)
            while read line; do
                echo $line | tr '[:upper:]' '[:lower:]'
            done
            ;;
    esac
}

f_argsc () {
    case $1. in
        --upper.)
            echo "$@" | tr '[:lower:]' '[:upper:]'
            ;;
        --lower.)
            echo "$@" | tr '[:upper:]' '[:lower:]'
            ;;
    esac
}

