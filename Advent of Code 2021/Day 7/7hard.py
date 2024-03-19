f = open("7.txt", "r")


data = f.read().split(",")

for i,j in enumerate(data) : 
    data[i] = int(j)
    
def cout(x) : 
    return (x*(x+1)/2)
    
#data = [16,1,2,0,4,2,7,1,2,14]

somme = 100000000000
res = 0
for i in range(max(data)) : 
    compte = 0 
    for j in data : 
        compte += cout(abs(j-i))
    if compte < somme : 
        somme = compte
        res = i
        print(res)
        print(somme)

print(res)
        



