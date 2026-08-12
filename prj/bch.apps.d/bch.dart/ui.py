#!/usr/bin/env python3
import sys
import user as USER
import constants as CC
import stamp as STAMP
import darts as DART

from files import darts4stdin
import files as FF


def new(*args):
    first = USER.line4args(*args)
    rest = USER.lines4user()
    lines = [ first ] + rest
    dart = DART.dart4lines( lines )
    FF.write4dart(dart)




