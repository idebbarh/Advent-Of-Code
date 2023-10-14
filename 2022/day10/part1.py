input = open("testInput.txt","r").read().split("\n")
cyclesNeedToKnow = [20,60,100,140,180,220];
xVal = 1 
curCycle = 0
res = []

def checkIfThisIsTheMoment():
    if curCycle in cyclesNeedToKnow :
        res.append(curCycle*xVal)    

for step in input :
    if step == "" : continue

    if step == "noop" : 
        curCycle +=1
        checkIfThisIsTheMoment()
    else :
        _,n = step.split(" ") 
        curCycle+=1
        checkIfThisIsTheMoment()
        curCycle+=1
        checkIfThisIsTheMoment()
        xVal+=int(n)

print(sum(res))

        
