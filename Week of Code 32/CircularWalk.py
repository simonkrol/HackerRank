#!/bin/python3

import sys

def circularWalk(n, s, t, r_0, g, seed, p):
    rs=[r_0]
    for i in range(0, n-1):
        rs.append((rs[i]*g+seed)%p)
    time=0
    if(s==t):
        return 0
    spot=set()
    spot.add(s)
    sofar=spot
    while(True):
        time+=1
        spot=find_spot(n,spot,rs)
        spot=spot.difference(sofar)
        sofar=sofar|spot
        if(t in spot):
            return time
        elif(len(spot)==0):
            return -1
            
    
def find_spot(n,spot,rs):
    spots=set()
    for i in list(spot):
        ran=rs[i]
        for j in range(-ran, ran+1):
            spots.add((i+j)%n)
    return spots

n, s, t = input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)

