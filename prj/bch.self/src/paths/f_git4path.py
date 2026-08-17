from .f_upline4path import upline4path

def git4path(path):
    for path in upline4path(path):
        if (path/'.git').is_dir():
           return path
