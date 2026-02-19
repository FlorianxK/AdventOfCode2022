from typing import *

def dayFourteen():
    filled = set()
    void = 0
    #read
    with open("Day14/14_2.txt") as file:
        for line in file:
            line = line.strip().split(" -> ")
            vals = []
            for v in line:
                x,y = [int(x) for x in v.split(',')]
                vals.append((x,y))
            
            for (x1,y1),(x2,y2) in zip(vals,vals[1:]):
                if x1 > x2:
                    x1,x2 = x2,x1
                if y1 > y2:
                    y1,y2 = y2,y1
                for x in range(x1,x2+1):
                    for y in range(y1,y2+1):
                        filled.add( (x,y) )
                        void = max(void,y+1)
    
    time = 0
    while True:
        s = [500,0]
        while True:
            if s[1] >= void:
                return time
            #down
            if (s[0],s[1]+1) not in filled:
                s[1] += 1
                continue
            #down-left
            if (s[0]-1,s[1]+1) not in filled:
                s[0] -= 1
                s[1] += 1
                continue
            #down-right
            if (s[0]+1,s[1]+1) not in filled:
                s[0] += 1
                s[1] += 1
                continue

            filled.add( tuple(s) )
            time += 1
            break

def dayFourteen2():
    filled = set()
    void = 0
    #read
    with open("Day14/14_2.txt") as file:
        for line in file:
            line = line.strip().split(" -> ")
            vals = []
            for v in line:
                x,y = [int(x) for x in v.split(',')]
                vals.append((x,y))
            
            for (x1,y1),(x2,y2) in zip(vals,vals[1:]):
                if x1 > x2:
                    x1,x2 = x2,x1
                if y1 > y2:
                    y1,y2 = y2,y1
                for x in range(x1,x2+1):
                    for y in range(y1,y2+1):
                        filled.add( (x,y) )
                        void = max(void,y+1)

    time = 0
    while True:
        s = [500,0]
        if tuple(s) in filled:
            return time
        
        while True:
            if s[1] >= void:
                break
            #down
            if (s[0],s[1]+1) not in filled:
                s[1] += 1
                continue
            #down-left
            if (s[0]-1,s[1]+1) not in filled:
                s[0] -= 1
                s[1] += 1
                continue
            #down-right
            if (s[0]+1,s[1]+1) not in filled:
                s[0] += 1
                s[1] += 1
                continue
            break
        filled.add( tuple(s) )
        time += 1

def main():
    print("Hallo")
    print(dayFourteen(), "ist die Lösung von Teil 1")
    print(dayFourteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()