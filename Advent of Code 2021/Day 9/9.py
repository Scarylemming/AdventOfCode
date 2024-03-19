import copy

f = open("9.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

#data = ["2199943210","3987894921","9856789892","8767896789","9899965678"]

n = len(data)
m = len(data[0])

empty = copy.deepcopy(data)


def is_min(x,y,grid,n,m) : 
    if x > 0 : 
        if int(grid[x][y]) >= int(grid[x-1][y]) : 
            return False 
    if x < n-1 : 
        if int(grid[x][y]) >= int(grid[x+1][y]) : 
            return False
    if y > 0 : 
        if int(grid[x][y]) >= int(grid[x][y-1]) : 
            return False
    if y < m-1 : 
        if int(grid[x][y]) >= int(grid[x][y+1]) : 
            return False
    
    return True

somme = 0

for x in range(n) : 
    for y in range(m) : 
        if is_min(x,y,data,n,m) : 
            #print(int(data[x][y]) + 1)
            somme += int(data[x][y]) + 1
            empty[x] = empty[x][0:y] + "X" + empty[x][y+1:]
            
print(somme)
            
            


