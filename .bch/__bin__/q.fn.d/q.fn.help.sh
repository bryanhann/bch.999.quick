#!/usr/bin/env  bash
[ -z $1 ] && {
cat<<USAGE
$(basename $BASH_SOURCE) (version zero)
usage:
    $(basename $BASH_SOURCE) NAME

Give help on bash function NAME
USAGE
return
}

declare -f $1 | q.fn.help.py

