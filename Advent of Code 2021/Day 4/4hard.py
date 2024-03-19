import copy

f = open("4.txt", "r")


data = [line for line in f.read().split("\n")][:-1]

numbers = data[0].split(",")


def create_line(line):
    int_line = []
    integer = ""
    for i, j in enumerate(line):
        if i % 3 == 2:
            int_line += [int(integer)]
            integer = ""
        else:
            integer += j
    int_line += [int(integer)]
    return int_line

def verify(board) : 
    compte = 0
    for i in range(5) : 
        for j in range(5) : 
            if board[i][j] == 1 : 
                compte += 1
        #print(compte)
        if compte == 5: 
            return True
        compte = 0
    for i in range(5) :
        for j in range(5): 
            if board[j][i] == 1 : 
                compte += 1   
        if compte == 5: 
            return True
        compte = 0
    return False

def find(board) : 
    for i,b in enumerate(board) : 
        if verify(b) == True : 
            return i 
    return -1

def find_all(board) : 
    all_b = []
    for i,b in enumerate(board) : 
        if verify(b) == True : 
            all_b += [i]
    return all_b
    
    
def play(number, bingos, board) : 
    for n,b in enumerate(bingos) :
        for i in range(5) : 
            for j in range(5) : 
                if b[i][j] == number : 
                    board[n][i][j] = 1
    return board
        

data = data[2:]

bingos = []
bingo = []
for i,j in enumerate(data) : 
    if i%6 == 5: 
        bingos +=  [bingo]
        bingo = []
    else : 
        bingo += [create_line(j)]
bingos += [bingo]

board = [[[0 for i in range(5)]for j in range(5)] for k in range(len(bingos))]


wins = []
for n in numbers : 
    board = play(int(n), bingos, board)
    #print(board[0])
    for b in board : 
        if verify(b) == True : 
            a = find_all(board)
            for i in a : 
                if i not in wins : 
                    wins.append(i)
                    print(i, "ajouter. IL FAUT REGARDER LA DERNIÈRE FOIS QUE CELA S'AFFICHE")
            somme = 0 
            for i in range(5) : 
                for j in range(5) : 
                    if board[wins[-1]][i][j] == 0 : 
                        somme += bingos[wins[-1]][i][j]
            print(int(n), somme)
            print(int(n)*somme)
            break



# print(bingos)
