from collections import deque
from typing import *

def dayTwelve():
    arr = []
    i = 0
    #read
    with open("Day12/12_2.txt") as file:
        for line in file:
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
                elif line[j] == 'E':
                    end = (i,j)
            arr.append( list(line.strip()) )
            i += 1
    m,n = len(arr),len(arr[0])
    arr[start[0]][start[1]] = 'a'
    arr[end[0]][end[1]] = 'z'
    
    def bfs(start):
        seen = set()
        seen.add(start)
        q = deque([(start,0)])

        while q:
            curr = q.popleft()
            pos,steps = curr
            i,j = pos
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = di+i,dj+j

                if 0<=ni<m and 0<=nj<n and (ni,nj) not in seen:
                    if ord(arr[ni][nj]) <= ord(arr[i][j])+1:
                        seen.add( (ni,nj) )
                        q.append( ((ni,nj),steps+1) )
                        
                        if arr[ni][nj] == 'z' and (ni,nj) == end:
                            return steps+1
    res = bfs(start)
    return res

def dayTwelve2():
    arr = []
    starts = []
    i = 0
    #read
    with open("Day12/12_2.txt") as file:
        for line in file:
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
                elif line[j] == 'a':
                    starts.append((i,j))
                elif line[j] == 'E':
                    end = (i,j)
            arr.append( list(line.strip()) )
            i += 1
    m,n = len(arr),len(arr[0])
    arr[start[0]][start[1]] = 'a'
    starts.append(start)
    arr[end[0]][end[1]] = 'z'
    
    def bfs(start):
        seen = set()
        seen.add(start)
        q = deque([(start,0)])

        while q:
            curr = q.popleft()
            pos,steps = curr
            i,j = pos
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = di+i,dj+j

                if 0<=ni<m and 0<=nj<n and (ni,nj) not in seen:
                    if ord(arr[ni][nj]) <= ord(arr[i][j])+1:
                        seen.add( (ni,nj) )
                        q.append( ((ni,nj),steps+1) )
                        
                        if arr[ni][nj] == 'z' and (ni,nj) == end:
                            return steps+1
        return float('inf')

    minStart = float('inf')
    for s in starts:
        minStart = min(minStart,bfs(s))
    return minStart

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    print(dayTwelve2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()