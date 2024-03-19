import re 

f = open("18.txt", "r") 

data = [line.split(" ") for line in f.read().split("\n")]

data = data[0:-1]

def faire_operation(operation,res,n) : 
	if operation == "plus" : 
		return res + n 
	if operation == "fois" : 
		return res * n 

def effectuer_calcul(string) : 
	 #print(string)
	res = 0 
	operation = "plus"
	nombre = ""
	for i in range(0,len(string)) : 
		#print(res,string[i],"nombre", nombre)
		if string[i] in "1234567890" :
			if nombre == "" : 
				if i == len(string)-1 : 
					nombre += string[i]
					res = faire_operation(operation,res,int(nombre))
					nombre = ""
				elif (i != len(string) - 1) & (string[i+1] not in "1234567890") : 
					nombre += string[i]
					res = faire_operation(operation,res,int(nombre))
					nombre = ""
				else : 
					nombre += string[i]
			elif i != len(string) - 1 : 
				if string[i+1] in "1234567890" : 
					nombre += string[i]
				else : 
					nombre += string[i]
					res = faire_operation(operation,res,int(nombre))
					nombre = ""
			else : 
				nombre += string[i]
				res = faire_operation(operation,res,int(nombre))
		elif string[i] in "+*" : 
			if string[i] == "+" : 
				operation = "plus" 
			else : 
				operation = "fois"
		else : 
			print("PROBLEME")
	#print(res)
	return res 

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

test = instructions[0]


somme = 0 
for i in instructions : 
	somme += enlever_parentheses(i)

print(somme)
