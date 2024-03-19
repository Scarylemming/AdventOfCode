f = open("1.txt", "r")


data = [line for line in f.read().split("\n")][:-1]
data_int = [int(i) for i in data]

test = [1,2,3,4,5]
somme = 0 

for i in range(len(data)-1) : 
    if data_int[i] < data_int[i+1] : 
        somme += 1

print(somme)




