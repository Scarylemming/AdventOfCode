f = open("8.txt", "r")


data = [line.split("|") for line in f.read().split("\n")][:-1]

print(data[0])

somme = 0

for i in data : 
    a = i[1].split(" ")[1:]
    for j in a : 
        if len(j) in [2,3,4,7]:
            somme += 1
            

print(somme)





