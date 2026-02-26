from typing import *

def dayTwentyTwo():
    arr = []
    second = False
    pos = None
    n = 0
    i = 0
    # right bottom left top
    dirs = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    #read
    with open("Day22/22_2.txt") as file:
        for line in file:
            if line == '\n':
                second = True
                continue
            if second:
                seq = line
            else:
                line = line[:-1]
                n = max(n,len(line))
                if pos == None:
                    for j in range(len(line)):
                        if line[j] == '.':
                            pos = (i,j)
                            break
                arr.append(line)
                i += 1
    
    m = len(arr)
    for i in range(m):
        if len(arr[i]) < n:
            arr[i] += ' '*(n-len(arr[i]))

    #start,end
    rowsMod = []
    colsMod = []
    for i in range(m):
        start = None
        for j in range(n):
            if start == None and arr[i][j] in ".#":
                start = j
            elif start != None and arr[i][j] == ' ':
                break
        if j < n-1:
            j -= 1
        rowsMod.append( (start,j) )

    for j in range(n):
        start = None
        for i in range(m):
            if start == None and arr[i][j] in ".#":
                start = i
            elif start != None and arr[i][j] == ' ':
                break
        if i < m-1:
            i -= 1
        colsMod.append( (start,i) )

    order = []
    num = ""
    for c in seq:
        if c in "LR":
            order.append(int(num))
            num = ""
            order.append(c)
        else:
            num += c
    order.append(int(num))

    cDir = 0
    for move in order:
        i,j = pos
        if type(move) == int:
            di,dj = dirs[cDir]
            # right left
            if cDir == 0 or cDir == 2:
                for _ in range(move):
                    nextJ = j + dj
                    if nextJ > rowsMod[i][1]:
                        nextJ = rowsMod[i][0]
                    elif nextJ < rowsMod[i][0]:
                        nextJ = rowsMod[i][1]
                    # IF no rock
                    if arr[i][nextJ] != '#':
                        j = nextJ
                    else:
                        break
            # bottom top
            elif cDir == 1 or cDir == 3:
                for _ in range(move):
                    nextI = i + di
                    if nextI > colsMod[j][1]:
                        nextI = colsMod[j][0]
                    elif nextI < colsMod[j][0]:
                        nextI = colsMod[j][1]
                    # IF no rock
                    if arr[nextI][j] != '#':
                        i = nextI
                    else:
                        break
        else:
            #L or R
            if move == 'R':
                cDir = (cDir+1)%4
            elif move == 'L':
                cDir = (cDir-1)%4
        
        pos = (i,j)
    
    return 1000*(pos[0]+1)+4*(pos[1]+1)+cDir

def dayTwentyTwo2():
    pass

def main():
    print("Hallo")
    print(dayTwentyTwo(), "ist die Lösung von Teil 1")
    print(dayTwentyTwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()