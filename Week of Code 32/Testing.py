#!/bin/python3

import sys
def seeding(rlist, g, seed, p):
    r=(rlist[0]*g+seed)%p
    while(r not in rlist):
        rlist.append(r)
        r=(r*g+seed)%p
    return rlist.index(r)

def getPath(num, rlist,start,destination):

    rlist=[r_0]
    rindex=seeding(rlist,3,4,7)
    period=len(rlist)-rindex

    currentnodes={start}
    pastnodes=currentnodes
    tempnodes=set()
    time=0
    while(True):
        if(destination in currentnodes):
            return time
        if(len(currentnodes)==0):
            return -1
        for node in currentnodes.copy():
            noderange=rlist[(node-rindex)%period+rindex]
            for newnode in range(-noderange, noderange+1):
                if(newnode!=0):
                    newnode=(node+newnode)%num
                    tempnodes.add(newnode)
        tempnodes=tempnodes.difference(pastnodes)
        pastnodes=tempnodes|pastnodes
        currentnodes=tempnodes
        time+=1






r_0=3
g=5
seed=6
p=15
rlist=seeding([r_0],g,seed,p)
period=len(rlist)-rindex
for i in range(30):
    print(i,":",rlist[(i-rindex)%period+rindex], sep="")
#print(getPath(n,rlist,s,t))