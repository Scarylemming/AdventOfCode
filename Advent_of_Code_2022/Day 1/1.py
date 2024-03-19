f = open("1.txt", "r")


data = [line for line in f.read().split("\n\n")][:-1]
new_data = []

for i in data : 
    new_data.append([i.split("\n")])
sums = []
for i in new_data : 
    sum = 0
    for j in i[0] : 
        sum += int(j)
    sums.append(sum)

print(max(sums))
