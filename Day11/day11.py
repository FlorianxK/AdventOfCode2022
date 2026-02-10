from typing import *

def dayEleven():
    monkeys = []
    rounds = 20
    #read
    with open("Day11/11_2.txt") as file:
        for group in file.read().strip().split("\n\n"):
            lines = group.splitlines()
            monkey = []
            monkey.append( [int(x) for x in lines[1].split(": ")[1].split(", ")] )
            monkey.append( eval("lambda old:" + lines[2].split("=")[1]) )
            for line in lines[3:]:
                monkey.append( int( line.split()[-1] ) )
            monkeys.append(monkey)
    n = len(monkeys)

    counts = [0]*n
    for _ in range(rounds):
        for index,monkey in enumerate(monkeys):
            for arr in monkey[0]:
                item = monkey[1](arr)
                item = item//3
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[index] += len(monkey[0])
            monkey[0] = []

    counts.sort()
    return counts[-2]*counts[-1]

def dayEleven2():
    monkeys = []
    rounds = 10000
    #read
    with open("Day11/11_2.txt") as file:
        for group in file.read().strip().split("\n\n"):
            lines = group.splitlines()
            monkey = []
            monkey.append( [int(x) for x in lines[1].split(": ")[1].split(", ")] )
            monkey.append( eval("lambda old:" + lines[2].split("=")[1]) )
            for line in lines[3:]:
                monkey.append( int( line.split()[-1] ) )
            monkeys.append(monkey)
    n = len(monkeys)
    counts = [0]*n

    mod = 1
    for monkey in monkeys:
        mod *= monkey[2]

    for _ in range(rounds):
        for index,monkey in enumerate(monkeys):
            for arr in monkey[0]:
                item = monkey[1](arr)
                item = item%mod
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[index] += len(monkey[0])
            monkey[0] = []

    counts.sort()
    return counts[-2]*counts[-1]

def main():
    print("Hallo")
    print(dayEleven(), "ist die Lösung von Teil 1")
    print(dayEleven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()