from pathlib import Path
from .f_upline4path import upline4path
from .f_git4path import git4path

def __upline4path(path):
    while True:
         yield path
         if path==path.parent:
             break
         path=path.parent
def __git4path(path):
    for path in upline4path(path):
        if (path/'.git').is_dir():
           return path
