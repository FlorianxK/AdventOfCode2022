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
    arr = []
    second = False
    pos = None
    n = 0
    i = 0
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

    # right bottom left top (0,1,2,3)
    cDir = 0
    for move in order:
        i,j = pos
        if type(move) == int:
            for _ in range(move):
                nextI = i
                nextJ = j
                nextDir = cDir

                if cDir == 0:  # right
                    nextJ = j+1
                    if nextJ > rowsMod[i][1]:
                        if 0<=i<50: # 3-4
                            nextDir = 2
                            nextI,nextJ = 149-i,99
                        elif 50<=i<100: # 4
                            nextDir = 3
                            nextI,nextJ = 49,i+50
                        elif 100<=i<150: # 4-3
                            nextDir = 2
                            nextI,nextJ = 149-i,149
                        elif 150<=i<200: # 3
                            nextDir = 3
                            nextI,nextJ = 149,i-100
                elif cDir == 2:  # left
                    nextJ = j-1
                    if nextJ < rowsMod[i][0]:
                        if 0<=i<50: # 1-2
                            nextDir = 0
                            nextI,nextJ = 149-i,0
                        elif 50<=i<100: # 2
                            nextDir = 1
                            nextI,nextJ = 100,i-50
                        elif 100<=i<150: #2-1
                            nextDir = 0
                            nextI,nextJ = 149-i,50
                        elif 150<=i<200: # 1-5
                            nextDir = 1
                            nextI,nextJ = 0,i-100
                elif cDir == 1:  # down
                    nextI = i+1
                    if nextI > colsMod[j][1]:
                        if 0<=j<50: # 5-3
                            nextDir = 1
                            nextI,nextJ = 0,j+100
                        elif 50<=j<100: # 3
                            nextDir = 2
                            nextI,nextJ = j+100,49
                        elif 100<=j<150: # 4
                            nextDir = 2
                            nextI,nextJ = j-50,99
                elif cDir == 3:  # up
                    nextI = i-1
                    if nextI < colsMod[j][0]:
                        if 0<=j<50: # 2
                            nextDir = 0
                            nextI,nextJ = j+50,50
                        elif 50<=j<100: # 1-5
                            nextDir = 0
                            nextI,nextJ = j+100,0
                        elif 100<=j<150: # 5-3
                            nextDir = 3
                            nextI,nextJ = 199,j-100

                # move if no wall
                if arr[nextI][nextJ] != '#':
                    i,j,cDir = nextI,nextJ,nextDir
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

def main():
    print("Hallo")
    print(dayTwentyTwo(), "ist die Lösung von Teil 1")
    print(dayTwentyTwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()