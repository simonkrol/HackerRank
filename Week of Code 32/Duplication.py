#!/bin/python3

import sys

def duplication(x, s):
    while(len(s)<x+1):
        t=s
        for i in t:
            s+=str(1-int(i))
    return s[x]
            
    # Complete this function

q = int(input().strip())
s='0'
for a0 in range(q):
    x = int(input().strip())
    result = duplication(x, s)
    print(result)
