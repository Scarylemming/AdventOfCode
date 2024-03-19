import re 

f = open("14.txt", "r")

data = [line.split(" ") for line in f.read().split("\n")]
data = data[0:-1]


def masquer(nombre, mask) : 
	binaire = bin(int(nombre))[2:]
	binaire = "0"*(36 - len(binaire)) + binaire 
	res = ""
	for i in range(0,36) : 
		if mask[i] == "X" : 
			res += binaire[i]
		else : 
			res += mask[i]
	return res
liste = []
for i in data : 
	if i[0] == "mask" : 
		mask = i[2]
	else : 
		if len(liste) == 0 : 
			liste += [[int(i[0][4:-1]), masquer(i[2],mask)]]
		for j in range(0,len(liste)) : 
			if liste[j][0] == int(i[0][4:-1]) : 
				liste[j][1] = masquer(i[2], mask)
				break
			elif j == len(liste)-1 : 
				liste += [[int(i[0][4:-1]), masquer(i[2],mask)]]


somme = 0 
for i in liste : 
	somme += int(i[1],2)
print(somme)
