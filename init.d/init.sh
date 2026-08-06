#!/usr/bin/env bash
$BH1
here=$(dirname ${BASH_SOURCE[0]})
for name in $(ls $here | sort | grep ^[0-9]); do
    0bold ". [bch.quick]/init.d/$name"
    source $here/$name
done
