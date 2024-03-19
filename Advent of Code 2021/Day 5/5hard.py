f = open("5.txt", "r")


data = [line.split(" ")[0::2] for line in f.read().split("\n")][:-1]

for i,line in enumerate(data) : 
    a = line[0].split(",")
    b = line[1].split(",")
    data[i] = [[int(a[0]), int(a[1])],[int(b[0]), int(b[1])]]
    
board = [[0 for i in range(1000)] for j in range(1000)]

def sign(x) : 
    if x == 0 : 
        return 0
    elif abs(x) == x : 
        return 1
    else : 
        return -1

def write(a,b, board) : 
    if a[0] == b[0] : 
        for i in range(abs(a[1] - b[1]) + 1) : 
            board[a[0]][min(a[1],b[1]) + i] += 1
    elif a[1] == b[1] : 
        for i in range(abs(a[0] - b[0]) + 1) : 
            board[min(a[0],b[0]) + i][a[1]] += 1
    else : 
        for i in range(abs(a[0] - b[0]) + 1) : 
            board[a[0] + i*sign(b[0] - a[0])][a[1] + i*sign(b[1] - a[1])] += 1
            
    return board

for i in data : 
    board = write(i[0], i[1], board)

somme = 0 

for i in range(1000) : 
    for j in range(1000) : 
        if board[i][j] >= 2 : 
            somme += 1
            
print(somme)