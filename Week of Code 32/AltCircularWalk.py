#!/bin/python3

import sys
def seeding(rs, g, seed, p):
 #   for i in range(0,p+4):
 #       rs.append((rs[i]*g+seed)%p)
 #       print(i, rs[i])
     return rs

def circularWalk(num, start, term, r_0, g, seed, modp):
    rlist=[r_0]
    print(0,rlist[0])
 #   for i in range(1,modp+1):
    rlistperiod=0
    repeatsat=-1
    index = 1
    while(rlistperiod==0 and repeatsat==-1):
        newhops=(rlist[index-1]*g+seed)%modp
        if(newhops == rlist[index-1]):
            repeatsat = index-1
            print("repeatsat", repeatsat)
        if(newhops != r_0):
            rlist.append(newhops)
            print(index, rlist[index])
            index+=1
        if(newhops==r_0):
            rlistperiod=index
            print("period ",rlistperiod)
 #   rlist=seeding(rlist,g,seed,modp)
    time=0
    if(start==term):
        return 0
    spotset={start}
    sofar=spotset
    while(True):
        time+=1
        maximum=max(spotset)
  #      if(len(rlist)-1<maximum):
  #          rlist=seeding(rlist,g,seed,p,maximum)
        reachablespots=set()
        for i in list(spotset):
            if(rlistperiod!=0):
                ran=rlist[i%rlistperiod]
            elif(i>repeatsat):
                ran=rlist[repeatsat]
            else:
                ran=rlist[i]
            for j in range(-ran, ran+1):
                ad=((i+j)%n)
                reachablespots.add(ad)
        spotset=reachablespots.difference(sofar)
        if(term in spotset):
            return time
        if(len(spotset)==0):
            return -1
        sofar=sofar|spotset

n, s, t = input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
