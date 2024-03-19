import re 

f = open("1.txt", "r") 

data = [line for line in f.read().split("\n")]
data = data[0:len(data)-1]
for i in range(0,len(data)) : 
	data[i] = int(data[i])

for i in range(0,len(data)) : 
	for j in range(i,len(data)) : 
		if (2020 - data[i] - data[j]) in data : 
			if (2020 - data[i] - data[j]) != i != j : 
				print(data[i] * data[j] * (2020 - data[i] - data[j]), data[i] , data[j] , (2020 - data[i] - data[j]))
