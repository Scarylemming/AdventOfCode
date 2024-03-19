import copy 
from copy import deepcopy 

def one_move(liste,current) :
	for i in enumerate(liste) : 
		if i[1] == current : 
			place = i[0]
			trois_suivants = deepcopy(liste[place+1:place+4])
			print(trois_suivants)
			liste = liste[0:place+1] + liste[place+4:]
			destination = trouver_destination(liste,current)
			break

	for i in enumerate(liste) : 
		if i[1] == destination : 
			nouvelle_place = i[0]
			liste = liste[0:nouvelle_place+1] + trois_suivants + liste[nouvelle_place+1:]
			break

	for i in enumerate(liste) : 
		if i[1] == current : 
			suivant = liste[i[0]+1]
			break

	if place == 6 : 
		liste = liste[1:]
	elif place == 7 : 
		liste = liste[2:]
	elif place == 8 : 
		liste = liste[3:]

	liste = liste[0:9]*2

	return [liste,suivant]

def trouver_destination(liste,current) : 
	destination = current - 1 
	if destination < 1 : 
		destination = 9
	while une_fois(destination, liste) : 
		if destination == 1 : 
			destination = 9 
		else : 
			destination -= 1 
	return destination

def une_fois(destination, liste) : 
	compte = 0
	for i in liste : 
		if i == destination : 
			compte += 1
	if compte == 1 : 
		return True 
	if compte == 2 : 
		return False 
	print("PROBLEMO")
	pass
def afficher_liste(liste) : 
	string = ""
	for i in liste : 
		string += str(i) 
	return string
start = 135468729

liste = []
for i in str(start) : 
	liste += [int(i)]

liste = liste*2 

print(liste)

current = liste[0]
for i in range(0,100) : 
	[liste, current] = one_move(liste,current)

print(liste)

print(afficher_liste(liste))

