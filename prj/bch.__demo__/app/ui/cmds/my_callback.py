#!/usr/bin/env python3
from me import MY
def my_callback():
    MY.cb_append( '# this is an appended line' )
    MY.cb_append( '# this is another line' )
    MY.dump()
