#!/usr/bin/env python3

def goodfolder(folder):
    folder.is_dir() or folder.mkdir()
    return folder

def bold(text):
    from colorama import Style
    print( Style.BRIGHT + str(text) + Style.NORMAL)


def stamp():
    import datetime as DT
    return DT.datetime.now().strftime("%Y%m%dT%H%M%S%f")


def isfile(pth):
    return pth.is_file()

def walk(root):
    assert root.exists()
    yield root
    if root.is_dir():
        for pth in root.glob('*'):
            yield from walk(pth)

def prompt_lines():
    acc = []
    while not acc[-2:] == [ '', '' ]:
        acc.append( input( '> ') )
    return acc[:-2]
 
def text4lines( lines ):
    return '\n'.join(lines)+'\n' 

def strip4lines(lines): 
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop(-1)
    return lines


