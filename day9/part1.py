def checkIfCloseToEachOther(hp,tp):
    return [tp[0]+1,tp[1]] == hp or [tp[0] - 1,tp[1]] == hp or [tp[0],tp[1] + 1] == hp or [tp[0],tp[1] - 1] == hp or [tp[0]+1,tp[1]+1] == hp or [tp[0]+1,tp[1]-1] == hp or [tp[0]-1,tp[1]+1] == hp or [tp[0]-1,tp[1]-1] == hp

def isInTheSamePos(hp,tp):
    return hp == tp

def checkIfHeadAndTailInTheSameRowOrCol(hp,tp):
    return hp[0] == tp[0] or hp[1] == tp[1] 

moves = open("input.txt","r").read().split("\n")
places = set() 
headPos,tailPos=[0,0],[0,0]

directions = {
    "U":[0,1],
    "D":[0,-1],
    "R":[1,1],
    "L":[1,-1],
}

def moveMeBabby(d):
    global tailPos
    headPos[directions[d][0]]+=directions[d][1]
    if not checkIfCloseToEachOther(headPos,tailPos) and not isInTheSamePos(headPos,tailPos):
        if checkIfHeadAndTailInTheSameRowOrCol(headPos,tailPos):
            tailPos[directions[d][0]]+=directions[d][1]
        else :
            newTailPos = [tailPos[0]+1,tailPos[1]+1] 
            if not isInTheSamePos(headPos,newTailPos) and checkIfCloseToEachOther(headPos,newTailPos) :
                tailPos = newTailPos
                return

            newTailPos = [tailPos[0]+1,tailPos[1]-1]
            if not isInTheSamePos(headPos,newTailPos) and checkIfCloseToEachOther(headPos,newTailPos):
                tailPos = newTailPos
                return

            newTailPos = [tailPos[0]-1,tailPos[1]+1] 
            if not isInTheSamePos(headPos,newTailPos) and checkIfCloseToEachOther(headPos,newTailPos):
                tailPos = newTailPos
                return

            newTailPos = [tailPos[0]-1,tailPos[1]-1] 
            if not isInTheSamePos(headPos,newTailPos) and checkIfCloseToEachOther(headPos,newTailPos):
                tailPos = newTailPos
                return 

def main() :

    for move in moves :
        if move == "": continue
        d,s = move.split(" ")
        for _ in range(int(s)) :
            moveMeBabby(d)
            places.add((tailPos[0],tailPos[1]))

    print(len(places))

main()

