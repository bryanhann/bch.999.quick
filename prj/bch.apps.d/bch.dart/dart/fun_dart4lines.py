#!/usr/bin/env python3
from stamp import Stamp
from dart import Dart
PIPE='|'
def dart4lines(lines):
    lines = [ Stamp().raw ] + lines
    text = PIPE.join(lines)
    return Dart(text)

