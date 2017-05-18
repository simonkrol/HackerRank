#!/bin/python3

import sys

def getMaxMonsters(n, hit, t, h):
    monster=0
    h=sorted(h)
    for i in range(t):
        h[monster]-=hit
        if(h[monster]<=0):
            monster+=1
    return monster
        

n, hit, t = input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = list(map(int, input().strip().split(' ')))
result = getMaxMonsters(n, hit, t, h)
print(result)
