from typing import *

def dayTwentyFour():
    arr = []
    tornados = set()
    torn = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}
    i = 0
    #read
    with open("Day24/24.txt") as file:
        for line in file:
            arr.append( list(line.strip()) )
            for j in range(len(line)):
                if line[j] in "<>^v":
                    tornados.add( (i,j,arr[i][j]) )
            i += 1

    m,n = len(arr),len(arr[0])
    start = (0,1)
    end = (m-1,n-2)
    arr[start[0]][start[1]] = 'S'
    arr[end[0]][end[1]] = 'E'

    def moveTornado():
        newTorn = set()
        for i,j,comp in tornados:
            di,dj = torn[comp]
            ni,nj = i+di,j+dj
            if arr[ni][nj] == '#':
                if comp == '<':
                    nj = n-2
                elif comp == '>':
                    nj = 1
                elif comp == '^':
                    ni = m-2
                elif comp == 'v':
                    ni = 1
            newTorn.add( (ni,nj,comp) )
        return newTorn

    def movePlayer(i,j):
        pass

    minute = 0
    pos = start
    while True:
        minute += 1

        for i,j,_ in tornados:
            arr[i][j] = '.'

        tornados = moveTornado()
        movePlayer(0,0)

        for i,j,comp in tornados:
            arr[i][j] = comp

        for a in arr:
            print(''.join(a))
        print()
        if pos == end or minute == 5:
            break
    return minute

def dayTwentyFour2():
    pass

def main():
    print("Hallo")
    print(dayTwentyFour(), "ist die Lösung von Teil 1")
    #print(dayTwentyFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()