from typing import *

def dayFifteen():
    Y = 2000000
    lines = []
    intervals = []
    seen = set()
    unseen = set()
    #read
    with open("Day15/15_2.txt") as file:
        for line in file:
            line = line.split()
            sx = int(line[2][2:-1])
            sy = int(line[3][2:-1])
            bx = int(line[-2][2:-1])
            by = int(line[-1][2:])
            lines.append( (sx,sy,bx,by) )

    for sx,sy,bx,by in lines:
        manDist = abs(sx-bx)+abs(sy-by)
        rowY = manDist - abs(sy-Y)

        if rowY < 0:
            continue
        
        lx = sx-rowY
        ly = sx+rowY
        intervals.append( [lx,ly] )

        if by == Y:
            seen.add(bx)
    
    intervals.sort()
    q = []
    for l,r in intervals:
        if not q:
            q.append( [l,r] )
            continue
        qr = q[-1][1]
        if l > qr+1:
            q.append( [l,r] )
            continue
        q[-1][1] = max(qr,r)
    
    for l,r in q:
        for x in range(l,r+1):
            unseen.add(x)

    return len(unseen-seen)

def dayFifteen2():
    M = 4_000_000
    lines = []
    #read
    with open("Day15/15_2.txt") as file:
        for line in file:
            line = line.split()
            sx = int(line[2][2:-1])
            sy = int(line[3][2:-1])
            bx = int(line[-2][2:-1])
            by = int(line[-1][2:])
            lines.append( (sx,sy,bx,by) )
    
    for Y in range(M+1):
        intervals = []
        for sx,sy,bx,by in lines:

            manDist = abs(sx-bx)+abs(sy-by)
            rowY = manDist - abs(sy-Y)

            if rowY < 0:
                continue
            
            lx = sx-rowY
            ly = sx+rowY
            intervals.append( [lx,ly] )

            intervals.sort()
            q = []
            for l,r in intervals:
                if not q:
                    q.append( [l,r] )
                    continue
                qr = q[-1][1]
                if l > qr+1:
                    q.append( [l,r] )
                    continue
                q[-1][1] = max(qr,r)
        
        x = 0
        for l,r in q:
            if x < l:
                return x*4_000_000+Y
            x = max(x,r+1)
            if x > M:
                break

def main():
    print("Hallo")
    print(dayFifteen(), "ist die Lösung von Teil 1")
    #print(dayFifteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()