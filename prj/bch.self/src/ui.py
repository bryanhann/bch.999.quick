from pathlib import Path
import os
import commands as CMD
import repos as REPOS
import paths as PP
from repos import repos4name
from repos import repo4name

def repo4name(name):
    print( REPOS.repo4name(name) )
def name4link(link):
    name = link.name
    if name.startswith('bch.'):
        return name[4:]
    return name

def commands():
    for cmd in CMD.commands():
        cmd.dbg()
def repos_list():
    """Gather all repos"""
    yield from REPOS.list()
def repos_dbg():
    """Gather all repos"""
    for repo in REPOS.list():
        repo.dbg()
def list():
    for mod in mods():
        print(mod.name)
def mods4name(name):
    for mod in mods():
        if mod.matches(name):
            yield mod


def path4app(app):
    pass    
