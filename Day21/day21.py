from collections import defaultdict, deque
from typing import *

import sympy

def dayTwentyOne():
    nums = defaultdict(int)
    #read
    with open("Day21/21_2.txt") as file:
        lines = deque([line.strip() for line in file])

    while lines:
        line = lines.popleft()
        l,r = line.strip().split(": ")
        if r.isnumeric():
            nums[l] = int(r)
        else:
            left,op,right = r.split()
            if left in nums and right in nums:
                nums[l] = eval( f"{nums[left]} {op} {nums[right]}")
            else:
                lines.append(line)
    return int(nums["root"])

def dayTwentyOne2():
    nums = defaultdict(int)
    nums["humn"] = sympy.Symbol("x")
    #read
    with open("Day21/21_2.txt") as file:
        lines = deque([line.strip() for line in file])

    operations = {'+': lambda x,y: x+y,
                  '-': lambda x,y: x-y,
                  '*': lambda x,y: x*y,
                  '/': lambda x,y: x/y}

    while lines:
        line = lines.popleft()
        l,r = line.strip().split(": ")
        if l in nums:
            continue

        if r.isnumeric():
            nums[l] = float(r)
        else:
            left,op,right = r.split()
            if left in nums and right in nums:
                if l == "root":
                    res = sympy.solve(nums[left]-nums[right])
                    break
                nums[l] = operations[op](nums[left],nums[right])
            else:
                lines.append(line)
    return int(res[0])

def main():
    print("Hallo")
    print(dayTwentyOne(), "ist die Lösung von Teil 1")
    print(dayTwentyOne2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()