# input = [[[int(n) for n in interval.split("-") if n != ""] for interval in row.split(",")] for row in open("input.txt").read().split("\n")][::-1][1:][::-1]
# res = 0
# for pair in input :
#     [s,e],[s2,e2] = pair
#     if (s <= s2 and e >= e2) or (s2<=s and e2>=e):
#         res+=1
# print(res)
#########################################################################################
input = [[[int(n) for n in interval.split("-") if n != ""] for interval in row.split(",")] for row in open("input.txt").read().split("\n")][::-1][1:][::-1]
res = 0
def helper(s,e,s2,e2):
    return (s2 <= e and s2>=s) or (e2 <= e and e2 >= s)
for pair in input :
    [s,e],[s2,e2] = pair
    if helper(s,e,s2,e2) or helper(s2,e2,s,e):
        res+=1
print(res)

            
