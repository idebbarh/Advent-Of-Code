import math

moves = open("input.txt","r").read().split("\n")
places = set() 
knotsPos=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

directions = {
    "U":[0,1],
    "D":[0,-1],
    "R":[1,1],
    "L":[1,-1],
}

def manhattanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def closestPoint(point, point_set):
    closestPoint = min(point_set, key=lambda p: manhattanDistance(point, p))
    return closestPoint

def arePointsAdjacent(point1, point2):
    return manhattanDistance(point1, point2) <= math.sqrt(2)

def moveMeBabby(d,one,two):
    global knotsPos

    if one == 0: 
        knotsPos[one][directions[d][0]]+=directions[d][1]

    if not arePointsAdjacent(knotsPos[one],knotsPos[two]) :
        clone = knotsPos[two].copy()
        setOfPoints = set()

        for y,x in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)] :
            setOfPoints.add(tuple([clone[0]+y,clone[1]+x]))

        knotsPos[two] = list(closestPoint(knotsPos[one],setOfPoints))    




def main() :
    for move in moves :
        if move == "": continue

        d,s = move.split(" ")

        for _ in range(int(s)) :
            for i in range(len(knotsPos)-1) :

                moveMeBabby(d,i,i+1)
                places.add((knotsPos[-1][0],knotsPos[-1][1]))

    print(len(places))
main()

