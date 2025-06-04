#!/usr/bin/env bash

case .$1 in .|.-h|.--help)cat<<USAGE;return;;esac
usage:
    . $(basename ${BASH_SOURCE[0]}) <repo>
description:
    show the status of git repo.
USAGE

[ ! -d $1/.git ] && echo bad value && return

pushd $1 > /dev/null
    __git_ps1
    printf "\t$PWD\n"
popd > /dev/null
