#!/usr/bin/env python3

from pathlib import Path

import colorama

from . import fns4path

F=colorama.Fore
S=colorama.Style

def bold(text):  return f'{S.BRIGHT}{text}{S.RESET_ALL}'
def green(text): return bold(f'{F.GREEN}{text}{F.RESET}')
def red  (text): return bold(f'{F.RED}{text}{F.RESET}')


PASS=green('PASS')
FAIL=red('FAIL')

def exercise4fn(fn):
    mod  = fn.__module__.split('.')[-1]
    desc = f'[{mod}.{fn.__name__}]' 
    doc  = str(fn.__doc__).split('\n')[0] or 'no doc'
    try:
        fn()
        print( f'{PASS} {desc} {doc}' )
    except Exception as foo:
        exc=foo
        print( f'{FAIL} {desc} {doc} [{bold(exc)}]' )


def check4mods(*mods):
    TAGS="sane sanity check".split()
    def sane(obj): return any( tag in str(obj.__doc__) for tag in TAGS ) 
    for mod in mods:
        print( bold(f'CHECKING MODULE: {mod.__name__}'))
        path = Path(mod.__file__).parent
        for fn in filter( sane, fns4path(path)):
            exercise4fn(fn)

