#!/usr/bin/env python3
import constants as CC
import util as UU

def lines4user():
    acc = []
    while not acc[-2:] == [ '', '' ]:
        acc.append( input( '> ') )
    return acc[:-2]
 
def line4args(*args):
    return CC.SPACE.join(UU.lmap(str,args))

