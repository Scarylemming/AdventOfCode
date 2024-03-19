import re 

f = open("2.txt", "r") 

data = [line.split(" ") for line in f.read().split("\n")]
data = data[0:len(data) - 1]

compte = 0 
for i in data :
	policy = i[0].split("-") 
	minimum = int(policy[0])
	maximum = int(policy[1])
	lettre = i[1][0]
	compte_lettre = 0
	for j in i[2] : 
		if j == lettre : 
			compte_lettre += 1 
	if minimum <= compte_lettre <= maximum : 
		compte += 1 

print(compte)