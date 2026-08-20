import os
from pathlib import Path
from pprint import pprint
import colorama as CC
def bold(text):
    return f"{CC.Style.BRIGHT}{text}{CC.Style.NORMAL}"
class This(dict):
    def __init__(self):
        prefix = os.environ['THIS']
        for key,val in os.environ.items():
            if key.startswith(prefix):
                shortkey = '_'.join(key.split('_')[2:])
                if shortkey:
                    self[shortkey] = val
    def __getattr__(self, name):
        return self[name]
THIS = This()

class My:
    def __init__(self):
        self._env = THIS
    @property
    def env(self): return self._env 
    @property
    def name(self): return self._env.NAME 
    def dump(self):
        print( f"{bold('MY ENVIRONMENT')}" )
        pprint( self._env )
        print( f"{bold('MY CALLBACK FILE')}" )
        print( Path(self._env.CALLBACK).read_text() )
    def cb_append(self, line):
        with open(self._env.CALLBACK, 'a') as fd:
            fd.write(f"{line}\n") 
    @property
    def _cbpath(self):
        return Path(self._env.CALLBACK) 
MY = My()
