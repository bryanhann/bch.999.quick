#!/usr/bin/env python3
import sys
import util as UU
import user as USER
import constants as CC
import stamp as STAMP
import dart as DART

from files import dump
def __dump():
    paths = sorted( filter( UU.isfile, UU.walk(CC.ACC)))
    for path in paths:
        print( path.read_text().strip() )

def darts4stdin():
    for line in sys.stdin:
        yield DART.Dart(line)


def write4dart(dart):
    outfile = outfile4dart(dart)
    with open(outfile, 'a') as fd:
        fd.write(dart.raw+'\n')

def outfile4dart(dart):
    return CC.ACC/f"{dart.dateT}.{CC.EXT}"

def new(*args):
    first = USER.line4args(*args)
    rest = USER.lines4user()
    lines = [ first ] + rest
    dart = DART.dart4lines( lines )
    DART.write4dart(dart)




