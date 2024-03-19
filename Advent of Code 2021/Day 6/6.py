f = open("6.txt", "r")

data= f.read()


tout = [0 for i in range(9)]

for i in data : 
    for j in range(6) : 
        if i == str(j) : 
            tout[j] += 1

print(tout)

for i in range(256) : 
    new = [0 for j in range(9)]
    for j in range(9) : 
        if j == 0 : 
            new[6] += tout[0]
            new[8] += tout[0]
        else : 
            new[j-1] += tout[j]
    tout = new
    #print(tout)
    
print(sum(tout))