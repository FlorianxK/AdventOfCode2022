import math
from typing import *

def dayNineteen():
    
    def dfs(bp,maxSpend,cache,time,bots,amount):
        if time == 0:
            return amount[3]

        key = tuple( [time,*bots,*amount] )
        if key in cache:
            return cache[key]
        
        maxVal = amount[3]+bots[3]*time

        for botType,recipe in enumerate(bp):
            if botType != 3 and bots[botType] >= maxSpend[botType]:
                continue

            wait = 0
            for rAmount,rType in recipe:
                if bots[rType] == 0:
                    break
                build = math.ceil( (rAmount-amount[rType])/bots[rType] )
                wait = max(wait,build)
            else:
                remTime = time-wait-1
                if remTime <= 0:
                    continue
                bots_ = bots[:]
                amount_ = [ x+y*(wait+1) for x,y in zip(amount,bots) ]
                for rAmount,rType in recipe:
                    amount_[rType] -= rAmount
                bots_[botType] += 1
                for i in range(3):
                    amount_[i] = min(amount_[i], maxSpend[i]*remTime)
                maxVal = max( maxVal,dfs(bp,maxSpend,cache,remTime,bots_,amount_) )
        cache[key] = maxVal
        return maxVal

    res = 0
    #read
    with open("Day19/19_2.txt") as file:
        for line in file:
            a = line.strip().split()
            maxSpend = [0,0,0]
            bpNum = int(a[1][:-1])
            bp = []
            bp.append( [( int(a[6]),0 )] )
            bp.append( [( int(a[12]),0 )] )
            bp.append( [( int(a[18]),0 ),( int(a[21]),1 )] )
            bp.append( [( int(a[27]),0 ),( int(a[30]),2 )] )
            
            maxSpend = [0,0,0]
            for vals in bp:
                for v in vals:
                    maxSpend[v[1]] = max(maxSpend[v[1]],v[0])

            v = dfs(bp,maxSpend,{},24,[1,0,0,0],[0,0,0,0])
            res += bpNum*v
    return res

def dayNineteen2():

    def dfs(bp,maxSpend,cache,time,bots,amount):
        if time == 0:
            return amount[3]

        key = tuple( [time,*bots,*amount] )
        if key in cache:
            return cache[key]
        
        maxVal = amount[3]+bots[3]*time

        for botType,recipe in enumerate(bp):
            if botType != 3 and bots[botType] >= maxSpend[botType]:
                continue

            wait = 0
            for rAmount,rType in recipe:
                if bots[rType] == 0:
                    break
                build = math.ceil( (rAmount-amount[rType])/bots[rType] )
                wait = max(wait,build)
            else:
                remTime = time-wait-1
                if remTime <= 0:
                    continue
                bots_ = bots[:]
                amount_ = [ x+y*(wait+1) for x,y in zip(amount,bots) ]
                for rAmount,rType in recipe:
                    amount_[rType] -= rAmount
                bots_[botType] += 1
                for i in range(3):
                    amount_[i] = min(amount_[i], maxSpend[i]*remTime)
                maxVal = max( maxVal,dfs(bp,maxSpend,cache,remTime,bots_,amount_) )
        cache[key] = maxVal
        return maxVal

    res = 1
    counter = 0
    #read
    with open("Day19/19_2.txt") as file:
        for line in file:
            a = line.strip().split()
            maxSpend = [0,0,0]
            bp = []
            bp.append( [( int(a[6]),0 )] )
            bp.append( [( int(a[12]),0 )] )
            bp.append( [( int(a[18]),0 ),( int(a[21]),1 )] )
            bp.append( [( int(a[27]),0 ),( int(a[30]),2 )] )
            
            maxSpend = [0,0,0]
            for vals in bp:
                for v in vals:
                    maxSpend[v[1]] = max(maxSpend[v[1]],v[0])

            v = dfs(bp,maxSpend,{},32,[1,0,0,0],[0,0,0,0])
            res *= v

            counter += 1
            if counter == 3:
                return res

def main():
    print("Hallo")
    print(dayNineteen(), "ist die Lösung von Teil 1")
    print(dayNineteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()