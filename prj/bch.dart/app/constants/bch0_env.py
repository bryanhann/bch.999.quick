#!/usr/bin/env python3
import os
from pathlib import Path
import util as UU

BCH0_DART = Path( os.environ.get(
    'BCH0_DART',
    Path.home()/'bch.DART.acc'
))

ACC=UU.mkdirs(BCH0_DART)
