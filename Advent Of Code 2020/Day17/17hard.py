from copy import deepcopy

import re 

f = open("Test.txt", "r")

data = [line for line in f.read().split("\n")]
data = data[0:-1]

def faire_3D(matrice) : 
	n = len(matrice[0])
	ligne = []
	etage = []
	for i in range(0,n) : 
		ligne += deepcopy(["."])
	for i in range(0,n) : 
		etage += deepcopy([ligne])

	return [deepcopy([etage]) + matrice + deepcopy([etage])]


def affichage(matrice) : 
	ensemble = ""

	for i in matrice : 
		cube = ""
		for j in i : 
			etage = ""
			for k in j : 
				ligne = ""
				for l in k : 
					ligne += l 
				etage += ligne + "\n" 
			cube += etage + "\n"
		ensemble += cube + "\n\n"

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
	cube = []
	for i in range(0,n) : 
		ligne += deepcopy(["."])
	for i in range(0,n) : 
		etage += deepcopy([ligne])
	for i in range(0,n) : 
		cube += deepcopy([etage])

	for i in range(0,len(matrice)) : 
		for j in range(0,len(matrice[i])) : 
			for k in range(0,len(matrice[i][j])) : 
				matrice[i][j][k] = deepcopy(["."]) + matrice[i][j][k] + deepcopy(["."])
			matrice[i][j] = deepcopy([ligne]) + matrice[i][j] + deepcopy([ligne])
		matrice[i] = deepcopy([etage]) + matrice[i] + deepcopy([etage])
	
	matrice = deepcopy([cube]) + matrice + deepcopy([cube])

	return matrice

def voisins(coord,n,l) : 
	res = []
	for i in [-1,0,1] : 
		if 0 <= coord[0] + i <= l-1: 
			for j in [-1,0,1] : 
				if 0 <= coord[1] + j <= n-1 : 
					for k in [-1,0,1] : 
						if 0 <= coord[2] + k <= n-1 : 
							for l in [-1,0,1] : 
								if 0 <= coord[3] + l <= n-1 : 
									vois = [[coord[0]+i, coord[1]+j, coord[2]+k, coord[3]+l]]
									if [coord] != vois : 
										res += vois
	return res 

def changer(matrice) : 

	matrice = agrandir(matrice)
	
	ancien = deepcopy(matrice)

	print("ancienne configuration")

	print(affichage(ancien))

	n = len(matrice[0])
	for i in range(0,len(matrice)) : 
		for j in range(0,n) : 
			for k in range(0,n) : 
				for l in range(0,n) : 
					compte = 0
					print(voisins([i,j,k,l],n,len(matrice)))
					for voisin in voisins([i,j,k,l],n,len(matrice)) : 
						#print(voisin,len(matrice[voisin[0]]),len(matrice[voisin[0]]))
						if ancien[voisin[0]][voisin[1]][voisin[2]][voisin[3]] == "#" : 
							compte += 1 
					print([i,j,k,l], compte)
					if ancien[i][j][k][l] == "." : 
						if compte == 3 : 
							matrice[i][j][k][l] = "#"
					elif ancien[i][j][k][l] == "#" : 
						if compte not in [2,3] : 
							matrice[i][j][k][l] = "."
				#print(affichage(matrice))
	return matrice 

a = faire_matrice(data)
a = faire_3D(a)
print(affichage(a))
a = changer(a)

print(affichage(a))