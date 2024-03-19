import copy

f = open("11.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

grid = []

def print_grid(grid) : 
    for i in grid : 
        print(i)

for line in data : 
    n_line = []
    for j in line : 
        n_line.append(int(j))
    grid.append(n_line)


def add_level(n) : 
    return (n+1)

def flash(i,j,grid) : 
    n = len(grid)
    m = len(grid[0])
    if i > 0 : 
        grid[i-1][j] = add_level(grid[i-1][j])
        if j > 0 : 
            grid[i-1][j-1] = add_level(grid[i-1][j-1])
        if j < m-1 : 
            grid[i-1][j+1] = add_level(grid[i-1][j+1])
    if i < n-1 : 
        grid[i+1][j] = add_level(grid[i+1][j])
        if j > 0 : 
            grid[i+1][j-1] = add_level(grid[i+1][j-1])
        if j < m-1 : 
            grid[i+1][j+1] = add_level(grid[i+1][j+1])
    if j > 0 : 
        grid[i][j-1] = add_level(grid[i][j-1])
    if j < m-1 : 
        grid[i][j+1] = add_level(grid[i][j+1])
    return grid

def step(grid) : 
    n = len(grid)
    m = len(grid[0])
    
    n_grid = copy.deepcopy(grid)
    # print_grid(n_grid)
    # print("-----------------------------")
    
    for i in range(n) : 
        for j in range(m) : 
            n_grid[i][j] = add_level(grid[i][j])
    
    
    liste_flash = []
    old_liste_flash = []
    no_nine = False
    rounds = 1
    
    while no_nine == False : 
        # print(rounds)
        for i in range(n) : 
            for j in range(m) : 
                if n_grid[i][j] > 9 : 
                    if [i,j] not in liste_flash : 
                        liste_flash.append([i,j])
        # print(liste_flash)
        # print(old_liste_flash)
        for f in liste_flash : 
            if f not in old_liste_flash : 
                n_grid = flash(f[0], f[1],n_grid)
                # print_grid(n_grid)
                # print("-----------------------------")
        
        if old_liste_flash == liste_flash : 
            # print("Same")
            no_nine = True
            break
        
        old_liste_flash = copy.deepcopy(liste_flash)
        rounds += 1
    for f in liste_flash : 
        n_grid[f[0]][f[1]] = 0
    # print(liste_flash)
    # print(old_liste_flash)
    return n_grid, liste_flash

somme = 0
def test_all(grid) : 
    for i in range(len(grid)) : 
        for j in range(len(grid[0])) : 
            if grid[i][j] != 0 : 
                return False
    return True
i = 0
while True : 
    i += 1
    grid,l = step(grid)
    somme += len(l)
    if test_all(grid) : 
        print(i)
        break
print("-----------------------------")
print_grid(grid)
print(somme)

#J'ai l'impression que les pieuvres de flashent pas. Il faut vérifier ça

    


