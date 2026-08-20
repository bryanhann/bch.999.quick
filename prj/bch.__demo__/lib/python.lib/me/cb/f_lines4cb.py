#!/usr/bin/env python3
from me import MY

def lines4cb():
    text = MY._cbpath.read_text()
    lines = text.split('\n')
    assert lines[-1]==''
    del lines[-1]
    del lines[0]
    return lines
