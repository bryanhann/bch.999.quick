#!/usr/bin/env bash
case .$1 in .|.-h|.--help)cat<<USAGE;return;;esac
usage:
    . $(basename ${BASH_SOURCE[0]}) <dir>
description:
    show the status of git repos directly under <dir>
USAGE

my_git_stat () {
    pushd $(dirname $1) > /dev/null
    __git_ps1
    printf "\t$PWD\n"
    popd > /dev/null
}

_map () {
    local fn=$1; shift
    for x in $*; do $fn $x; done
}

_map my_git_stat $(find $1 -maxdepth 2 -name .git | sort)


