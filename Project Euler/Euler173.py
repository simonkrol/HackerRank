def getLaminae(n):
    numTiles=int(n/4)
    n=int(numTiles**(1/2))
    laminae=0
    for i in range(1, n+1):
        laminae+=int(numTiles/i)-i
    return laminae    
print(getLaminae(int(input())))      