from typing import *

def dayTwentyFive():
    # 125 25 5 1
    def calc(arr):
        res = 0
        base = 1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] not in "-=":
                res += int(arr[i])*base
            elif arr[i] == '-':
                res += -1*base
            elif arr[i] == '=':
                res += -2*base
            base *= 5
        return res
    
    def reverse(val):
        res = ""
        while val > 0:
            rem = val%5
            val = val//5
            if rem <= 2:
                res = str(rem)+res
            else:
                if rem == 3:
                    res = '='+res
                elif rem == 4:
                    res = '-'+res
                val += 1
        return res
    
    res = 0
    #read
    with open("Day25/25_2.txt") as file:
        for line in file:
            arr = list(line.strip())
            res += calc(arr)
    return reverse(res)

def main():
    print("Hallo")
    print(dayTwentyFive(), "ist die Lösung")
     
if __name__=="__main__":
    main()