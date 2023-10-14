#A : rock, B : paper, C : scessor
#X : rock, Y : paper , Z : scessor
#rock : 1, paper : 2, scissors : 3
# win : 6, draw : 3, lost : 0

# def roundScore(row):
#     return roundPoints[row] if row in roundPoints else 0 
#     
# def shooseScore(secondCol):
#     return shoosePoints[secondCol]
#
# roundPoints= {
#     "AX":3,
#     "BY":3,
#     "CZ":3,
#     "AY":6,
#     "BZ":6,
#     "CX":6,
# }
# shoosePoints = {
#     "X":1,
#     "Y":2,
#     "Z":3,
# }
#
# input = open("input.txt","r").read().split("\n")
# res = 0
#
# for row in input :
#     if row == "" : continue
#     row = row.replace(" ","")
#     res+=roundScore(row) + shooseScore(row[-1]) 
#
# print(res)
######################################################################

#A : rock, B : paper, C : scessor
#X : rock, Y : paper , Z : scessor
#rock : 1, paper : 2, scissors : 3
# win : 6, draw : 3, lost : 0
#X : lost, Y : draw, Z : win


def roundScore(row):
    return roundPoints[row] if row in roundPoints else 0 
    
def shooseScore(secondCol):
    return shoosePoints[secondCol]

roundPoints= {
    "AX":3,
    "BY":3,
    "CZ":3,
    "AY":6,
    "BZ":6,
    "CX":6,
}
shoosePoints = {
    "X":1,
    "Y":2,
    "Z":3,
}
secondColMean = {
    "X":"lost",
    "Y":"draw",
    "Z":"win",
}
newState = {
    "lost":{
        "A":"AZ",
        "B":"BX",
        "C":"CY",
    },
    "draw":{
        "A":"AX",
        "B":"BY",
        "C":"CZ",
    },
    "win":{
        "A":"AY",
        "B":"BZ",
        "C":"CX",
    }
}

input = open("input.txt","r").read().split("\n")
res = 0

for row in input:
    if row == "":continue
    row = row.replace(" ","")
    newRow = newState[secondColMean[row[-1]]][row[0]]
    res+=roundScore(newRow)+shooseScore(newRow[-1])
print(res)




