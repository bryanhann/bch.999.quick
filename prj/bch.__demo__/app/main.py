#!/usr/bin/env python3
import fire
name='foo'
from me import THIS
from me import MY as my
name = my.name
import ui.cmds
from ui import *

def die(err):
    exit(err)
if __name__=='__main__':
    fire.Fire(name=name)
