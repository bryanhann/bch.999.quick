from pathlib import Path
import os
BCH=Path(os.environ['BH0_BCH'])

class Repo:
    """
    export
    """
    def matches(self, name):
        return self.name.startswith(name)
    def __init__(self, root):
        self._root = root
    def __repr__(self):
        return f"Repo({str(self.root)})"
    @property
    def prj(self):
        prj = self.root/'prj'
        return prj.is_dir() and prj or None
    @property
    def root(self): return self._root
    @property
    def name(self): 
        name = self._root.name
        parts = name.split('.')
        return '.'.join(parts[2:])
    def exports(self):
        for pth in self.root.glob('**'): 
            yield pth
    def dbg(self): print( f"""{self}
        {self.root=}
        {self.name=}
        """)
REPOS  = [ Repo(x) for x in BCH.glob('*') ]

