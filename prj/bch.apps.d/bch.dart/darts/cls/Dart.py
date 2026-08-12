#!/usr/bin/env python3

from stamp import Stamp
PIPE='|'
#class DartError(Exception):
from .DartError import DartError

class Dart:
    def __init__(self, line):
        if not (line and line[0] in '12'):
            raise DartError( f'bad line: [{repr(line)}]' )
        self._raw = line.strip()
    def __eq__(self, other): return self.raw == other.raw
    def __repr__(self):      return f"Dart('{self.raw}')"

    @property
    def raw(self): return self._raw
    
    @property
    def parts(self): return self.raw.split(PIPE)

    @property
    def stamp(self): return self.parts[0]

    @property
    def Stamp(self): return Stamp(self.stamp)

    @property
    def dateT(self): return self.Stamp.dateT
