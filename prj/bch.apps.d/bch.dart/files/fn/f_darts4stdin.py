#!/usr/bin/env python3

import sys

from darts import Dart

def darts4stdin():
    for line in sys.stdin:
        yield Dart(line)

