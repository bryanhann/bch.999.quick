#/usr/bin/env bash
bch_dart () { 
    real=$(readlink ${BASH_SOURCE[0]})
    local cmd=$1
    shift
    [ ! x$cmd == x  ] && source $real.d/$cmd "$@"
}
bch_dart .init 
bch_dart .env 
bch_dart .bch0 
bch_dart .init 
bch_dart .fds
bch_dart .exec $*

