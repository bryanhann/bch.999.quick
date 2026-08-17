from pathlib import Path
from paths import git4path
LBIN=Path().home()/'.local/bin'
class Command:
    def __init__(self, link):
        self._link = link
    def __repr__(self):
        return f'Command({self.name})'
    @property
    def link(self): return self._link
    @property
    def real(self):
        if self._link.is_symlink():
            return self._link.readlink()
        return self._link
    def repo(self):
        return git4path(self.real)
    @property
    def name(self):
        return self._link.name
    def dbg(self):
        print(f"""{self}
        {self.real=}
        {self.link=}
        {self.repo()=}
        """)
def commands():
    return map( Command, LBIN.glob('bch.*') ) 


