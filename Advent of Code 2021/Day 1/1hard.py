f = open("1.txt", "r")


data = [line for line in f.read().split("\n")][:-1]
data = [int(i) for i in data]


new_data = []
for i in range(len(data)-2) : 
    new_data.append(data[i] + data[i+1] + data[i+2])
somme = 0 

data_int = new_data
for i in range(len(new_data)-1) : 
    if data_int[i] < data_int[i+1] : 
        somme += 1

print(somme)




