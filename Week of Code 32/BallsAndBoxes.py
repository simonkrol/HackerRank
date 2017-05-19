#!/bin/python3

import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
numB = list(map(int, input().strip().split(' ')))
holdB = list(map(int, input().strip().split(' ')))
numC = []
for B_i in range(n):
   B_t = [int(B_temp) for B_temp in input().strip().split(' ')]
   numC.append(B_t)
def body(n,m,numB,holdB,numC):
    can=0
    allowed=True
    while(allowed):
        val=(max(numC[i]))#Get the value of the highest scoring box
        maxI=numC[i].index(val)#Get the index of the highest scoring box
        allowed=True
        if(val<=0):#Make sure that we have at least one value greater than 0, otherwise it wouldnt be worth placing
            return -1
        if(val+((holdB[maxI]-1)*abs(holdB[maxI]-1)>0)): #If our net gain is greater than our net loss, add the ball to the box
            can+=val
            holdB[maxI]-=1  #Set the score of that box to -1 because we cant place any more balls of that colour in there
            allowed=False
        numC[i][maxI]=-1
    return can
    

#n is the number of different colours 
#m is the number of boxes
#numB is a list of the number of balls of each colour(ie:len(numB)==n)
#holdB is a list of the number of balls each box can hold(len(holdB)==m)
#numC is a 2 dimensional array of the number of candies each colour in each box gets us
#No more than one of each colour can be in each box (Set value to -1 after placement)
#Order shouldnt matter
#Lose candies if place additional ones, check if gain makes it worth it
#Lost candies calculated at the end
candies=0
for i in range(n): #For each colour
    for j in range(numB[i]):#For each ball of that colour
        allowed=True
        c=body(n,m,numB,holdB,numC)
        if(c==-1):
            break
        candies+=c
for i in holdB:
    if(i<0):
        candies-=i**2
print(candies)
            
        