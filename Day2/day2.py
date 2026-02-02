from typing import *

def dayTwo():
    res = 0
    # 1 rock, 2 paper, 3 scissor
    m = {'A':1,'X':1,'B':2,'Y':2,'C':3,'Z':3}
    #read
    with open("Day2/2_2.txt") as file:
        for line in file:
            enemy,select = line.strip().split(' ')
            if m[enemy] == m[select]:
                res += 3
            elif m[enemy] == 1 and m[select] == 2:
                res += 6
            elif m[enemy] == 2 and m[select] == 3:
                res += 6
            elif m[enemy] == 3 and m[select] == 1:
                res += 6
            res += m[select]
    return res

def dayTwo2():
    res = 0
    # 1 rock, 2 paper, 3 scissor
    m = {'A':1,'B':2,'C':3}
    #read
    with open("Day2/2_2.txt") as file:
        for line in file:
            enemy,select = line.strip().split(' ')
            if select == 'Y':
                res += 3
                res += m[enemy]
            elif select == 'X':
                if  m[enemy] == 1:
                    res += 3
                elif m[enemy] == 2:
                    res += 1
                elif m[enemy] == 3:
                    res += 2
            elif select == 'Z':
                res += 6
                if m[enemy] == 1:
                    res += 2
                elif m[enemy] == 2:
                    res += 3
                elif m[enemy] == 3:
                    res += 1
    return res

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()