from pathlib import Path
import os
from .c_Repo import Repo
BCH=Path(os.environ['BH0_BCH'])
def list ():
    """
    export
    """
    yield from map(Repo, BCH.glob('*'))

def test_list():
    repos = [x for x in list() ]
    assert repos
