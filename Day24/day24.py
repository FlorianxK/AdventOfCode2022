from collections import defaultdict, deque
import math
from typing import *

def dayTwentyFour():
    tornados = defaultdict(set)
    arr = []
    #read
    with open("Day24/24_2.txt") as file:
        for i,line in enumerate(file.read().splitlines()[1:-1]):
            line = line[1:-1]
            arr.append(line)
            for j,c in enumerate(line):
                if c in "<>^v":
                    tornados[c].add( (i,j) )

    m,n = len(arr),len(arr[0])
    start = (-1,0)
    end = (m,n-1)
    moves = {'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1)}
    #(i,j,time)
    q = deque([(start[0],start[1],0)])
    seen = set()
    lcm = m*n//math.gcd(m,n)

    while q:
        i,j,time = q.popleft()

        time += 1
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(0,0)]:
            ni,nj = i+di,j+dj

            if (ni,nj) == end:
                return time

            if (ni,nj) == start:
                key = (ni,nj,time%lcm)
                if key in seen:
                    continue
                seen.add(key)
                q.append((ni,nj,time))
            elif 0<=ni<m and 0<=nj<n:
                for c,(ti,tj) in moves.items():
                    newTi = (ni - ti*time) % m
                    newTj = (nj - tj*time) % n
                    if (newTi,newTj) in tornados[c]:
                        break
                else:
                    key = (ni,nj,time%lcm)
                    if key in seen:
                        continue
                    seen.add(key)
                    q.append((ni,nj,time))

def dayTwentyFour2():
    tornados = defaultdict(set)
    arr = []
    #read
    with open("Day24/24_2.txt") as file:
        for i,line in enumerate(file.read().splitlines()[1:-1]):
            line = line[1:-1]
            arr.append(line)
            for j,c in enumerate(line):
                if c in "<>^v":
                    tornados[c].add( (i,j) )

    m,n = len(arr),len(arr[0])
    start = (-1,0)
    ends = [(m,n-1),(-1,0)]
    moves = {'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1)}
    #(i,j,time,stage)
    q = deque([(start[0],start[1],0,0)])
    seen = set()
    lcm = m*n//math.gcd(m,n)

    while q:
        i,j,time,stage = q.popleft()

        time += 1
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(0,0)]:
            ni,nj = i+di,j+dj
            nstage = stage
            if (ni,nj) == ends[stage%2]:
                if stage == 2:
                    return time
                nstage += 1

            fail = False
            if (ni,nj) in ends:
                key = (ni,nj,time%lcm,nstage)
                if key in seen:
                    continue
                seen.add(key)
                q.append((ni,nj,time,nstage))
            elif 0<=ni<m and 0<=nj<n:
                for c,(ti,tj) in moves.items():
                    newTi = (ni - ti*time) % m
                    newTj = (nj - tj*time) % n
                    if (newTi,newTj) in tornados[c]:
                        fail = True
                        break

                if not fail:
                    key = (ni,nj,time%lcm,nstage)
                    if key in seen:
                        continue
                    seen.add(key)
                    q.append((ni,nj,time,nstage))

def main():
    print("Hallo")
    print(dayTwentyFour(), "ist die Lösung von Teil 1")
    print(dayTwentyFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()