from typing import *

class Node:
    def __init__(self,val:int):
        self.val = val
        self.prev:Node = None
        self.next:Node = None

def dayTwenty():
    linked = []
    #read
    with open("Day20/20_2.txt") as file:
        for line in file:
            linked.append( Node(int(line)) )
    n = len(linked)
    for i in range(n):
        linked[i].next = linked[ (i+1)%n ]
        linked[i].prev = linked[ (i-1)%n ]

    mod = n-1
    for node in linked:
        if node.val == 0:
            zero = node
            continue
        temp = node
        if node.val > 0:
            for _ in range( node.val%mod ):
                temp = temp.next
            
            if temp == node:
                continue
            #remove node
            node.next.prev = node.prev
            node.prev.next = node.next
            #insert node
            temp.next.prev = node
            node.next = temp.next
            temp.next = node
            node.prev = temp
        else:
            for _ in range( -node.val%mod ):
                temp = temp.prev
            
            if temp == node:
                continue
            #remove node
            node.prev.next = node.next
            node.next.prev = node.prev
            #insert node
            temp.prev.next = node
            node.prev = temp.prev
            temp.prev = node
            node.next = temp
 
    res = 0
    for _ in range(3):
        for _ in range(1000):
            zero = zero.next
        res += zero.val
    return res

def dayTwenty2():
    linked = []
    #read
    with open("Day20/20_2.txt") as file:
        for line in file:
            linked.append( Node(int(line)*811589153) )
    n = len(linked)
    for i in range(n):
        linked[i].next = linked[ (i+1)%n ]
        linked[i].prev = linked[ (i-1)%n ]

    mod = n-1
    for _ in range(10):
        for node in linked:
            if node.val == 0:
                zero = node
                continue
            temp = node
            if node.val > 0:
                for _ in range( node.val%mod ):
                    temp = temp.next
                
                if temp == node:
                    continue
                #remove node
                node.next.prev = node.prev
                node.prev.next = node.next
                #insert node
                temp.next.prev = node
                node.next = temp.next
                temp.next = node
                node.prev = temp
            else:
                for _ in range( -node.val%mod ):
                    temp = temp.prev
                
                if temp == node:
                    continue
                #remove node
                node.prev.next = node.next
                node.next.prev = node.prev
                #insert node
                temp.prev.next = node
                node.prev = temp.prev
                temp.prev = node
                node.next = temp
 
    res = 0
    for _ in range(3):
        for _ in range(1000):
            zero = zero.next
        res += zero.val
    return res

def main():
    print("Hallo")
    print(dayTwenty(), "ist die Lösung von Teil 1")
    print(dayTwenty2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()