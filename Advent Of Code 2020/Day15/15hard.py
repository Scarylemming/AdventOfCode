import copy
liste = [19,0,5,1,10,13]
liste1 = [0,3,6]

def creer_liste(liste) : 
	res = [liste[-1]]
	for i in range(0,len(liste)) : 
		res += [[liste[i],i]]
	return res 

def jouer(liste,n) : 
	nombre = liste[0]
	for i in range(1,len(liste)) : 
		if liste[i][0] == nombre : 
			if len(liste[i]) == 2 : 
				nouveau = 0
			else : 
				nouveau = liste[i][2]-liste[i][1]
	#print(liste,nouveau)
	liste[0] = nouveau
	test = 0
	for i in range(1,len(liste)) : 
		if liste[i][0] == nouveau :
			if len(liste[i]) == 2 : 
				liste[i] += [n-1]
			else : 
				liste[i][1] = liste[i][2] 
				liste[i][2] = n-1
			test = 1
			break 
	if test == 0 : 
		liste += [[nouveau,n-1]]

	return liste
liste = creer_liste(liste)
n = 20000
for i in range(len(liste)-1,n) : 
	liste = jouer(liste,i+1)

print(liste[0])
print(liste)