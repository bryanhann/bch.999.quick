from pathlib import Path
from importlib import import_module

def modnames4path(path):
    for script in path.glob('f_*.py'):
        yield script.name[:-3]

def goodname(name): 
    return not name.startswith('_')

def goodattr(attr):
    fntype=type(lambda : None)
    if type(attr)==fntype:
        return True
    return False

def names4modname(modname):
    mod = import_module(modname)
    for name in dir(mod):
        attr = getattr(mod,name)
        if not goodname(name): continue
        if not goodattr(attr): continue
        yield name

def dopath(path):
    for modname in modnames4path(path):
        for name in names4modname(modname):
            yield f"from {modname} import {name}"
