#!/usr/bin/env sh
echo "++[${BASH_SOURCE[0]}] [$@]" :stub-source:

__main () {
    echo "==[${FUNCNAME[0]}()] [$@]"
}

__null () {
    echo "==[${FUNCNAME[0]}()] [$@]"
}

__usage () {
    echo "==[${FUNCNAME[0]}()] [$@]"
}

case $1. in
    .) __null ;;
    -h.|--help.) __usage ;;
    *) __main ;;
esac

echo "--[${BASH_SOURCE[0]}]"
