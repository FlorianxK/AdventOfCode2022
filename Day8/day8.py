from typing import *

def dayEight():
    arr = []
    #read
    with open("Day8/8_2.txt") as file:
        for line in file:
            arr.append( [int(x) for x in line.strip()] )
    
    m,n = len(arr),len(arr[0])
    visible = set()

    #left to right
    for i in range(n):
        maxV = -1
        for j in range(m):
            if arr[i][j] > maxV and (i,j) not in visible:
                visible.add( (i,j) )
            maxV = max(maxV,arr[i][j])

    #right to left
    for i in range(n):
        maxV = -1
        for j in range(m-1,-1,-1):
            if arr[i][j] > maxV and (i,j) not in visible:
                visible.add( (i,j) )
            maxV = max(maxV,arr[i][j])

    #top to bottom
    for j in range(n):
        maxV = -1
        for i in range(m):
            if arr[i][j] > maxV and (i,j) not in visible:
                visible.add( (i,j) )
            maxV = max(maxV,arr[i][j])

    #bottom to top
    for j in range(n):
        maxV = -1
        for i in range(m-1,-1,-1):
            if arr[i][j] > maxV and (i,j) not in visible:
                visible.add( (i,j) )
            maxV = max(maxV,arr[i][j])
    
    return len(visible)

def dayEight2():
    arr = []
    maxV = 0
    #read
    with open("Day8/8_2.txt") as file:
        for line in file:
            arr.append( [int(x) for x in line.strip()] )
    
    m,n = len(arr),len(arr[0])
    scenic = [[1]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i != 0 and i != m-1 and j != 0 and j != n-1:
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    seeInDir = 0
                    nx,ny = i+dx,j+dy
                    while True:
                        if 0<=nx<m and 0<=ny<n:
                            seeInDir += 1
                            if arr[nx][ny] < arr[i][j]:
                                nx += dx
                                ny += dy
                            else:
                                break
                        else:
                            break
                    if seeInDir > 0:
                        scenic[i][j] *= seeInDir
                        maxV = max(maxV,scenic[i][j])
    return maxV

def main():
    print("Hallo")
    print(dayEight(), "ist die Lösung von Teil 1")
    print(dayEight2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()