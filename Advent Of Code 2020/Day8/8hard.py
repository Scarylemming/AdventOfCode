import re 

f = open("8.txt", "r")

data = [line.split(" ") for line in f.read().split("\n")]
if data[-1] == [""] : 
	data = data[0:len(data)-1]

def faire_boucle(data) : 
	place = 0 
	accumulateur = 0 
	liste_places_visitées = []
	test = 0
	while place not in liste_places_visitées : 
		if place >= len(data) :
			test = 1
			break
		liste_places_visitées += [place]
		if data[place][0] == "acc" : 
			accumulateur += int(data[place][1])
			place += 1
		elif data[place][0] == "jmp" : 
			place += int(data[place][1]) 
		elif data[place][0] == "nop" : 
			place += 1 
	if test == 1 : 
		return accumulateur
	else : 
		return 0

somme = 0 

for i in range(0,len(data)) :
	if data[i][0] == "jmp" : 
		data[i][0] = "nop" 
		somme += faire_boucle(data)

		data[i][0] = "jmp"
	if data[i][0] == "nop" :  
		data[i][0] = "jmp" 
		somme += faire_boucle(data)

		data[i][0] = "nop"

print(somme)
