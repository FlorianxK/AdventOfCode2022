from typing import *

def dayThirteen():
    #read
    with open("Day13/13_2.txt") as file:
        arr = [x.splitlines() for x in file.read().strip().split("\n\n")]

    def f(x,y):
        if type(x) == int:
            if type(y) == int:
                return x-y
            else:
                return f( [x],y )
        else:
            if type(y) == int:
                return f( x,[y] )
    
        for a,b in zip(x,y):
            v = f(a,b)
            if v:
                return v
            
        return len(x)-len(y)

    res = 0
    index = 1
    for l,r in arr:
        if f( eval(l),eval(r) ) < 0:
            res += index
        index += 1
    return res

def dayThirteen2():
    #read
    with open("Day13/13_2.txt") as file:
        arr = [eval(x) for x in file.read().split()]

    def f(x,y):
        if type(x) == int:
            if type(y) == int:
                return x-y
            else:
                return f( [x],y )
        else:
            if type(y) == int:
                return f( x,[y] )
    
        for a,b in zip(x,y):
            v = f(a,b)
            if v:
                return v
            
        return len(x)-len(y)

    i2 = 1
    i6 = 2
    for a in arr:
        if f( a,[[2]] ) < 0:
            i2 += 1
            i6 += 1
        elif f( a,[[6]] ) < 0:
            i6 += 1

    return i2*i6

def main():
    print("Hallo")
    #print(dayThirteen(), "ist die Lösung von Teil 1")
    print(dayThirteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()