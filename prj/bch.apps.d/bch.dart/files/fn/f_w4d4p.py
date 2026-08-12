#!/usr/bin/env python3

def w4d4p(dart, path):
    with open(path, 'a') as fd:
        fd.write(dart.raw + '\n')

