#!/usr/bin/env python3
import sys
import constants as CC
import dart as DART
from freezegun import freeze_time
from util import lmap
from dart import Dart, DartError
import util as UU
import constants as CC
from constants import ACC
from stamp import Stamp
from constants import PIPE

@UU.listify
def darts4path(path): 
    def isdart(raw):
        try:    Dart(raw)
        except: return False
        return True
    return map(Dart, filter(isdart, UU.lines4path(path)))

def dump():
    for path in allfiles():
        print( path.read_text() + 'XXX')

def darts4stdin():
    for line in sys.stdin:
        yield Dart(line)


def write4dart4file(dart, file):
    with open(file, 'a') as fd:
        fd.write(dart.raw + '\n')


def write4dart(dart):
    outfile=CC.ACC/f"{dart.dateT}"
    outfile.touch()
    with open(outfile, 'a') as fd:
       fd.write(dart.raw + '\n')
def write4raw(raw):
    write4dart( Dart(raw) )

@UU.listify
def darts4path(path): 
    def isdart(raw):
        try:    Dart(raw)
        except: return False
        return True
    return map(Dart, filter(isdart, UU.lines4path(path)))



