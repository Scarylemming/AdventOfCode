import re 

f = open("18.txt", "r") 

data = [line.split(" ") for line in f.read().split("\n")]

data = data[0:-1]

def faire_operation(operation,res,n) : 
	if operation == "plus" : 
		return res + n 
	if operation == "fois" : 
		return res * n 

def separer(string) : 
	res = []
	nombre = ""
	for i in string : 
		if i in "1234567890" : 
			nombre += i 
		else : 
			res += [nombre]
			nombre = ""
			res += [i]
	res += [nombre]

	return res 

def faire_plus(liste) : 
	while "+" in liste : 
		for i in range(0,len(liste)) : 
			if liste[i] == "+" : 
				if i == 1 : 
					liste = [str(int(liste[0]) + int(liste[2]))] + liste[3:]
				else : 
					liste = liste[0:i-1] + [str(int(liste[i-1]) + int(liste[i+1]))] + liste[i+2:]
				break 
	return liste 

def faire_fois(liste) : 
	res = 1 
	for i in liste : 
		if i != "*" : 
			res *= int(i) 
	return res 

def effectuer_calcul(string) : 
	string = separer(string) 
	string = faire_plus(string) 
	string = faire_fois(string) 
	return string 


def enlever_parentheses(string) : 
	place_derniere_ouverte = 0
	while "(" in string :
		for i in range(0,len(string)) : 
			if string[i] == "(" : 
				place_derniere_ouverte = i
			elif string[i] == ")" : 
				place_premiere_fermee = i 
				break 
		resultat_interne = effectuer_calcul(string[place_derniere_ouverte+1:place_premiere_fermee])
		#print(resultat_interne)
		string = string[0:place_derniere_ouverte] + str(resultat_interne) + string[place_premiere_fermee+1:]
		#print(string)

	return effectuer_calcul(string)

instructions = []

for line in data : 
	ligne = ""
	for i in line : 
		ligne += i 
	instructions += [ligne]


somme = 0

for i in instructions : 
	somme += enlever_parentheses(i) 

print(somme)
