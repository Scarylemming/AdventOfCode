import re

f = open("10.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:-1]
for i in range(0,len(data)) : 
	data[i] = int(data[i])
data += [0]
data.sort()


groupes = []
groupe = []
for i in data : 
	if groupe == [] : 
		groupe += [i]
	elif groupe[-1]+1 == i : 
		groupe += [i]
	else : 
		groupes += [groupe]
		groupe = [i]


produit = 1 
for i in groupes : 
	if len(i) == 3 : 
		produit *= 2 
	elif len(i) == 4 : 
		produit *= 4 
	elif len(i) == 5 : 
		produit *= 7 
print(produit)


