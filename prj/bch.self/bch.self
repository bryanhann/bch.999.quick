#!/usr/bin/env bash
# #bch:command=True
$BH1
this=$(0resolve $0)
uv run $(dirname $this)/src/$(basename $this) $*
exit

app=
args=


B=$(dirname $this)/bin
app=$(echo$B
$B/app4name $1
read
[ ! ${BASH_SOURCE[0]} == $0 ] &&  {
    echo bch.quick must be called, not sourced
    return
}

$(dirname $this)/bin/app4name $1
read
if [ -f $this.d/$1 ]; then
    $this.d/$@
    exit $?
fi

0bold commands:
for name in $(ls $this.d); do
    0bold "    $(basename $this) $name"
done
