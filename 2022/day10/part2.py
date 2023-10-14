input = open("input.txt","r").read().split("\n")

xVal = 1 
curCycle = 0
crt = [[" " for j in range(40)] for i in range(6)]

def getDrawingRow():
    return curCycle // 40

def getDrawingCol():
    col = curCycle
    while col > 39 :
        col-=40

    return col 

def drawInCrt():
    row = getDrawingRow()
    col = getDrawingCol()

    if col in [xVal-1,xVal,xVal+1] :
        crt[row][col] = "#"
    
for step in input :
    if step == "" : continue

    if step == "noop" : 
        drawInCrt()
        curCycle +=1
    else :
        _,n = step.split(" ") 
        drawInCrt()
        curCycle+=1
        drawInCrt()
        curCycle+=1
        xVal+=int(n)

for row in crt :
    print("".join(row))
