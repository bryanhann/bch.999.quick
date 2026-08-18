#!/usr/bin/env python3
import fire
from self import SELF
NAME=SELF['SELF_NAME']
print( f"{SELF=}" )
from ui import *
if __name__=='__main__':
    fire.Fire(name=NAME)
