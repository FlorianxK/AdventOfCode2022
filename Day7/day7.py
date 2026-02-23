from collections import defaultdict
from typing import *

def daySeven():
    cwd = root = defaultdict(list)
    stack = []
    #read
    with open("Day7/7_2.txt") as file:
        for line in file:
            line = line.strip()
            if line[0] == '$':
                if line[2] == 'c':
                    drcy = line[5:]
                    if drcy == '/':
                        cwd = root
                        stack = []
                    elif drcy == "..":
                        cwd = stack.pop()
                    else:
                        stack.append(cwd)
                        cwd = cwd[drcy]
            else:
                x,y = line.split()
                if x == "dir":
                    if y not in cwd:
                        cwd[y] = {}
                else:
                    cwd[y] = int(x)

    def solve(drcy:dict):
        if type(drcy) == int:
            return (drcy,0)
        size = 0
        res = 0
        for child in drcy.values():
            s,a = solve(child)
            size += s
            res += a
        if size <= 100_000:
            res += size
        return (size,res)
    
    res = solve(root)
    return res[1]

def daySeven2():
    cwd = root = {}
    stack = []
    #read
    with open("Day7/7_2.txt") as file:
        for line in file:
            line = line.strip()
            if line[0] == '$':
                if line[2] == 'c':
                    drcy = line[5:]
                    if drcy == '/':
                        cwd = root
                        stack = []
                    elif drcy == "..":
                        cwd = stack.pop()
                    else:
                        stack.append(cwd)
                        cwd = cwd[drcy]
            else:
                x,y = line.split()
                if x == "dir":
                    if y not in cwd:
                        cwd[y] = {}
                else:
                    cwd[y] = int(x)

    def size(drcy):
        if type(drcy) == int:
            return drcy
        return sum( [size(x) for x in drcy.values()] )
    
    th = size(root)-40_000_000

    def solve(drcy:dict):
        res = float("inf")
        val = size(drcy)
        if val >= th:
            res = val
        for child in drcy.values():
            if type(child) == int:
                continue
            q = solve(child)
            res = min(res,q)
        return res
    
    return solve(root)

def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()