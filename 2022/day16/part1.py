data = [line for line in open("./testInput.txt","r").read().split("\n") if line]

graph = {}

for line in data :
    left,right = line.split("; ")
    valve = left.split(" ")[1]
    flowRate = int(left.split(" ")[-1][-1])
    leads = right.replace(",","").split(" ")[4:]
    graph[valve] = {
        "flowRate":flowRate,
        "leads":leads
    }

openValves = set()
res = 0

def getValue(time):
    value = 0
    for n in openValves :
        if n in graph : 
            value+=(graph[n]["flowRate"]*time)

    return value



def backtrack(current,value,time,vis,first=False):
    global res

    if time == 0 :
        res = max(res,value)
        return 

    m = 0
    for v in graph[current]["leads"] :
        if graph[current]["flowRate"] :
            m+=1
            openValves.add(v)

        m+=1
        backtrack(v,getValue(m),time-m)

        if current in openValves : 
            time+=1
            m-=1
            openValves.remove(v)

        backtrack(v,getValue(time-m)*m,time-m)

    
    
print(backtrack("AA",0,30,True))


    
