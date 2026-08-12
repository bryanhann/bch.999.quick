#!/usr/bin/env python3
import sys
import util as UU
from constants import NOTES

SPACE=' '

EXT = 'kjot'
ACC = UU.goodfolder(NOTES/f"acc.{EXT}")

def day4path(path):
    assert path.is_file()
    day=path.name[:9]
    assert day.startswith('20')
    assert day.endswith('T')
    return day

def stow4acc(acc):
    assert acc.name.startswith('acc.')
    for src in filter( UU.isfile, acc.glob('20*T*')):
        dst = str( UU.goodfolder( acc/day4path(src) )/src.name )
        print( f"stowing\n\t{src}\n\t->{dst}" )
        src.rename(dst)

def stow():
    stow4acc(ACC)
def note(*args,tag='x'):
    fname = f"{UU.stamp()}.{EXT}!{tag}"
    outfile = ACC/fname
    lines = [fname, ' '.join(args) ]  + UU.prompt_lines()
    text = UU.text4lines(lines)
    outfile.write_text(text)

def dump():
    paths = sorted( filter( UU.isfile, UU.walk(NOTES)))
    for path in paths:
        UU.bold(path)
        print( path.read_text().strip() )
