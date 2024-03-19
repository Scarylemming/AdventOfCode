import copy

f = open("3.txt", "r")


data_base = [line for line in f.read().split("\n")][:-1]

#data_base  =["00100", "11110", "10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]

a = ""
b = ""

data = copy.deepcopy(data_base)

for j in range(len(data[0])) : 
    if len(data) == 1 : 
        a = data[0]
        break
    count = 0 
    ones = 0 
    for i in range(len(data)) : 
        if data[i][j] == "1" : 
            ones += 1
        count += 1
    if 2 * ones >= count : 
        a += "1"
    else : 
        a += "0"
    data_new = []
    for i in data : 
        if i[0:len(a)] == a : 
            data_new.append(i)
    data = data_new

data = copy.deepcopy(data_base)
for j in range(len(data[0])) : 
    if len(data) == 1 : 
        b = data[0] 
        break
    count = 0 
    ones = 0 
    for i in range(len(data)) : 
        if data[i][j] == "1" : 
            ones += 1
        count += 1
    if 2 * ones >= count : 
        b += "0"
    else : 
        b += "1"
    data_new = []
    for i in data : 
        if i[0:len(b)] == b : 
            data_new.append(i)
    data = data_new
        
print(a,b)
        
print(int(a, 2), int(b,2))

print(int(a, 2) * int(b, 2))
        