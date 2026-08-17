#!/usr/bin/env bash
[ ! ${BASH_SOURCE[0]} == $0 ] &&  {
    echo bch.quick must be called, not sourced
    return
}
$BH1
this=$(0resolve $0)
if [ -f $this.d/$1 ]; then
    $this.d/$@
    exit $?
fi

0bold commands:
for name in $(ls $this.d); do
    0bold "    $(basename $this) $name"
done
