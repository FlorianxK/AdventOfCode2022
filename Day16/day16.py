from collections import deque
from typing import *

def daySixteen():
    valves = {}
    tunnels = {}
    #read
    with open("Day16/16_2.txt") as file:
        for line in file:
            l,r = line.strip().split("to")
            valve = l.split()[1]
            flow = int(l.split('=')[1].split(';')[0])
            targets = r.split(", ")
            targets[0] = targets[0].split()[1]
            valves[valve] = flow
            tunnels[valve] = targets
    
    dists = {}
    nonempty = []
    for valve in valves:
        if valve != "AA" and not valves[valve]:
            continue
        
        if valve != "AA":
            nonempty.append(valve)

        dists[valve] = {valve:0, "AA":0}
        visited = set()
        q = deque([(0,valve)])

        while q:
            distance,pos = q.popleft()
            for ngh in tunnels[pos]:
                if ngh in visited:
                    continue
                visited.add(ngh)
                if valves[ngh]:
                    dists[valve][ngh] = distance+1
                q.append( (distance+1,ngh) )

        del dists[valve][valve]
        if valve != "AA":
            del dists[valve]["AA"]

    idx = {}
    for i,element in enumerate(nonempty):
        idx[element] = i

    cache = {}
    def dfs(t,valve,bitmask):
        if (t,valve,bitmask) in cache:
            return cache[(t,valve,bitmask)]
        
        maxVal = 0
        for ngh in dists[valve]:
            bit = 1 << idx[ngh]
            if bitmask & bit:
                continue

            remTime = t-dists[valve][ngh]-1
            if remTime <= 0:
                continue
            maxVal = max( maxVal,dfs(remTime,ngh,bitmask|bit)+(valves[ngh]*remTime) )
        cache[(t,valve,bitmask)] = maxVal
        return maxVal
    
    return dfs(30,"AA",0)

def daySixteen2():
    valves = {}
    tunnels = {}
    #read
    with open("Day16/16_2.txt") as file:
        for line in file:
            l,r = line.strip().split("to")
            valve = l.split()[1]
            flow = int(l.split('=')[1].split(';')[0])
            targets = r.split(", ")
            targets[0] = targets[0].split()[1]
            valves[valve] = flow
            tunnels[valve] = targets
    
    dists = {}
    nonempty = []
    for valve in valves:
        if valve != "AA" and not valves[valve]:
            continue
        
        if valve != "AA":
            nonempty.append(valve)

        dists[valve] = {valve:0, "AA":0}
        visited = set()
        q = deque([(0,valve)])

        while q:
            distance,pos = q.popleft()
            for ngh in tunnels[pos]:
                if ngh in visited:
                    continue
                visited.add(ngh)
                if valves[ngh]:
                    dists[valve][ngh] = distance+1
                q.append( (distance+1,ngh) )

        del dists[valve][valve]
        if valve != "AA":
            del dists[valve]["AA"]

    idx = {}
    for i,element in enumerate(nonempty):
        idx[element] = i

    cache = {}
    def dfs(t,valve,bitmask):
        if (t,valve,bitmask) in cache:
            return cache[(t,valve,bitmask)]
        
        maxVal = 0
        for ngh in dists[valve]:
            bit = 1 << idx[ngh]
            if bitmask & bit:
                continue

            remTime = t-dists[valve][ngh]-1
            if remTime <= 0:
                continue
            maxVal = max( maxVal,dfs(remTime,ngh,bitmask|bit)+(valves[ngh]*remTime) )
        cache[(t,valve,bitmask)] = maxVal
        return maxVal
    
    b = (1 << len(nonempty))-1
    res = 0
    for i in range(b+1):
        res = max(res, dfs(26,"AA",i)+dfs(26,"AA",b^i) )
    return res

def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    print(daySixteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()