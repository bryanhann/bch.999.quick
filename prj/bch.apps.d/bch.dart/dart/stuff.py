#!/usr/bin/env python3
import util as UU
from stamp import Stamp
from constants import PIPE
def dart4lines(lines):
    lines = [ Stamp().raw ] + lines
    text = PIPE.join(lines)
    return Dart(text)


@UU.listify
def darts(): 
    for ii in range(10):
        lines = f"this|is|line|{ii}".split('|')
        yield dart4lines( lines )
