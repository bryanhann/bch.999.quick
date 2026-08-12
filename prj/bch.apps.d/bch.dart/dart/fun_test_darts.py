#!/usr/bin/env python3
import util as UU

@UU.listify
def test_darts(n): 
    for ii in range(n):
        lines = f"this|is|line|{ii}".split('|')
        yield dart4lines( lines )
