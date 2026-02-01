from heapq import heappush,heappop
from typing import *

def dayOne():
    h = []
    amount = 0
    #read
    with open("Day1/1_2.txt") as file:
        for line in file:
            if line == '\n':
                heappush(h,-amount)
                amount = 0
            else:
                amount += int(line.strip())
    heappush(h,-amount)
    return (-1)*heappop(h)

def dayOne2():
    h = []
    amount = 0
    #read
    with open("Day1/1_2.txt") as file:
        for line in file:
            if line == '\n':
                heappush(h,-amount)
                amount = 0
            else:
                amount += int(line.strip())
    heappush(h,-amount)

    res = 0
    for _ in range(3):
        res += (-1)*heappop(h)
    return res

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()