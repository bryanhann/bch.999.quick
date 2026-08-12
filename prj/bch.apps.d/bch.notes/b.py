#!/usr/bin/env python3
INC={}
for ii in range(24): 
    INC[ii]=15
INC[0] = 30
INC[1] = 30
INC[2] = 60
INC[3] = 60
INC[4] = 60
INC[5] = 60
INC[22] = 30
INC[23] = 30
import sys
LINES=0

def hhmm4hm(h,m):
    if m==0:
        return f"{h:02}{m:02}"    
    else: 
        return f" {m:02} "


def block(hour, inc=15):
     global LINES
     for hh in range(hour, hour+4):
          inc = INC[hh]
          for mm in range(0,60,inc):
               sys.stdout.write( hhmm4hm(hh,mm) )
               LINES = LINES + 1
     sys.stdout.write('_'*80 )
     LINES = LINES + 1





def tuples():
    for hh in range(2,26):
        hh = hh % 24
    #for hh in range(24):
        for mm in range(0,60, INC[hh]) :
             yield hh,mm

def hrule():
    sys.stdout.write('_'*80 + '\b' * 90) 

def main():
    acc = [ x for x in tuples() ]
    ret = len(acc)
    print()
    hrule()
    print()
    while acc:
        h,m = acc.pop(0)
        if (h%4==1 and acc and acc[0][0] > h) or not acc:
              hrule()
        print( ' '*10 + hhmm4hm(h,m))
    return ret
    block(0,30)
    block(4,30)
    block(8,15) 
    block(12,15) 
    block(16,15) 
    block(20,15) 

if __name__=='__main__':
    lines=main()
    sys.stderr.write(f'lines: {lines}')
