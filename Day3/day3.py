from typing import *

def dayThree():
    res = 0
    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            line = line.strip()
            l,r = set(line[:len(line)//2]),set(line[len(line)//2:])

            c:str
            for c in l:
                if c in r:
                    if c.islower():
                        res += ord(c)-96
                    else:
                        res += ord(c)-38
    return res

def dayThree2():
    res = 0
    triple = []
    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            triple.append( set(line.strip()) )

            if len(triple) == 3:
                c:str
                for c in triple[0]:
                    if c in triple[1] and c in triple[2]:
                        if c.islower():
                            res += ord(c)-96
                        else:
                            res += ord(c)-38
                triple = []
    return res

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()