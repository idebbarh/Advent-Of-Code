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

def isCanBeHere(p) :
    for sensor in sensorsPos :
        sensorCurrentPos = sensor 
        closestBeacon = min(beaconsPos,key=lambda p: manhattanDis(p,sensorCurrentPos))

        if manhattanDis(p,sensorCurrentPos) <= manhattanDis(closestBeacon,sensorCurrentPos) :
            return False

        if manhattanDis(p,sensorCurrentPos) <= manhattanDis(closestBeacon,sensorCurrentPos) :
            return False

    return True

maxRange = 4000000       

for y in range(maxRange+1) :
    for x in range(maxRange+1) :
        if 0 < y < maxRange and 0 < x < maxRange and isCanBeHere((y,x)):
            print((y,x))
        
