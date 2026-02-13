from collections import deque
from typing import *

def dayTwentyTwo():
    elves = set()
    i = 0
    #read
    with open("Day23/23_2.txt") as file:
        for line in file:
            line = line.strip()
            for j in range(len(line)):
                if line[j] == '#':
                    elves.add( (i,j) )
            i += 1
    def move(dirs):
        #dirs = ['N','S','W','E']
        lookup = {'N':[(-1,0),(-1,-1),(-1,1)],'S':[(1,0),(1,-1),(1,1)],'E':[(0,1),(-1,1),(1,1)],'W':[(0,-1),(-1,-1),(1,-1)]}
        nextElves = set()
        # k=to , v=from
        propMove = DefaultDict(list)
        for i,j in elves:
            ngh = False
            # look for neighbour
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(-1,1),(1,-1)]:
                ni,nj = i+di,j+dj
                if (ni,nj) in elves:
                    ngh = True
                    break
            # won't move
            if ngh == False:
                nextElves.add( (i,j) )
                continue
            
            # propose move
            moved = False
            for comp in dirs:
                free = True
                for di,dj in lookup[comp]:
                    ni,nj = i+di,j+dj
                    if (ni,nj) in elves:
                        free = False
                        break
                if free:
                    if comp == 'N':
                        propMove[(i-1,j)].append( (i,j) )
                    elif comp == 'S':
                        propMove[(i+1,j)].append( (i,j) )                    
                    elif comp == 'W':
                        propMove[(i,j-1)].append( (i,j) )    
                    elif comp == 'E':
                        propMove[(i,j+1)].append( (i,j) )
                    moved = True
                    break
            
            if moved == False:
                nextElves.add( (i,j) )
        
        for k,v in propMove.items():
            if len(v) == 1:
                nextElves.add(k)
            else:
                for coord in v:
                    nextElves.add(coord)
        return nextElves

    rounds = 10
    dirs = deque(['N','S','W','E'])
    for _ in range(rounds):
        elves = move(dirs)
        front = dirs.popleft()
        dirs.append(front)
    
    minI = float("inf")
    minJ = float("inf")
    maxI = -float("inf")
    maxJ = -float("inf")
    #calc rectangle
    for i,j in elves:
        minI = min(minI,i)
        minJ = min(minJ,j)
        maxI = max(maxI,i)
        maxJ = max(maxJ,j)

    return (maxI-minI+1)*(maxJ-minJ+1)-len(elves)

def dayTwentyTwo2():
    elves = set()
    i = 0
    #read
    with open("Day23/23_2.txt") as file:
        for line in file:
            line = line.strip()
            for j in range(len(line)):
                if line[j] == '#':
                    elves.add( (i,j) )
            i += 1
    def move(dirs):
        #dirs = ['N','S','W','E']
        lookup = {'N':[(-1,0),(-1,-1),(-1,1)],'S':[(1,0),(1,-1),(1,1)],'E':[(0,1),(-1,1),(1,1)],'W':[(0,-1),(-1,-1),(1,-1)]}
        nextElves = set()
        # k=to , v=from
        propMove = DefaultDict(list)
        for i,j in elves:
            ngh = False
            # look for neighbour
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(-1,1),(1,-1)]:
                ni,nj = i+di,j+dj
                if (ni,nj) in elves:
                    ngh = True
                    break
            # won't move
            if ngh == False:
                nextElves.add( (i,j) )
                continue
            
            # propose move
            moved = False
            for comp in dirs:
                free = True
                for di,dj in lookup[comp]:
                    ni,nj = i+di,j+dj
                    if (ni,nj) in elves:
                        free = False
                        break
                if free:
                    if comp == 'N':
                        propMove[(i-1,j)].append( (i,j) )
                    elif comp == 'S':
                        propMove[(i+1,j)].append( (i,j) )                    
                    elif comp == 'W':
                        propMove[(i,j-1)].append( (i,j) )    
                    elif comp == 'E':
                        propMove[(i,j+1)].append( (i,j) )
                    moved = True
                    break
            
            if moved == False:
                nextElves.add( (i,j) )
        
        for k,v in propMove.items():
            if len(v) == 1:
                nextElves.add(k)
            else:
                for coord in v:
                    nextElves.add(coord)
        return nextElves

    round = 0
    dirs = deque(['N','S','W','E'])
    while True:
        round += 1
        nextElves = move(dirs)
        if elves == nextElves:
            return round
        else:
            elves = nextElves

        front = dirs.popleft()
        dirs.append(front)

def main():
    print("Hallo")
    print(dayTwentyTwo(), "ist die Lösung von Teil 1")
    print(dayTwentyTwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()