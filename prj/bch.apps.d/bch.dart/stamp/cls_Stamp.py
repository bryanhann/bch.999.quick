#!/usr/bin/env python3
import stamp.formats as FF
import datetime as DT

class Stamp:
    def __init__(self, init=None):
        if init is None:
            init = DT.datetime.now()
        if isinstance(init, DT.datetime):
            self._raw = init.strftime(FF.CANONICAL)
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
        return DT.datetime.strptime( self.raw, FF.CANONICAL )
    @property
    def dateT(self): 
        return self.left + 'T'
    @property
    def raw(self):
        return self._raw
    @classmethod
    def __new8now(cls): 
        return cls(raw8now())
        return cls(DT.datetime.now().strftime(FF.CANONICAL))
    def format(self, format):
        return self.dt.strftime(format)
    def human(self):
        return self.format(FF.HUMAN)
