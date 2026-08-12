#!/usr/bin/env python3
import util as UU
from .dart4lines import dart4lines

@UU.listify
def sample_darts(n=10): 
    for ii in range(n):
        lines = f"this|is|line|{ii}".split('|')
        yield dart4lines( lines )
