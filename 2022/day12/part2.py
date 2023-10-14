import math

grid = open("input.txt").read().split("\n")
grid = [[c for c in row] for row in grid if row != ""]

class Node:
    def __init__(self, value, gCost, hCost, fCost, parent,x,y):
        self.id = (x,y)
        self.value = value
        self.gCost = gCost
        self.hCost = hCost
        self.fCost = fCost
        self.parent = parent
        self.x = x
        self.y = y

    def getNeighbors(self):
        neighbors = []
        if self.x > 0:
            neighbors.append(Node(grid[self.x - 1][self.y], float("inf"), float("inf"), float("inf"), None, self.x - 1, self.y))
        if self.x < len(grid) - 1:
            neighbors.append(Node(grid[self.x + 1][self.y], float("inf"), float("inf"), float("inf"), None, self.x + 1, self.y))
        if self.y > 0:
            neighbors.append(Node(grid[self.x][self.y - 1], float("inf"), float("inf"), float("inf"), None, self.x, self.y - 1))
        if self.y < len(grid[0]) - 1:
            neighbors.append(Node(grid[self.x][self.y + 1], float("inf"), float("inf"), float("inf"), None, self.x, self.y + 1))

        return neighbors

    def getValidNeighbors(self):
        neighbors = self.getNeighbors()
        validNeighbors = []
        for neighbor in neighbors:
            if self.value >= neighbor.value or getNextLetter(self.value) == neighbor.value:
                validNeighbors.append(neighbor)

        return validNeighbors

startPoints = []
endPoint = Node("z",float("inf"),float("inf"),float("inf"),None,0,0) 
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S" or grid[i][j] == "a" :
            grid[i][j] = "a"
            startPoints.append(Node("a",0,float("inf"),float("inf"),None,i,j))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "E":
            grid[i][j] = "z"
            endPoint.x = i
            endPoint.y = j
            endPoint.id=(i,j)
            break

def getFcost(gCost, hCost):
    return gCost + hCost

def manhattanDistance(point1, point2):
    
    return math.sqrt(abs(point1.x - point2.x)**2 + abs(point1.y - point2.y)**2)


def getLowestCostNode(openList):
    lowestCostNode = openList[0]
    for node in openList:
        if node.fCost < lowestCostNode.fCost:
            lowestCostNode = node
    return lowestCostNode


def getNextLetter(letter):
    return chr(ord(letter) + 1)


res = []
def calcSteps(endPoint):
    current = endPoint.parent
    steps = 0
    while current :
        steps += 1
        current = current.parent

    res.append(steps)

def aStar(startPoint):
    openList = []
    closedSet = set()
    openSet = set()
    openList.append(startPoint)
    openSet.add(startPoint.id)
    while len(openList) > 0:
        current = getLowestCostNode(openList)
        if current.id == endPoint.id:
            calcSteps(current)
            break
        openList = list(filter(lambda p : p.id != current.id,openList))
        openSet.remove(current.id)

        closedSet.add(current.id)
        
        for point in current.getValidNeighbors():
            if point.id in closedSet : 
                continue

            newCost = current.gCost + manhattanDistance(current,point)

            if newCost < point.gCost :
                point.parent = current
                point.gCost = newCost
                point.hCost = manhattanDistance(point,endPoint)
                point.fCost = getFcost(point.gCost,point.hCost)

                if point not in openSet :
                    openList.append(point)
                    openSet.add(point.id)

for s in startPoints:
    aStar(s)

print(min(res))
