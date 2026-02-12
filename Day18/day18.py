from collections import defaultdict, deque
from typing import *

def dayEighteen():
    faces = defaultdict(int)
    offsets = [ (0,0,0.5),(0,0.5,0),(0.5,0,0),(0,0,-0.5),(0,-0.5,0),(-0.5,0,0) ]
    #read
    with open("Day18/18_2.txt") as file:
        for line in file:
            vals = [int(x) for x in line.strip().split(',')]
            x,y,z = vals
            for dx,dy,dz in offsets:
                k = (x+dx,y+dy,z+dz)
                faces[k] += 1
    res = 0
    for v in faces.values():
        if v == 1:
            res += 1
    return res

def dayEighteen2():
    faces = defaultdict(int)
    minX=minY=minZ = float("inf")
    maxX=maxY=maxZ = -float("inf")
    offsets = [ (0,0,0.5),(0,0.5,0),(0.5,0,0),(0,0,-0.5),(0,-0.5,0),(-0.5,0,0) ]
    droplet = set()
    #read
    with open("Day18/18_2.txt") as file:
        for line in file:
            vals = [int(x) for x in line.strip().split(',')]
            droplet.add(tuple(vals))
            x,y,z = vals
            minX = min(minX,x)
            minY = min(minY,y)
            minZ = min(minZ,z)

            maxX = max(maxX,x)
            maxY = max(maxY,y)
            maxZ = max(maxZ,z)

            for dx,dy,dz in offsets:
                k = (x+dx,y+dy,z+dz)
                faces[k] += 1

    minX-=1
    minY-=1
    minZ-=1
    maxX+=1
    maxY+=1
    maxZ+=1

    q = deque([(minX,minY,minZ)])
    air = {(minX,minY,minZ)}
    while q:
        x,y,z = q.popleft()
        for dx,dy,dz in offsets:
            nx = x+dx*2
            ny = y+dy*2
            nz = z+dz*2
            k = (nx,ny,nz)
            if not (minX<=nx<=maxX and minY<=ny<=maxY and minZ<=nz<=maxZ):
                continue
            if k in droplet or k in air:
                continue
            air.add(k)
            q.append(k)
    
    free = set()
    for x,y,z in air:
        for dx,dy,dz in offsets:
            free.add( (x+dx,y+dy,z+dz) )
    
    res = 0
    for k in faces:
        if k in free:
            res += 1
    return res

def main():
    print("Hallo")
    print(dayEighteen(), "ist die Lösung von Teil 1")
    print(dayEighteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()