from collections import defaultdict, deque
from typing import *

def dayFive():
    #read
    with open("Day5/5_2.txt") as file:
        stacks,moves = file.read().split("\n\n")
    
    d = defaultdict(list)
    stacks = [list(s) for s in stacks.split('\n')]
    for j in range(len(stacks[-1])):
        if stacks[-1][j] != ' ':
            for i in range( len(stacks)-2,-1,-1 ):
                if stacks[i][j] != ' ':
                    d[stacks[-1][j]].append(stacks[i][j])

    moves = moves.split('\n')
    for move in moves:
        move = move.split(' ')
        amount = int(move[1])
        fromStack = move[3]
        toStack = move[-1]
        
        for _ in range(amount):
            elem = d[fromStack].pop()
            d[toStack].append(elem)

    res = ""
    for v in d.values():
        res += v[-1]
    return res

def dayFive2():
    #read
    with open("Day5/5_2.txt") as file:
        stacks,moves = file.read().split("\n\n")
    
    d = defaultdict(list)
    stacks = [list(s) for s in stacks.split('\n')]
    for j in range(len(stacks[-1])):
        if stacks[-1][j] != ' ':
            for i in range( len(stacks)-2,-1,-1 ):
                if stacks[i][j] != ' ':
                    d[stacks[-1][j]].append(stacks[i][j])

    moves = moves.split('\n')
    for move in moves:
        move = move.split(' ')
        amount = int(move[1])
        fromStack = move[3]
        toStack = move[-1]
        
        arr = deque([])
        for _ in range(amount):
            elem = d[fromStack].pop()
            arr.appendleft(elem)
        d[toStack].extend(arr)

    res = ""
    for v in d.values():
        res += v[-1]
    return res

def main():
    print("Hallo")
    print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()