import re 

f = open("5.txt", "r") 

data = [line for line in f.read().split("\n")]

def debinariser(seat) : 
	res = ""
	for i in seat : 
		if i in ["F", "L"] : 
			res += "0"
		else : 
			res += "1"

	return res 

def retrouver_ID(n) : 
	res = ""
	binaire = bin(n)[2:]
	print(binaire) 
	for i in range(0,7) : 
		if binaire[i] == "0" : 
			res += "F"
		else :
			res += "B"
	for i in range(7,10) : 
		if binaire[i] == "0" : 
			res += "L"
		else : 
			res += "R"
	return res 


data = data[0:len(data)-1]
maximum = 0 
toutes_infos = []
liste_nombres = []
for i in data : 
	toutes_infos += [[i,debinariser(i), int(debinariser(i),2)]]
	maximum = max(maximum, int(debinariser(i),2))
	liste_nombres += [int(debinariser(i),2)]
liste_nombres.sort()
#print(liste_nombres)
for i in range(0,len(liste_nombres)-1) : 
	if liste_nombres[i]+1 not in liste_nombres : 
		print(liste_nombres[i]+1)
		#print(retrouver_ID(liste_nombres[i] +1))


