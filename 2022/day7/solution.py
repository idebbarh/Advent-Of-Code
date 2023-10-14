input = open("input.txt","r").read().split("\n");

maxSize = 100000
updateSize = 30000000
fileSystem = 70000000
unusedSize = 0
res = float("inf");
hashMap = {}
class Stack :
    def __init__(self):
        self.items = []

    def push(self,value) :
        self.items.append(value)

    def pop(self):
        if self.size() > 0 :
            return self.items.pop(-1)

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

stack = Stack()

for line in input :
    if line == "" : continue
    line = line.split(" ")
    if line[0] == "$":  
        if line[1] == "cd":
            if line[2] == ".." :
                poped = stack.pop()
                stack.items[-1][-1]+=poped[-1]
                hashMap[poped[0]] = poped[-1]
                continue
            elif line[2] == "/" :
                stack.clear() 
            stack.push([line[2],0])

    elif line[0] == "dir" :
        continue

    else :
        stack.items[-1][-1]+= int(line[0])

while stack.items :
    poped = stack.pop()
    if stack.items :
        stack.items[-1][-1]+=poped[-1]
    hashMap[poped[0]] = poped[-1]

unusedSize = fileSystem-hashMap["/"]
curD = float("inf")
for _,v in hashMap.items():
    if unusedSize+v >= updateSize:
        res = min(res,v)
        
print(res)



        
