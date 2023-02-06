import math

input = open("input.txt","r").read().split("\n")
sensorsPos = set() 
beaconsPos = set() 

for row in input :
    if not row : continue

    left,right=row.split(":")
    x,y=None,None

    for i,c in enumerate(left) : 
        if c == "=" :
            if left[i-1] == "x" :
                n = ""
                for c2 in left[i+1:] :
                    if c2 == "," : break
                    n+=c2

                x = int(n)
            else :
                n=""
                for c2 in left[i+1:] :
                    n+=c2

                y = int(n)

    sensorsPos.add((y,x))

    for i,c in enumerate(right) : 
        if c == "=" :
            if right[i-1] == "x" :
                n = ""
                for c2 in right[i+1:] :
                    if c2 == "," : break
                    n+=c2

                x = int(n)
            else:
                n=""
                for c2 in right[i+1:]:
                    n+=c2

                y = int(n)

    beaconsPos.add((y,x))


def manhattanDis(p1,p2) :
    x1,y1=p1
    x2,y2=p2

    return abs(x2-x1) + abs(y2-y1)


searchRow = 2000000
rowRange = [float('inf'),float('-inf')]

for sensor in sensorsPos :
    sensorCurrentPos = sensor 
    closestBeacon = min(beaconsPos,key=lambda p: manhattanDis(p,sensorCurrentPos))
    mostLeft = sensor[1] 
    mostRight = sensor[1] 

    while manhattanDis((searchRow,mostLeft),sensorCurrentPos) < manhattanDis(closestBeacon,sensorCurrentPos) :
        mostLeft-=1

    while manhattanDis((searchRow,mostRight),sensorCurrentPos) < manhattanDis(closestBeacon,sensorCurrentPos) :
        mostRight+=1

    rowRange[0] = min(rowRange[0],mostLeft)
    rowRange[1] = max(rowRange[1],mostRight)

rowRange[1]+=1
res = abs(rowRange[1]-rowRange[0])

for x in range(*rowRange) :
    if (searchRow,x) in beaconsPos :
        res-=1

print(res)
        
