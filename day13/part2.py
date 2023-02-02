import json

input = open("input.txt","r").read().replace("\n\n","\n").split("\n")
packs = [*[json.loads(pack) for pack in input if pack],*[[[2]],[[6]]]]

def getPairNature(left,right):
    if isinstance(left,list) and isinstance(right,list):
        return checkTwoLists(left,right)

    if isinstance(left,int) and isinstance(right,int) :
        return checkTwoInts(left,right)

    if isinstance(left,int) and isinstance(right,list) :
        return checkOneInt(left,right,"l")

    if isinstance(left,list) and isinstance(right,int) :
        return checkOneInt(left,right,"r")


def checkTwoLists(left,right):
    l,r = 0,0
    while l < len(left) and r < len(right) :
        res = getPairNature(left[l], right[r]) 
        if res in [-1,1]:
            return res
        l+=1
        r+=1

    return 1 if l == len(left) and r < len(right) else (0 if len(left) == l and len(right) == r else -1)

def checkTwoInts(left,right):
    return 1 if left < right else (0 if left == right else -1) 

def checkOneInt(left,right,s):
    if s == "l":
        return checkTwoLists([left],right)

    return checkTwoLists(left,[right])


for i in range(len(packs)):
    for j in range(len(packs)-1-i):
        left = packs[j]
        right = packs[j+1]
        if getPairNature(left,right) == -1:
            packs[j],packs[j+1] = packs[j+1],packs[j]

res =1 
for i,pack in enumerate(packs) :
    if pack in [[[2]],[[6]]] :
        res*=(i+1)

print(res)


