from pathlib import Path
import os
import commands as CMD
import repos as REPOS
import util as UTIL

def repos4name(name):
    """export"""
    for repo in REPOS.list():
        if repo.name.startswith(name):
            yield repo

def repo4name(name):
    """export"""
    try:
        return UTIL.unique(repos4name(name))
    except UTIL.UniqueExc:
        raise UTIL.UniqueExc( f"{name}  is ambigous" )
