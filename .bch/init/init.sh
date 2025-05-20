#!/usr/bin/env bash

:::debug::: ++[${BASH_SOURCE[0]}]

for pth in $(ls $(dirname ${BASH_SOURCE[0]})/[0-9]*); do
    #. $pth ${BASH_SOURCE[1]}
    :::debug::: . $pth
    . $pth
done

:::debug::: --[${BASH_SOURCE[0]}]

