from typing import *

def daySeventeen():
    rocks = [
        [0,1,2,3],
        [1,1j,1+1j,2+1j,1+2j],
        [0,1,2,2+1j,2+2j],
        [0,1j,2j,3j],
        [0,1,1j,1+1j]
    ]
    #read
    with open("Day17/17_2.txt") as file:
        winds = [1 if x == '>' else -1 for x in file.read()]
    solid = {x-1j for x in range(7)}
    height = 0
    count = 0
    rIdx = 0
    rock = { x+2+(height+3)*1j for x in rocks[rIdx] }

    while count < 2022:
        for wind in winds:
            moved = {x+wind for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x-1j for x in rock}
            if moved & solid:
                solid |= rock
                height = max(x.imag for x in solid)+1
                count += 1
                if count >= 2022:
                    break
                rIdx = (rIdx+1)%5
                rock = { x+2+(height+3)*1j for x in rocks[rIdx] }
            else:
                rock = moved
    return int(height)

def daySeventeen2():
    rocks = [
        [0,1,2,3],
        [1,1j,1+1j,2+1j,1+2j],
        [0,1,2,2+1j,2+2j],
        [0,1j,2j,3j],
        [0,1,1j,1+1j]
    ]

    def summarize():
        o = [-20]*7
        for x in solid:
            r = int(x.real)
            i = int(x.imag)
            o[r] = max( o[r],i )
            
        top = max(o)
        return tuple(x-top for x in o)

    #read
    with open("Day17/17_2.txt") as file:
        winds = [1 if x == '>' else -1 for x in file.read()]
    solid = {x-1j for x in range(7)}
    height = 0
    count = 0
    rIdx = 0
    rock = { x+2+(height+3)*1j for x in rocks[rIdx] }
    seen = {}
    T = 1_000_000_000_000
    while count < T:
        for wi,wind in enumerate(winds):
            moved = {x+wind for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x-1j for x in rock}
            if moved & solid:
                solid |= rock
                height = max(x.imag for x in solid)+1
                count += 1
                if count >= T:
                    break
                rIdx = (rIdx+1)%5
                rock = { x+2+(height+3)*1j for x in rocks[rIdx] }
                key = (wi,rIdx,summarize())
                if key in seen:
                    lastCount,lastHeight = seen[key]
                    rem = T - count
                    rep = rem // (count-lastCount)
                    offset = rep*(height-lastHeight)
                    count += rep*(count-lastCount)
                    seen = {}
                seen[key] = (count,height)
            else:
                rock = moved
    return int(height+offset)

def main():
    print("Hallo")
    print(daySeventeen(), "ist die Lösung von Teil 1")
    print(daySeventeen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()