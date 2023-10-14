import json

input = open("input.txt","r").read().split("\n\n")
pairs = [[json.loads(part) for part in pair.split("\n") if part] for pair in input]

def getPairNature(left,right):
    if isinstance(left,list) and isinstance(right,list) :
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

res =0 

for i,pair in enumerate(pairs) :
    l,r = pair
    if getPairNature(l,r) != -1:
        res+=(i+1)

print(res)


