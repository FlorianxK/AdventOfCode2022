from typing import *

def dayFour():
    res = 0
    #read
    with open("Day4/4_2.txt") as file:
        for line in file:
            l,r = line.strip().split(',')
            range1 = [int(x) for x in l.split('-')]
            range2 = [int(x) for x in r.split('-')]

            if range1[0] <= range2[0] and range1[1] >= range2[1]:
                res += 1
            elif range2[0] <= range1[0] and range2[1] >= range1[1]:
                res += 1
    return res

def dayFour2():
    res = 0
    #read
    with open("Day4/4_2.txt") as file:
        for line in file:
            l,r = line.strip().split(',')
            range1 = [int(x) for x in l.split('-')]
            range2 = [int(x) for x in r.split('-')]
            
            if range1[0] <= range2[0] and range1[1] >= range2[0]:
                res += 1
            elif range2[0] <= range1[0] and range2[1] >= range1[0]:
                res += 1
    return res

def main():
    print("Hallo")
    print(dayFour(), "ist die Lösung von Teil 1")
    print(dayFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()