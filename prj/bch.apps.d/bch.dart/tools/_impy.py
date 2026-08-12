def modnames4pth(pth):
    for script in pth.glob('f_*.py'):
        yield script.name[:-3]
def goodname(name): 
    return not name.startswith('_')
def goodattr(attr):
    fntype=type(lambda : None)
    if type(attr)==fntype:
        return True
    return False
def names4modname(modname):
    fntype=type(lambda : None)
    from importlib import import_module
    mod = import_module(modname)
    for name in dir(mod):
        attr = getattr(mod,name)
        if not goodname(name): continue
        if not goodattr(attr): continue
        yield name
def lines4path(path):
    for modname in modnames4pth(path):
        for name in names4modname(modname):
            yield f"from {modname} import {name}"
def lmap(fn,seq):
     return list(map(fn,seq))
from pathlib import Path
def do__file__(file):
    yield from lines4path(Path(file).parent)
__file = do__file__
