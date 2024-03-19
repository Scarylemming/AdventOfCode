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
			res += "X"
		elif mask[i] == "1" : 
			res += "1" 
		else : 
			res += binaire[i]
	return res
def permutation01(perm) : 
	res = []
	for i in perm : 
		res += [i +  "0"]
		res += [i + "1"]
	return res
def creer_masques(mask) : 
	res = []
	liste_X = []
	for i in range(0,len(mask)) : 
		if mask[i] == "X" : 
			liste_X += [i]
	perm = ["0","1"]
	for i in range(1,len(liste_X)) : 
		perm = permutation01(perm)
	for i in perm : 
		masque = ""
		place_X = 0
		for j in mask : 
			if j == "X" : 
				masque += i[place_X]
				place_X += 1 
			else : 
				masque += j
		res += [masque]


	return res

liste = []
liste_memoire = []
for i in data : 
	print(i)
	if i[0] == "mask" : 
		unique_mask = i[2]
	else : 
		mask = masquer(i[0][4:-1],unique_mask)
		masques = creer_masques(mask)
		#print(masques, "c'est la liste des masques")
		for masque in masques : 
			if int(masque,2) in liste_memoire : 
				for j in range(0,len(liste)) : 
					if liste[j][0] == int(masque,2) : 
						liste[j][1] = i[2]
						break
			else : 
				liste_memoire += [int(masque,2)]
				liste += [[int(masque,2), i[2]]]
liste_memoire.sort()
#print(liste)
#print(liste_memoire)
somme = 0 
for i in liste : 
	somme += int(i[1])
print(somme)
