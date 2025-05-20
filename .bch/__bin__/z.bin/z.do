#!/usr/bin/env bash

[ -z $1 ] && {
    z.today | grep "{do}"
    exit
}

bch.zjot new "{do}" $*
