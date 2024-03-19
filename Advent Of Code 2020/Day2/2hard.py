import re 

f = open("2.txt", "r") 

data = [line.split(" ") for line in f.read().split("\n")]
data = data[0:len(data) - 1]

compte = 0 
for i in data :
	policy = i[0].split("-") 
	place1 = int(policy[0])
	place2 = int(policy[1])
	lettre = i[1][0]
	compte_lettre = 0
	if i[2][place1-1] == lettre : 
		compte_lettre += 1 
	if i[2][place2-1] == lettre : 
		compte_lettre += 1 
	if compte_lettre == 1 : 
		compte += 1


print(compte)