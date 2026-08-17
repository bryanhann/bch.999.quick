q_go () {
    [ $1. == . ] && { declare -F | grep $FUNCNAME ; return; }
    ${FUNCNAME[0]}_$*
}
