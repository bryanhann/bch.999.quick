#!/usr/bin/env bash

for pth in $(ls $(dirname ${BASH_SOURCE[0]})/[0-9]*); do
    :::debug::: . $pth ${BASH_SOURCE[1]}
    . $pth ${BASH_SOURCE[1]}
done

