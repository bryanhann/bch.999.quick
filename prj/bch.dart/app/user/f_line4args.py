#!/usr/bin/env python3
import constants as CC
import util as UU
 
def line4args(*args):
    return CC.SPACE.join(UU.lmap(str,args))

