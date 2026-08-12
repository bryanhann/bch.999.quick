#!/usr/bin/env python3

import datetime as DT
from stamp.formats import CANONICAL

def stamp(dt=None):
    if dt is None:
        dt = DT.datetime.now()
    return dt.strftime(CANONICAL)

