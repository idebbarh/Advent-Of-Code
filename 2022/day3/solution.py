# matches = {
#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4,
#     "e":5,
#     "f":6,
#     "g":7,
#     "h":8,
#     "i":9,
#     "j":10,
#     "k":11,
#     "l":12,
#     "m":13,
#     "n":14,
#     "o":15,
#     "p":16,
#     "q":17,
#     "r":18,
#     "s":19,
#     "t":20,
#     "u":21,
#     "v":22,
#     "w":23,
#     "x":24,
#     "y":25,
#     "z":26,
#     "total":26 
# }
# input = open("input.txt","r").read().split("\n")
# res = 0
# for row in input :
#     if row == "" : continue
#     hashSet = set()
#     checked = set()
#     left=row[0:len(row)//2] 
#     right=row[len(row)//2:] 
#     for c in left :
#         hashSet.add(c)
#
#     for c in right :
#         if c in hashSet and c not in checked:
#             res+=(matches[c] if c in matches else matches[c.lower()] + matches["total"])
#             checked.add(c)
#     
#     
# print(res) 

############################################################################################################
matches = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
    "total":26 
}
input = open("input.txt","r").read().split("\n")
res = 0
group = []
for row in input :
    if row == "" : continue
    group.append(row)
    if len(group) == 3:
        hashMap = {}
        for i,r in enumerate(group):
            for c in r :
                if c not in hashMap :
                    hashMap[c] = {0:0,1:0,2:0}
                hashMap[c][i]+=1
        for k,v in hashMap.items():
            if v[0] > 0 and v[1] > 0 and v[2] > 0 :
                res+=(matches[k] if k in matches else matches[k.lower()] + matches["total"])
                break
        group = []
print(res)


        






















