liste = [19,0,5,1,10,13]

def jouer(liste) : 
	nombre = liste[-1]
	test = 0
	if nombre not in liste[0:-1] : 
		return liste + [0]
	for i in range(2,len(liste)+1) : 
		if liste[-i] == nombre : 
			#print(liste, i-1)
			liste += [i-1]
			test = 1 
			break 
	if test == 0 : 
		print("je ne sais pas ce qu'il s'est passé")
	return liste


for i in range(0,20000-len(liste)) :
	if i%100000 == 0 : 
		print(i) 
	liste = jouer(liste) 
print(liste[-1])