input = open("input.txt","r").read()
grid = [[int(c) for c in row] for row in input.split("\n") if row]
visible = set()
edges = set() 

for i in range(len(grid[0])) :
    visible.add((0,i))
    visible.add((len(grid)-1,i))
    edges.add((0,i))
    edges.add((len(grid)-1,i))

for i in range(len(grid)):
    visible.add((i,0))
    visible.add((i,len(grid[0])-1))
    edges.add((i,0))
    edges.add((i,len(grid[0])-1))


def dfs(origin,row,col,direction) :
    if origin in visible : 
        return 
    if (row,col) in edges :
        visible.add(origin)    
        return 
    
    if direction == "down" :
        newR = row+1
        if newR < len(grid) and grid[origin[0]][origin[1]] > grid[newR][col]:
            dfs(origin,newR,col,direction)

    if direction == "up":
        newR = row-1
        if newR >= 0 and grid[origin[0]][origin[1]] > grid[newR][col]:
            dfs(origin,newR,col,direction)

    if direction == "left":
        newC = col+1
        if newC < len(grid[0]) and grid[origin[0]][origin[1]] > grid[row][newC]:
            dfs(origin,row,newC,direction)
            
    if direction == "right" :
        newC = col-1
        if newC >= 0 and grid[origin[0]][origin[1]] > grid[row][newC]:
            dfs(origin,row,newC,direction)

for i in range(len(grid)) :
    for j in range(len(grid[i])) :
        row = i
        col = j
        for d in ["down","up","left","right"] :
            if (row,col) not in visible :
                dfs((row,col),row,col,d)


print(len(visible))
        
    
    
