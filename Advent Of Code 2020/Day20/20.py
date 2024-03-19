import re 
import copy 
from copy import deepcopy 

f = open("Test.txt", "r")

data = [line for line in f.read().split("\n\n")]
print(data[-1], "dernier")
#data = data[0:-1]

for i in range(0,len(data)) : 
	tout = data[i]
	tout = tout.split("\n")
	tile = tout[0]
	piece = tout[1:]
	data[i] = [tile, piece]

premiere_piece = data[0][1]
ligne = premiere_piece[-1]

haut = 0 
bas = 0 
droite = 0 
gauche = 0

def cote_droit(piece) : 
	res = ""
	for i in piece : 
		if i != "" : 
			res += i[-1]
	return res

def cote_gauche(piece) : 
	res = ""
	for i in piece : 
		if i != "" : 
			res += i[0]
	return res

print(data[0]) 

for i in data[1:] : 
	if i[1][1] == ligne : 
		print(i[1][1])

print(cote_gauche(data[0][1]))

dico_data = {}

for i in data : 
	dico_data[int(i[0][5:-1])] = i[1]

liste = []
tout = []
for i in dico_data : 
	tout += [i]

possibles = ["haut", "bas", "droite", "gauche"]

coins = []

def afficher(piece) : 
	for i in piece[1] : 
		print(i) 


for i in data : 
	compte = 0 
	for j in data : 
		if i != j : 
			afficher(i)
			print("\n")
			afficher(j)
			print("suivant")
			if i[1][0] == j[1][-1] : 
				compte += 1
			if i[1][-1] == j[1][0] : 
				compte += 1 
			if cote_gauche(i[1]) == cote_droit(j[1]) : 
				compte += 1
			if cote_droit(i[1]) == cote_gauche(j[1]) : 
				compte += 1
	print(compte)
	if compte == 2 : 
		if int(i[0][5:-1]) not in coins : 
			coins += [int(i[0][5:-1])]
print(coins)


print(len(dico_data))	