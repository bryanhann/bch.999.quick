#!/usr/bin/env bash


export BCH_QUICK__root=$(dirname $(dirname ${BASH_SOURCE[0]}))
export BCH_QUICK__bin=${BCH_QUICK__root}/.bch.bin
export BCH_QUICK__lbin=${BCH_QUICK__root}/.bch.lbin
export BCH_QUICK__files=${BCH_QUICK__root}/.bch.files
export BCH_QUICK__init=${BCH_QUICK__root}/.bch/init/init.sh

. $(dirname ${BASH_SOURCE[0]})/init/fn.sh
. $(dirname ${BASH_SOURCE[0]})/init/init.sh

::lbin:: ${BCH_QUICK__lbin}
