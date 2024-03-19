from copy import deepcopy

import re 

f = open("Test.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:-1]

def affichage(matrice) : 
	ensemble = ""

	for i in matrice : 
		etage = ""
		for j in i : 
			ligne = ""
			for k in j : 
				ligne += k 
			etage += ligne + "\n"
		ensemble += etage + "\n\n"

	return ensemble

def faire_matrice(data) : 
	res = []
	for i in data : 
		etage = []
		for j in i : 
			ligne = []
			for k in j : 
				ligne += [k]
			etage += ligne
		res += [etage]
	return [res] 

def agrandir(matrice) : 
	n = len(matrice[0])+2
	etage = []
	ligne = []
	for i in range(0,n) : 
		ligne += deepcopy(["."])
	for i in range(0,n) : 
		etage += deepcopy([ligne])

	for i in range(0,len(matrice)) : 
		for j in range(0,len(matrice[i])) : 
			matrice[i][j] = deepcopy(["."]) + matrice[i][j] + deepcopy(["."])
		matrice[i] = deepcopy([ligne]) + matrice[i] + deepcopy([ligne])
	
	matrice = deepcopy([etage]) + matrice + deepcopy([etage])

	return matrice

def voisins(coord,n,l) : 
	res = []
	for i in [-1,0,1] : 
		if 0 <= coord[0] + i <= l-1: 
			for j in [-1,0,1] : 
				if 0 <= coord[1] + j <= n-1 : 
					for k in [-1,0,1] : 
						if 0 <= coord[2] + k <= n-1 : 
							vois = [[coord[0]+i, coord[1]+j, coord[2]+k]]
							if [coord] != vois : 
								res += vois

	return res 

def changer(matrice) : 

	matrice = agrandir(matrice)
	
	ancien = deepcopy(matrice)

	#print("ancienne configuration")

	#print(affichage(ancien))

	n = len(matrice[0])
	for i in range(0,len(matrice)) : 
		for j in range(0,n) : 
			for k in range(0,n) : 
				compte = 0
				for voisin in voisins([i,j,k],n,len(matrice)) : 
					#print(voisin,len(matrice[voisin[0]]),len(matrice[voisin[0]]))
					if ancien[voisin[0]][voisin[1]][voisin[2]] == "#" : 
						compte += 1 
				#print([i,j,k], compte)
				if ancien[i][j][k] == "." : 
					if compte == 3 : 
						matrice[i][j][k] = "#"
				elif ancien[i][j][k] == "#" : 
					if compte not in [2,3] : 
						matrice[i][j][k] = "."
				#print(affichage(matrice))
	return matrice 

a = faire_matrice(data)
print(a)

for i in range(0,6) : 
	#print(affichage(a))
	a = changer(a)
#print(affichage(a))

somme = 0 
for i in affichage(a) : 
	for j in i : 
		for k in j : 
			if k == "#" : 
				somme += 1 
print(somme)