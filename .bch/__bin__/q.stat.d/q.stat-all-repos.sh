#!/usr/bin/env bash

case .$1 in .-h|.--help)cat<<EOF;return;;esac
usage:
    . $(basename ${BASH_SOURCE[0]})
description:
    show the status of git repos directly under:
        ${BCH_000_BCH_ROOT}
        ~/.prj
        ~
EOF
. q.stat4root.sh ~/.local/share
. q.stat4root.sh ~/prj
. q.stat4root.sh ~
. q.stat4root.sh ${BCH_000_BCH_ROOT}
