#!/usr/bin/env python3

import util as __UU
from darts import Dart as __Dart

@__UU.listify
def darts4path(path): 
    def isdart(raw):
        try:    __Dart(raw)
        except: return False
        return True
    return map(__Dart, filter(isdart, __UU.lines4path(path)))


