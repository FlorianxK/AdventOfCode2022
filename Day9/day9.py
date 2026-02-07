from typing import *

def dayNine():
    seen = set()
    seen.add( (0,0) )
    dire = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    hi,hj = 0,0
    ti,tj = 0,0
    #read
    with open("Day9/9_2.txt") as file:
        for line in file:
            line = line.strip().split()
            comp,move = line[0],int(line[1])
            di,dj = dire[comp]
            for _ in range(move):
                hi += di
                hj += dj

                #move tail
                dx = hi-ti
                dy = hj-tj
                if max(abs(dx),abs(dy)) > 1:
                    if dx != 0:
                        ti+=1 if dx > 0 else -1
                    if dy != 0:
                        tj += 1 if dy > 0 else -1

                    if (ti,tj) not in seen:
                        seen.add( (ti,tj) )
    return len(seen)

def dayNine2():
    seen = set()
    seen.add( (0,0) )
    dire = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
    hi,hj = 0,0
    parts = []
    knots = 9
    for _ in range(knots):
        parts.append([0,0])
    #read
    with open("Day9/9_2.txt") as file:
        for line in file:
            line = line.strip().split()
            comp,move = line[0],int(line[1])
            di,dj = dire[comp]
            for _ in range(move):
                hi += di
                hj += dj
                
                for i in range(len(parts)):
                    if i == 0:
                        prev = [hi,hj]
                    else:
                        prev = parts[i-1]
                    
                    #move parts
                    pi,pj = prev
                    ti,tj = parts[i]
                    dx = pi - ti
                    dy = pj - tj
                    if max(abs(dx), abs(dy)) > 1:
                        if dx != 0:
                            ti += 1 if dx > 0 else -1
                        if dy != 0:
                            tj += 1 if dy > 0 else -1
                    
                    if i == len(parts)-1:
                        if (ti,tj) not in seen:
                            seen.add( (ti,tj) )

                    parts[i] = [ti,tj]
    return len(seen)

def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()