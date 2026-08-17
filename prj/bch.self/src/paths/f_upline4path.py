from pathlib import Path

def upline4path(path):
    """
    export
    """
    while True:
         yield path
         if path==path.parent:
             break
         path=path.parent
