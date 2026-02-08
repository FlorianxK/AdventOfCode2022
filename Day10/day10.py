from typing import *

def dayTen():
    x = 1
    arr = [0]
    #read
    with open("Day10/10_2.txt") as file:
        for line in file:
            line = line.strip()
            if line == "noop":
                arr.append(x)
            else:
                v = int(line.split()[1])
                arr.append(x)
                arr.append(x)
                x += v
    arr.append(x)
    
    n = len(arr)
    res = 0
    for i in range(20,n,40):
        res += i*arr[i]
    return res

def dayTen2():
    x = 1
    arr = []
    #read
    with open("Day10/10_2.txt") as file:
        for line in file:
            line = line.strip()
            if line == "noop":
                arr.append(x)
            else:
                v = int(line.split()[1])
                arr.append(x)
                arr.append(x)
                x += v
    
    n = len(arr)
    for i in range(0,n,40):
        for j in range(40):
            if abs(arr[i+j]-j) <= 1:
                print("##",end="")
            else:
                print("  ",end="")
        print()
    return "PZGPKPEB"

def main():
    print("Hallo")
    print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()