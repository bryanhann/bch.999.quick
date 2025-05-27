#!/usr/bin/env bash
. q.source
. bch.vendor.bash_colors.sh
touch ${Q_PROMPT}
a=$(cat $Q_PROMPT)
[ -z $a ] && exit
echo
clr_red  $a
