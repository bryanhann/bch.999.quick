#!/usr/bin/env python3
import sys
from freezegun import freeze_time

from stamp import Stamp
@freeze_time("1970-01-01 15:16:17")
def test_zot(tmp_path):
    s=Stamp()
    assert s.raw == f"{s.left}T{s.right}"
    assert s.left == "19700101"
    assert s.right.startswith("151617")
    assert s.dt.year==1970
    assert s.dateT=="19700101T"
    assert s.human() == "1970-01-01-T-15:16:17:000000"

import util as UU
import constants as CC
import datetime as DT

FORMAT="%Y%m%dT%H%M%S%f"
HUMAN="%Y-%m-%d-T-%H:%M:%S:%f"

def stamp(dt=None):
    if dt is None:
        dt = DT.datetime.now()
    return dt.strftime(FORMAT)
class Stamp:
    def __init__(self, init=None):
        if init is None:
            init = DT.datetime.now()
        if isinstance(init, DT.datetime):
            self._raw = init.strftime(FORMAT)
        elif isinstance(init,str):
            self._raw = init.split('.')[0]
        else:
           raise AssertionError('Not reachable')
       

    def __repr__(self):
        return self.raw
    @property
    def left(self): 
        return self.raw.split('T')[0] 
    @property
    def right(self): 
        return self.raw.split('T')[1]
    @property
    def dt(self):
        return DT.datetime.strptime( self.raw, FORMAT )
    @property
    def dateT(self): 
        return self.left + 'T'
    @property
    def raw(self):
        return self._raw
    @classmethod
    def __new8now(cls): 
        return cls(raw8now())
        return cls(DT.datetime.now().strftime(FORMAT))
    def format(self, format):
        return self.dt.strftime(format)
    def human(self):
        return self.format(HUMAN)

