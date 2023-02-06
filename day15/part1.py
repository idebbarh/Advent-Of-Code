import math
input = open("testInput.txt","r").read().split("\n")
sensorsPos = []
beaconPos = []
minX = float("inf")
maxX = float("-inf")
minY = float("inf")
maxY = float("-inf")
searchRow = 10

class Point :
    def __init__(self,position,distance) :
        self.position = position 
        self.distance = distance

    def getNeighbors(self):
        y,x = self.position
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        neighbors = [] 
        for y2,x2 in directions :
            neiPos = (y+y2,x+x2)
            ny,nx = neiPos
            if minY <= ny <= maxY and minX <= nx <= maxX :
                neighbors.append(Point(neiPos,float("inf")))

        return neighbors


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

    maxX,maxY,minX,minY = max(x,maxX),max(y,maxY),min(x,minX),min(y,minY)
    sensorsPos.append(Point((y,x),float("inf")))

    for i,c in enumerate(right) : 
        if c == "=" :
            if right[i-1] == "x" :
                n = ""
                for c2 in right[i+1:] :
                    if c2 == "," : break
                    n+=c2

                x = int(n)
            else :
                n=""
                for c2 in right[i+1:]:
                    n+=c2

                y = int(n)

    maxX,maxY,minX,minY = max(x,maxX),max(y,maxY),min(x,minX),min(y,minY)
    beaconPos.append((y,x))


def manhattanDis(p1,p2) :
    x1,y1=p1.position
    x2,y2=p2.position

    return math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)

def pointWithMinCost(points) :
    minCost = float("inf")
    point = None
    for p in points :
        if p.distance < minCost :
            minCost = p.distance
            point = p

    return p

def dijkstra(start):
    openList = []
    openSet = set()
    closeSet = set()
    start.distance = 0
    openList.append(start)
    openSet.add(start.position)
    while openList :
        current = pointWithMinCost(openList)
        if current.position in beaconPos :
            closeSet.add(current.position)
            return closeSet

        openList = list(filter(lambda p : p.position != current.position,openList))
        openSet.remove(current.position)
        closeSet.add(current.position) 

        for n in current.getNeighbors():
            if n.position in closeSet : continue
            newDis = current.distance + manhattanDis(current,n)
            if newDis < n.distance :
                n.distance = newDis
                if n.position not in openSet :
                    openSet.add(n.position)
                    openList.append(n)

    return -1



rowsRange = {}

for p in sensorsPos :
    if p.position != (7,8) : continue
    res = dijkstra(p)
    print(res)
    if res != -1 :
        for p2 in res :
            y,x = p2
            if y not in rowsRange :
                rowsRange[y] = [float("inf"),float("-inf")]
            rowsRange[y][0] = min(rowsRange[y][0],x)
            rowsRange[y][1] = max(rowsRange[y][1],x)


            



res = abs(rowsRange[searchRow][1]-rowsRange[searchRow][0])


print(res)
print((rowsRange[9][0],rowsRange[9][1]))
# print(rowsRange)
