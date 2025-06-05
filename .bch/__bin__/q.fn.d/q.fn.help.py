#!/usr/bin/env python3
"""
Use:
    $ declare -f foo | {THIS_SCRIPT}

    Extract colon documentation for the bash function 'foo'.

If foo is defined as follows:

    foo () {
        : this is a docline
        local a
        :this is a second docline
    }

then the output is as follows:

    foo ()
        : this is a docline
        :this is a second docline
"""

import sys


def main():
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    if not lines:
        return
    name = lines.pop(0).split()[0]
    print( f"{name}()" )
    for line in lines:
        if line.startswith(': '):
            line = line[2:-1]
            print( f"\t{line}" )
        continue
if __name__ == '__main__':
    main()
