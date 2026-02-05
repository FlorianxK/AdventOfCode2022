from collections import deque
from typing import *

def daySix():
    index = 4
    #read
    with open("Day6/6_2.txt") as file:
        for line in file:
            arr = deque(line[:index])
            if len(set(arr)) == 4:
                return index

            for i in range(4,len(line)):
                index += 1
                arr.popleft()
                arr.append(line[i])
                if len(set(arr)) == 4:
                    return index

def daySix2():
    index = 14
    #read
    with open("Day6/6_2.txt") as file:
        for line in file:
            arr = deque(line[:index])
            if len(set(arr)) == 14:
                return index

            for i in range(14,len(line)):
                index += 1
                arr.popleft()
                arr.append(line[i])
                if len(set(arr)) == 14:
                    return index

def main():
    print("Hallo")
    print(daySix(), "ist die Lösung von Teil 1")
    print(daySix2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()