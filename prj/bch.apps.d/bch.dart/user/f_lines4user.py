#!/usr/bin/env python3

def lines4user():
    acc = []
    while not acc[-2:] == [ '', '' ]:
        acc.append( input( '> ') )
    return acc[:-2]
 
