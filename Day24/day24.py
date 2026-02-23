from collections import deque
from typing import *

def dayTwentyFour():
    arr = []
    tornados = set()
    torn = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}
    i = 0
    #read
    with open("Day24/24.txt") as file:
        for line in file:
            arr.append( list(line.strip()) )
            for j in range(len(line)):
                if line[j] in "<>^v":
                    tornados.add( (i,j,arr[i][j]) )
            i += 1

    m,n = len(arr),len(arr[0])
    start = (0,1)
    end = (m-1,n-2)
    arr[start[0]][start[1]] = 'S'
    arr[end[0]][end[1]] = 'E'

    def moveTornado():
        newTorn = set()
        for i,j,comp in tornados:
            di,dj = torn[comp]
            ni,nj = i+di,j+dj
            if arr[ni][nj] == '#':
                if comp == '<':
                    nj = n-2
                elif comp == '>':
                    nj = 1
                elif comp == '^':
                    ni = m-2
                elif comp == 'v':
                    ni = 1
            newTorn.add( (ni,nj,comp) )
        return newTorn

    def movePlayer(q):
        # 2 possiblities: deque (i,j,time) wait or move on possible next -> do bfs and pop and add pop and all free to queue until one reaches E
        newQ = deque([])
        while q:
            i,j,time = q.popleft()
            #stand still if possible
            if (i,j) not in tornados:
                newQ.append( (i,j,time+1) )
            #look if move possible
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0 <=nj<n:
                    #found end
                    if arr[ni][nj] == 'E':
                        return deque([(ni,nj,time+1)]),True

                    if arr[ni][nj] == '#' or (ni,nj) in tornados:
                        continue
                    
                    newQ.append( (ni,nj,time+1) )
                
        return newQ,False

    q = deque([(start[0],start[1],0)])
    while True:
        tornados = moveTornado()
        q,found = movePlayer(q)

        if found:
            break
    return q[0][2]

def dayTwentyFour2():
    pass

def main():
    print("Hallo")
    print(dayTwentyFour(), "ist die Lösung von Teil 1")
    #print(dayTwentyFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()