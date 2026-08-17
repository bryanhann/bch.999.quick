#!/usr/bin/env bash
source $(dirname ${BASH_SOURCE[0]})/fn.sh
src_folder () {
    for name in $(ls $1 | grep ^[0-9] | sort); do
        pth=$1/$name
        [ -f $pth ] && [ -f ~/DEBUG ] && echo dbg [QUICK]${pth#*init.d}
        [ -f $pth ] && . $pth
        [ -d $pth ] && $FUNCNAME $pth
    done
}

here=$(dirname ${BASH_SOURCE[0]})
base=$(dirname $(dirname $here))
src_folder $(dirname ${BASH_SOURCE[0]})

