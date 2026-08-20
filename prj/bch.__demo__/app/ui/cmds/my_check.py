#!/usr/bin/env python3

from me.check import check4mods

def my_check(): 
    import me.checkthis as outer
    import me.checkthis.inner as inner
    check4mods(outer, inner)
