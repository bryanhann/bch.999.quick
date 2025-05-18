#!/usr/bin/env bash

:::debug::: ++[${BASH_SOURCE[0]}] [$@]
for pth in $(ls $(dirname ${BASH_SOURCE[0]})/[0-9]*); do
    :::debug::: . $pth ${BASH_SOURCE[1]}
    . $pth ${BASH_SOURCE[1]}
done
:::debug::: ++[${BASH_SOURCE[0]}] [$@]

