import copy

f = open("9.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

#data = ["2199943210","3987894921","9856789892","8767896789","9899965678"]

n = len(data)
m = len(data[0])

empty = [[0 for i in range(m)] for j in range(n)]


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

def add_basin(x,y,grid,empty,n,m) : 
    
    
    pass

def find_basins(x,y,grid,empty,n,m,count) : 
    
    if x > 0 : 
        if int(grid[x-1][y]) > int(grid[x][y]) : 
            if int(grid[x-1][y]) != 9 : 
                if empty[x-1][y] == 0 : 
                    count += 1
                    empty[x-1][y] = "X"
                empty,count = find_basins(x-1,y,grid,empty,n,m,count)
    if x < n-1 : 
        if int(grid[x+1][y]) > int(grid[x][y]) : 
            if int(grid[x+1][y]) != 9 : 
                if empty[x+1][y] == 0 : 
                    count += 1
                    empty[x+1][y] = "X"
                empty,count = find_basins(x+1,y,grid,empty,n,m,count) 
    if y > 0 : 
        if int(grid[x][y-1]) > int(grid[x][y]) : 
            if int(grid[x][y-1]) != 9 : 
                if empty[x][y-1] == 0 : 
                    count += 1
                    empty[x][y-1] = "X"
                empty,count = find_basins(x,y-1,grid,empty,n,m,count) 
    if y < m-1: 
        if int(grid[x][y+1]) > int(grid[x][y]) : 
            if int(grid[x][y+1]) != 9 : 
                if empty[x][y+1] == 0 : 
                    count += 1
                    empty[x][y+1] = "X"
                empty,count = find_basins(x,y+1,grid,empty,n,m,count) 
    
    return empty,count
    

somme = 0

tout_comptes = []

for x in range(n) : 
    for y in range(m) : 
        if is_min(x,y,data,n,m) : 
            #print(int(data[x][y]) + 1)
            somme += int(data[x][y]) + 1
            empty[x][y] = "X"
            empty,compte = find_basins(x, y, data, empty, n, m,1)
            tout_comptes.append(compte)
            
tout_comptes.sort()

print(tout_comptes)

print(tout_comptes[-1] * tout_comptes[-2] * tout_comptes[-3])
            


