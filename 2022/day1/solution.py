input = open("input.txt","r").read().split("\n")
def solution() : 
    res = [float("-inf"),float("-inf"),float("-inf")]
    curT = 0
    for n in input :
        if n == '' :
            if curT >= res[0] : 
                res[0],res[1],res[2] = curT,res[0],res[1] 
            elif curT >= res[1]:
                res[1],res[2]= curT,res[1]
            else :  
                res[2] = max(res[2],curT)
            curT = 0
            continue
        curT+=int(n)
     return sum(res)

print(solution())

